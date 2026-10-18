#!/usr/bin/env python3
"""Check a book's passages and draw its branch map.

Usage: python3 tools/check.py [book] [passage]

  book: a book name (parachute), a book folder (books/parachute) or any
        folder of passages (examples). Default: the only book in books/.
  passage: show where that passage comes from and the shortest path to it
        from the start, instead of checking the whole book.

Errors break the book (broken links, dead ends, bad frontmatter).
A passage with no text and no choices is a stub: listed as 'to write', not an error.
Warnings are guidelines (line counts, orphans, ending balance): Joep's
forms are inspiration, not hard rules, so these never fail the check.

The branch map is written to build/<book>-map.html.
"""

import html
import sys
from collections import deque
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TYPES = {"page", "joepie", "ending"}
MOODS = {"good", "bad"}
MAX_LINES = 5  # Joep's five-liner (Joep Luycx, "Doe als ik, schrijf als jij")


class Passage:
    def __init__(self, path, meta, body):
        self.path = path
        self.meta = meta
        self.body = body
        self.id = str(meta.get("id", ""))
        self.type = meta.get("type")
        self.choices = meta.get("choices") or []

    @property
    def targets(self):
        return [str(c.get("to")) for c in self.choices if isinstance(c, dict)]

    @property
    def is_stub(self):
        return not self.choices and not self.body.strip()

    @property
    def lines(self):
        return [l for l in self.body.splitlines() if l.strip()]


def load(folder, errors):
    passages = {}
    for path in sorted(folder.glob("*.md")):
        if path.name.startswith("_") or path.name.lower() == "readme.md":
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{path.name}: no frontmatter (should start with ---)")
            continue
        try:
            _, front, body = text.split("---", 2)
            meta = yaml.safe_load(front) or {}
        except (ValueError, yaml.YAMLError) as e:
            errors.append(f"{path.name}: frontmatter can't be read ({e.__class__.__name__})")
            continue
        p = Passage(path, meta, body.strip("\n"))
        if not p.id:
            errors.append(f"{path.name}: missing id")
            continue
        if p.id != path.stem:
            errors.append(f"{path.name}: id is '{p.id}' but the file is named '{path.stem}'")
        passages[p.id] = p
    return passages


def split_joepie(p):
    """Return (blocks, invitation). Blocks are (heading, lines) pairs.

    The invitation is whatever follows a blank line after the last block.
    """
    blocks, current = [], None
    for line in p.body.splitlines():
        if line.startswith("## "):
            current = [line[3:].strip(), []]
            blocks.append(current)
        elif current is not None:
            current[1].append(line)
    invitation = []
    if blocks:
        last = blocks[-1][1]
        while last and not last[0].strip():
            last.pop(0)
        if "" in [l.strip() for l in last]:
            cut = [l.strip() for l in last].index("")
            invitation = [l for l in last[cut:] if l.strip()]
            del last[cut:]
    return [(h, [l for l in ls if l.strip()]) for h, ls in blocks], invitation


def check_passage(p, ids, errors, warnings):
    name = p.path.name
    if p.type not in TYPES:
        errors.append(f"{name}: type is '{p.type}', should be one of {', '.join(sorted(TYPES))}")
        return
    if p.is_stub and p.type != "ending":
        return

    for c in p.choices:
        if not isinstance(c, dict) or "to" not in c:
            errors.append(f"{name}: a choice is missing 'to'")
        elif str(c["to"]) not in ids:
            errors.append(f"{name}: broken link → '{c['to']}' doesn't exist")
        if isinstance(c, dict) and not c.get("text"):
            warnings.append(f"{name}: a choice has no 'text' label")

    for line in p.lines:
        if "turn to page" in line.lower():
            warnings.append(f"{name}: 'Turn to page' in the text; the build adds it")
        if line.strip().upper().startswith("THE END"):
            warnings.append(f"{name}: 'THE END' in the text; the build adds it")

    if p.type == "ending":
        if p.choices:
            errors.append(f"{name}: an ending has choices")
        if p.meta.get("mood") not in MOODS:
            errors.append(f"{name}: ending mood is '{p.meta.get('mood')}', should be good or bad")
        if not p.lines:
            warnings.append(f"{name}: ending has no text yet")
        elif len(p.lines) > MAX_LINES:
            warnings.append(f"{name}: {len(p.lines)} lines (guideline: {MAX_LINES})")
        return

    if not p.choices:
        errors.append(f"{name}: dead end, a {p.type} with no choices")

    if p.type == "page":
        if not p.lines:
            warnings.append(f"{name}: page has no text yet")
        elif len(p.lines) > MAX_LINES:
            warnings.append(f"{name}: {len(p.lines)} lines (guideline: {MAX_LINES})")
        return

    # joepie
    if not p.meta.get("title"):
        warnings.append(f"{name}: Joepie has no title")
    blocks, invitation = split_joepie(p)
    if len(blocks) != 3:
        warnings.append(f"{name}: {len(blocks)} headed blocks (guideline: 3)")
    for heading, lines in blocks:
        if len(lines) > MAX_LINES:
            warnings.append(f"{name}: block '{heading}' has {len(lines)} lines (guideline: {MAX_LINES})")
    if blocks and not invitation:
        warnings.append(f"{name}: no invitation line after the last block (leave a blank line before it)")


