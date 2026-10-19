#!/usr/bin/env python3
"""Build a clickable version of a book: one page at a time, like the printed book.

Usage: python3 tools/build.py [book] [passage]

Page numbers are assigned here (start = page 1, then in reading order), and
the "Turn to page N" choices and "THE END." are added, as the playbook says.
Stubs show as "not written yet". Output: build/<book>.html

With a passage id, print that one passage as plain text instead, the way it
would be printed, for pasting into a chat. Nothing is written.

The HTML opens at a page number or a passage id: parachute.html#7 or
parachute.html#lake-roof.
"""

import html
import json
import sys
from collections import deque

from check import ROOT, load, resolve


def page_numbers(passages):
    """Start is page 1; then breadth-first along the choices; unreachable last."""
    starts = [i for i, p in passages.items() if p.meta.get("start")]
    order, queue = [], deque(starts[:1])
    seen = set(queue)
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for t in passages[cur].targets:
            if t in passages and t not in seen:
                seen.add(t)
                queue.append(t)
    order += sorted(set(passages) - seen)
    return {pid: n for n, pid in enumerate(order, 1)}


def blocks(p):
    """The text as (heading, lines) blocks. Only Joepies have headings."""
    out, current = [], [None, []]
    for line in p.body.splitlines():
        if p.type == "joepie" and line.startswith("## "):
            if current[0] or current[1]:
                out.append(current)
            current = [line[3:].strip(), []]
        elif line.strip():
            current[1].append(line.strip())
        elif current[1]:
            out.append(current)
            current = [None, []]
    if current[0] or current[1]:
        out.append(current)
    return out


def preview(pid, passages, numbers):
    """One passage as plain text, as printed: headings, THE END., Turn to page N."""
    if pid not in passages:
        sys.exit(f"No passage '{pid}'")
    p = passages[pid]
    out = [f"Page {numbers[pid]} · {pid} ({p.type}{', ' + p.meta['mood'] if p.meta.get('mood') else ''})", ""]
    if p.meta.get("title"):
        out += [p.meta["title"], ""]
    if p.is_stub:
        out.append("Not written yet.")
        if p.meta.get("note"):
            out.append(f"Note: {p.meta['note']}")
        if p.meta.get("suggestion"):
            out.append(f"Suggestion (not the author's): {p.meta['suggestion']}")
        out.append("")
    for head, lines in blocks(p):
        if head:
            out.append(f"~ {head} ~")
        out += lines + [""]
    if p.type == "ending":
        out.append("THE END.")
        if p.meta.get("card"):
            out.append(p.meta["card"])
    for c in p.choices:
        if isinstance(c, dict):
            to = numbers.get(str(c.get("to")))
            out.append(f"{str(c.get('text', '')).rstrip('?')}? " + (f"Turn to page {to}." if to else "(page missing)"))
    return "\n".join(out).strip()


