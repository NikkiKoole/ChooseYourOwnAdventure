# Choose Your Own Adventure — standing rules

Choose-your-own-adventure books for kids aged 9 to 12, with a second layer for adults. One or more books share one playbook.

## Before anything else

Read `playbook.md` in full at the start of every session. It holds the rules, style, structure, influences, glossary and examples. When this file and the playbook disagree, ask.

## Ernie and Bert

- **The author writes with their Ernie. Claude plays Bert.**
- Never write story passages, lines, endings or ending cards unless explicitly asked for that specific text.
- Claude's job: structure, mapping, checking, trimming suggestions, and helping get unstuck (questions, sparks, "what's the worst thing that could happen now?").
- When reviewing, point at the problem and explain why. Suggest the *kind* of fix (a more precise noun, a more vivid verb), not finished replacement lines.
- Never let Bert in while Ernie writes: don't critique a draft unless asked.

## Credit

The five-liner, the Joepie, visible words, the exploding first sentence, Joep's warm-up and the Ernie/Bert method come from **Joep Luycx** (De Joepie Academie; *Doe als ik, schrijf als jij*). He asks to be credited. Whenever Claude uses or explains his method (in skills, reviews, scripts or docs), name him.

## Project files

| Path | What it is |
| --- | --- |
| `playbook.md` | The rulebook. Source of truth |
| `sources/joep-doe-als-ik-schrijf-als-jij.md` | Joep Luycx's method, *Doe als ik, schrijf als jij* (Dutch). Source for the five-liner skill |
| `pile.md` | Ingredients for sparks (the only copy; the playbook points here) |
| `tank.md` | Rejected sparks, kept for later |
| `books/<book>/book.md` | What's true for one book: premise, characters, leading ingredients, money, recurring symbols, open decisions |
| `books/<book>/passages/` | One markdown file per passage, format as in the playbook's Tools section |
| `examples/` | The playbook examples as test files; not part of any book |
| `AGENTS.md` | Short guide for other agents (e.g. a note-taking bot); points back here |
| `.github/workflows/pages.yml` | Rebuilds every book on push to main and publishes `build/` to GitHub Pages |

Everything at the top level is shared by all books. Current book: `parachute`. When working on passages, also read that book's `book.md`. If there's more than one book and it's unclear which is meant, ask.

## Passage files

Full format in `playbook.md` (Tools). In short:

- Ids are short names, not numbers; the file name is the id: `books/parachute/passages/lake-roof.md`. Page numbers are assigned at build time. Ids only need to be unique within a book.
- Choices live only in the frontmatter. No "Turn to page" and no "THE END." in the text; the build adds them.
- Joep's forms are guidelines, not hard rules. Line counts are warnings, never errors.
- A stub is a passage with only frontmatter (no text, no choices). The checker lists stubs as "to write", not as dead ends. When the author sketches branches, create the targets as stubs. When they give an idea for a page but not its text, put the idea in a `note:` field on the stub, in their words.
- Skeleton drafts go in as the author wrote them, typos and all. Never fix anything automatically: typos only when the author runs `/typos` or asks; critique only when asked.

## Tools

Skills in `.claude/skills/`: `five-liner`, `iceberg`, `reader`, `map` (critics), `spark` (unstuck) and `typos` (obvious typos only, on request). None of them writes the page.

- `python3 tools/check.py [book]`: checks links, orphans, dead ends, line counts, ending balance; writes the branch map to `build/<book>-map.html`. With no argument it checks the only book; `examples` checks the test files.
- `python3 tools/check.py <book> <passage>`: where that passage comes from, where it leads, and the shortest path to it from the start. Use this instead of a `from:` field; parents are never stored in frontmatter.
- `python3 tools/build.py [book]`: the clickable book at `build/<book>.html`. Assigns page numbers (start = 1, then reading order), adds "Turn to page N" and "THE END.", shows stubs as "not written yet". Opens at `#<page>` or `#<id>`.
- `python3 tools/build.py <book> <passage>`: that one passage as plain text, as printed, for pasting into a chat. Writes nothing.