def reachable(start, passages):
    """Shortest number of choices from start to every reachable passage."""
    depth, queue = {start: 0}, deque([start])
    while queue:
        cur = queue.popleft()
        for t in passages[cur].targets:
            if t in passages and t not in depth:
                depth[t] = depth[cur] + 1
                queue.append(t)
    return depth


def can_end(passages):
    """Passages from which at least one ending can be reached."""
    ok = {i for i, p in passages.items() if p.type == "ending" or p.is_stub}
    changed = True
    while changed:
        changed = False
        for i, p in passages.items():
            if i not in ok and any(t in ok for t in p.targets):
                ok.add(i)
                changed = True
    return ok


def balance(passages, warnings):
    endings = [p for p in passages.values() if p.type == "ending"]
    good = [p for p in endings if p.meta.get("mood") == "good"]
    bad = [p for p in endings if p.meta.get("mood") == "bad"]
    n = len(passages)
    summary = f"{n} passage{'s' * (n != 1)}, {len(endings)} ending{'s' * (len(endings) != 1)} ({len(good)} good, {len(bad)} bad)"
    if len(good) > 2:
        warnings.append(f"balance: {len(good)} good endings (playbook: only 1 or 2 truly good)")
    if endings and len(bad) < len(good):
        warnings.append("balance: fewer bad endings than good ones (playbook: bad endings short and plentiful)")
    written = sum(1 for p in passages.values() if not p.is_stub)  # stubs may still become endings
    if written >= 10:
        ratio = len(endings) / written
        if not 0.12 <= ratio <= 0.30:
            warnings.append(
                f"balance: endings are {ratio:.0%} of passages (playbook: about 5 in 25, 15 to 25 in 100)"
            )
    return summary


MERMAID_STYLE = """
classDef page fill:#eef2f7,stroke:#5b6b82,color:#1d2433;
classDef joepie fill:#fff4d6,stroke:#b8860b,stroke-width:3px,color:#1d2433;
classDef good fill:#dff3e4,stroke:#2e7d4f,color:#1d2433;
classDef bad fill:#fbe3e1,stroke:#b3402e,color:#1d2433;
classDef missing fill:#ffffff,stroke:#b3402e,stroke-dasharray:4 3,color:#b3402e;
classDef orphan stroke-dasharray:6 4;
classDef stub fill:#ffffff,stroke:#9aa5b5,stroke-dasharray:2 3,color:#5b6b82;
classDef start stroke-width:4px;
"""