def main():
    name, folder = resolve(sys.argv[1] if len(sys.argv) > 1 else None)
    passages = load(folder, [])
    if not passages:
        sys.exit(f"{name}: no passages yet")
    numbers = page_numbers(passages)
    if len(sys.argv) > 2:
        print(preview(sys.argv[2], passages, numbers))
        return

    pages = {}
    for pid, p in passages.items():
        pages[numbers[pid]] = {
            "id": pid,
            "type": p.type,
            "mood": p.meta.get("mood"),
            "title": p.meta.get("title"),
            "card": p.meta.get("card"),
            "stub": p.is_stub,
            "note": p.meta.get("note"),
            "suggestion": p.meta.get("suggestion"),
            "blocks": blocks(p),
            "choices": [
                {"text": c.get("text", ""), "to": numbers.get(str(c.get("to")))}
                for c in p.choices
                if isinstance(c, dict)
            ],
        }

    data = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
    title = html.escape(name.replace("-", " ").title())
    out = ROOT / "build" / f"{name}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(TEMPLATE.replace("{{TITLE}}", title).replace("{{DATA}}", data), encoding="utf-8")
    print(f"{name}: {len(pages)} pages → {out.relative_to(ROOT)}")


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<style>
  :root {
    --paper: #f6f1e7; --ink: #23201b; --soft: #7a7266; --line: #ddd3c2;
    --card: #fffdf8; --accent: #b3402e; --good: #2e7d4f; --stub: #9a8f7e;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #1c1a17; --ink: #ece6da; --soft: #a39a8b; --line: #3a352e;
      --card: #252220; --accent: #e07a62; --good: #6cc08e; --stub: #8a8172;
    }
  }
  :root[data-theme="dark"] {
    --paper: #1c1a17; --ink: #ece6da; --soft: #a39a8b; --line: #3a352e;
    --card: #252220; --accent: #e07a62; --good: #6cc08e; --stub: #8a8172;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--paper); color: var(--ink);
    font: 19px/1.6 "Iowan Old Style", "Palatino Linotype", Georgia, serif; }
  main { max-width: 560px; margin: 0 auto; padding: 32px 16px 64px; }
  header { display: flex; justify-content: space-between; align-items: baseline;
    font: 14px/1.4 system-ui, sans-serif; color: var(--soft); margin-bottom: 24px; }
  header a { color: var(--soft); }
  .page { background: var(--card); border: 1px solid var(--line); border-radius: 6px;
    padding: 28px 24px 20px; min-height: 320px; display: flex; flex-direction: column; }
  .num { font: 600 13px/1 system-ui, sans-serif; letter-spacing: .08em; color: var(--soft);
    text-align: center; margin-top: auto; padding-top: 24px; }
  h1 { font-size: 20px; letter-spacing: .06em; text-align: center; margin: 0 0 20px; }
  h2 { font-size: 16px; font-style: italic; font-weight: normal; margin: 20px 0 4px; color: var(--soft); }
  p { margin: 0 0 16px; }
  .end { font-weight: 700; letter-spacing: .08em; margin-top: 8px; }
  .end.bad { color: var(--accent); } .end.good { color: var(--good); }
  .cardline { font-style: italic; color: var(--soft); }
  .stub { color: var(--stub); font-style: italic; }
  .suggestion { color: var(--stub); font: 13px/1.4 system-ui, sans-serif; border-left: 2px dashed var(--line); padding-left: 10px; }
  .choices { display: grid; gap: 10px; margin-top: 8px; }
  .choices button { font: inherit; font-size: 17px; text-align: left; cursor: pointer;
    background: transparent; color: var(--ink); border: 1px solid var(--line);
    border-radius: 6px; padding: 10px 14px; }
  .choices button:hover, .choices button:focus-visible { border-color: var(--ink); outline: none; }
  .choices small { display: block; font: 13px/1.4 system-ui, sans-serif; color: var(--soft); }
  .again { margin-top: 16px; font: 14px system-ui, sans-serif; }
  .again a { color: var(--soft); }
</style></head><body>
<main>
  <header><span>{{TITLE}}</span><a href="#1">Back to the start</a></header>
  <article class="page" id="page" aria-live="polite"></article>
</main>
<script>
const PAGES = {{DATA}};
const el = document.getElementById("page");
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

function show(n) {
  const p = PAGES[n] || PAGES[1];
  n = PAGES[n] ? n : 1;
  let h = p.title ? `<h1>${esc(p.title)}</h1>` : "";
  if (p.stub) h += `<p class="stub">This page isn't written yet. (${esc(p.id)})</p>`
    + (p.note ? `<p class="stub">Note: ${esc(p.note)}</p>` : "")
    + (p.suggestion ? `<p class="suggestion">Suggestion (not the author's): ${esc(p.suggestion)}</p>` : "");
  for (const [head, lines] of p.blocks) {
    if (head) h += `<h2>${esc(head)}</h2>`;
    h += `<p>${lines.map(esc).join("<br>")}</p>`;
  }
  if (p.type === "ending") {
    h += `<p class="end ${p.mood === "good" ? "good" : "bad"}">THE END.</p>`;
    if (p.card) h += `<p class="cardline">${esc(p.card)}</p>`;
    h += `<p class="again"><a href="#1">Start again</a></p>`;
  } else if (p.choices.length) {
    h += `<div class="choices">` + p.choices.map(c => c.to
      ? `<button data-to="${c.to}">${esc(c.text)}<small>Turn to page ${c.to}</small></button>`
      : `<button disabled>${esc(c.text)}<small>Page missing</small></button>`).join("") + `</div>`;
  }
  h += `<div class="num">${n}</div>`;
  el.innerHTML = h;
  window.scrollTo(0, 0);
}
el.addEventListener("click", e => {
  const b = e.target.closest("button[data-to]");
  if (b) location.hash = b.dataset.to;
});
const BY_ID = Object.fromEntries(Object.entries(PAGES).map(([n, p]) => [p.id, +n]));
const target = () => {
  const h = decodeURIComponent(location.hash.slice(1));
  return /^[0-9]+$/.test(h) ? +h : BY_ID[h] || 1;
};
addEventListener("hashchange", () => show(target()));
show(target());
</script>
</body></html>
"""


if __name__ == "__main__":
    main()
