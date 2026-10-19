# For any agent working in this repo

The house rules are in `CLAUDE.md` and `playbook.md`. Read both first; they apply to every agent, not just Claude. When they disagree with this file, they win.

## Taking notes for the author

The author writes; you take notes. Default: suggest, ask, map and check. Don't fix or critique unless asked.

- **As dictated.** Put a passage in exactly as the author says it, typos and all. Don't fix, polish or critique unless asked.
- **Drafts are an option.** A skill such as `pitch` or `interview` may offer wording labeled DRAFT. Never insert it into a passage file. The author edits or rewrites it.
- **One file per passage:** `books/<book>/passages/<id>.md`. The id is a short name and the file name. Format in `playbook.md` (Tools).
- **Choices go only in the frontmatter** (`choices:` with `text` and `to`). No "Turn to page" and no "THE END." in the text; the build adds them.
- **Branches without text become stubs:** frontmatter only. An idea for a page goes in a `note:` field on the stub, in the author's words.
- **`note:` is the author's, `suggestion:` is yours.** Never write your own idea into `note:`. If you have an idea, offer it; only if the author says yes, put it in a `suggestion:` field. It shows up labeled "not the author's".
- **Never store parents** (no `from:` field).
- Joep Luycx's forms (five-liner, Joepie) are guidelines. Credit him when you use or explain his method.

## Showing the author a passage

- `python3 tools/build.py <book> <id>`: that passage as plain text, as printed (page number, "Turn to page N", "THE END."). Paste it into the chat.
- `python3 tools/check.py <book>`: links, dead ends, stubs; run it after adding passages.
- The clickable book is rebuilt on every push to main and published to GitHub Pages at http://mipolai.com/ChooseYourOwnAdventure/. Each book has its own address: `http://mipolai.com/ChooseYourOwnAdventure/<book>/`, and `.../<book>/#<id>` opens at a passage (`#<page number>` works too). The branch map is at `.../<book>/map.html`. Builds take a minute or two after a push.