def mermaid(passages, start, depth, folder):
    node = {}

    def nid(i):
        return node.setdefault(i, f"n{len(node)}")

    def label(s):
        return s.replace('"', "'")

    out = ["flowchart TD"]
    for i, p in passages.items():
        if p.type == "joepie":
            text = f"{i}<br/><i>{label(str(p.meta.get('title', '')))}</i>"
        elif p.type == "ending":
            text = f"{i}<br/>END · {p.meta.get('mood', '?')}"
        else:
            text = i
        shape = ('(["', '"])') if p.type == "ending" else ('["', '"]')
        out.append(f"  {nid(i)}{shape[0]}{label(text)}{shape[1]}")
        cls = p.meta.get("mood") if p.type == "ending" else p.type
        out.append(f"  class {nid(i)} {cls if cls in ('page', 'joepie', 'good', 'bad') else 'page'}")
        if p.is_stub:
            out.append(f"  class {nid(i)} stub")
        if start and i not in depth:
            out.append(f"  class {nid(i)} orphan")
        rel = Path("..") / p.path.relative_to(ROOT) if p.path.is_relative_to(ROOT) else p.path
        out.append(f'  click {nid(i)} href "{rel.as_posix()}" _blank')
    if start in passages:
        out.append(f"  class {nid(start)} start")
    for i, p in passages.items():
        for c in p.choices:
            if not isinstance(c, dict) or "to" not in c:
                continue
            t = str(c["to"])
            if t not in passages:
                out.append(f'  {nid(t)}["{label(t)}<br/>missing"]')
                out.append(f"  class {nid(t)} missing")
            edge = label(str(c.get("text", "")))
            out.append(f'  {nid(i)} -->|"{edge}"| {nid(t)}' if edge else f"  {nid(i)} --> {nid(t)}")
    out.append(MERMAID_STYLE)
    return "\n".join(out)


def write_map(name, folder, passages, start, depth, summary, errors, warnings):
    out = ROOT / "build" / f"{name}-map.html"
    out.parent.mkdir(exist_ok=True)
    issues = "".join(f'<li class="err">{html.escape(e)}</li>' for e in errors)
    issues += "".join(f'<li class="warn">{html.escape(w)}</li>' for w in warnings)
    graph = mermaid(passages, start, depth, folder) if passages else "flowchart TD\n  empty[No passages yet]"
    out.write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Branch map: {html.escape(name)}</title>
<style>
  body {{ font: 15px/1.5 system-ui, sans-serif; margin: 24px 16px; color: #1d2433; background: #fafaf7; }}
  h1 {{ font-size: 20px; margin: 0 0 4px; }}
  .sum {{ color: #5b6b82; margin: 0 0 16px; }}
  .legend span {{ display: inline-block; padding: 2px 8px; margin: 0 6px 6px 0; border: 1px solid; border-radius: 4px; font-size: 13px; }}
  #map {{ overflow-x: auto; background: #fff; border: 1px solid #e3e3dc; border-radius: 8px; padding: 16px; }}
  ul {{ padding-left: 20px; }} .err {{ color: #b3402e; }} .warn {{ color: #8a6d00; }}
</style></head><body>
<h1>Branch map: {html.escape(name)}</h1>
<p class="sum">{html.escape(summary)}. Click a passage to open its file.</p>
<div class="legend">
  <span style="background:#eef2f7;border-color:#5b6b82">page</span>
  <span style="background:#fff4d6;border-color:#b8860b">Joepie</span>
  <span style="background:#dff3e4;border-color:#2e7d4f">good ending</span>
  <span style="background:#fbe3e1;border-color:#b3402e">bad ending</span>
  <span style="border-style:dashed;border-color:#b3402e;color:#b3402e">missing</span>
  <span style="border-style:dashed;border-color:#5b6b82">orphan</span>
  <span style="border-style:dotted;border-color:#9aa5b5;color:#5b6b82">to write</span>
  <span style="border-width:3px;border-color:#1d2433">start</span>
</div>
<div id="map"><pre class="mermaid">{html.escape(graph)}</pre></div>
<h2>Issues</h2>
<ul>{issues or "<li>None.</li>"}</ul>
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
  mermaid.initialize({{ startOnLoad: true, securityLevel: "loose", flowchart: {{ htmlLabels: true }} }});
</script>
</body></html>
""",
        encoding="utf-8",
    )
    return out


def resolve(arg):
    """Return (name, passages folder) for a book name, book folder or plain folder."""
    books = ROOT / "books"
    if arg is None:
        found = sorted(d.name for d in books.iterdir() if d.is_dir()) if books.is_dir() else []
        if len(found) != 1:
            sys.exit(f"Which book? python3 tools/check.py <book>  (books: {', '.join(found) or 'none'})")
        arg = found[0]
    path = ROOT / arg
    if not path.is_dir() and (books / arg).is_dir():
        path = books / arg
    if not path.is_dir():
        sys.exit(f"No book or folder called '{arg}'")
    folder = path / "passages" if (path / "passages").is_dir() else path
    return path.name, folder


def label_of(p, target):
    for c in p.choices:
        if isinstance(c, dict) and str(c.get("to")) == target:
            return c.get("text", "")
    return ""


def show_passage(pid, passages):
    if pid not in passages:
        sys.exit(f"No passage '{pid}'")
    p = passages[pid]
    state = "empty, to write" if p.is_stub else p.type
    if p.type == "ending" and not p.is_stub:
        state = f"ending, {p.meta.get('mood', '?')}"
    print(f"{pid} ({state})")
    if p.meta.get("note"):
        print(f"Note:        {p.meta['note']}")

    parents = [(i, label_of(q, pid)) for i, q in passages.items() if pid in q.targets]
    print("\nComes from:  " + (", ".join(f'{i} ("{t}")' for i, t in parents) if parents else ("nowhere (this is the start)" if p.meta.get("start") else "nowhere")))
    if p.choices:
        print("Leads to:    " + ", ".join(f'{t} ("{label_of(p, t)}")' for t in dict.fromkeys(p.targets)))

    starts = [i for i, q in passages.items() if q.meta.get("start")]
    if len(starts) != 1:
        return
    prev, queue = {starts[0]: None}, deque([starts[0]])
    while queue:
        cur = queue.popleft()
        for t in passages[cur].targets:
            if t in passages and t not in prev:
                prev[t] = cur
                queue.append(t)
    if pid not in prev:
        print(f"\nNo path from the start ({starts[0]}).")
        return
    path = [pid]
    while prev[path[-1]] is not None:
        path.append(prev[path[-1]])
    path.reverse()
    steps = [path[0]]
    for a, b in zip(path, path[1:]):
        steps += [f'"{label_of(passages[a], b)}"', b]
    print("\nShortest path from the start:\n  " + " → ".join(steps))


def main():
    name, folder = resolve(sys.argv[1] if len(sys.argv) > 1 else None)
    if len(sys.argv) > 2:
        show_passage(sys.argv[2], load(folder, []))
        return
    errors, warnings = [], []
    passages = load(folder, errors)
    ids = set(passages)

    for p in passages.values():
        check_passage(p, ids, errors, warnings)

    starts = [i for i, p in passages.items() if p.meta.get("start")]
    start, depth = None, {}
    if passages and not starts:
        errors.append("no passage has 'start: true'")
    elif len(starts) > 1:
        errors.append(f"more than one start: {', '.join(starts)}")
    if len(starts) == 1:
        start = starts[0]
        depth = reachable(start, passages)
        for i in sorted(ids - set(depth)):
            warnings.append(f"{passages[i].path.name}: orphan, can't be reached from '{start}'")

    endable = can_end(passages)
    trapped = [i for i, p in passages.items() if p.type != "ending" and p.choices and i not in endable]
    for i in trapped:
        warnings.append(f"{passages[i].path.name}: stuck, no ending can be reached from here (a loop or broken links)")

    summary = balance(passages, warnings)
    out = write_map(name, folder, passages, start, depth, summary, errors, warnings)

    print(f"{name}: {summary}")
    endings = sorted((p for p in passages.values() if p.type == "ending"), key=lambda p: depth.get(p.id, 999))
    if endings:
        print("\nEndings (choices from start):")
        for p in endings:
            print(f"  {p.meta.get('mood', '?'):4}  {p.id}  ({depth.get(p.id, 'unreachable')})")
    stubs = [p.id for p in passages.values() if p.is_stub]
    if stubs:
        print(f"\nTo write ({len(stubs)}): {', '.join(stubs)}")
    print(f"\nErrors ({len(errors)}):" if errors else "\nErrors: none")
    for e in errors:
        print(f"  ✗ {e}")
    print(f"\nWarnings ({len(warnings)}):" if warnings else "\nWarnings: none")
    for w in warnings:
        print(f"  ! {w}")
    print(f"\nMap: {out.relative_to(ROOT)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
