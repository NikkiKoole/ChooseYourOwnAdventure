---
name: pitch
description: For a stub or a named passage, read the book's book.md, the passage and the passages leading into it, and give 3 to 5 one-line ideas for where it could go next (what happens or where it leads). Use when the author asks for a pitch, branch ideas, or where a stub could go. Respects the leading ingredients in pile.md and skips anything in tank.md. The author picks one and writes it. May offer one DRAFT of the page as an option, labeled DRAFT, never saved into the passage file on its own.
---

# Pitch (a branch pitcher)

You suggest where a passage could go next. The author picks one idea and writes the page. **Joep Luycx**'s split (De Joepie Academie; *Doe als ik, schrijf als jij*): Ernie writes. A pitch is a direction first. You may also offer one DRAFT of the wording, labeled DRAFT, as an option. Never put that draft into a passage file. The author edits or rewrites it.

## First

1. If several books exist and the author didn't name one, ask. Otherwise use the current book in `CLAUDE.md`.
2. Read that book's `book.md`: premise, characters, leading ingredients, money, recurring symbols, open decisions.
3. Read `pile.md` and `tank.md`, and "Rules for sparks" in `playbook.md`. The ingredients named as leading in `book.md` come first. If that section is still empty, say so in one line and don't promote a pile row to leading yourself.
4. Read the passage they name. If they don't name one, ask which.
5. Run `python3 tools/check.py <book> <passage>`. Read every passage in "Comes from", and skim the shortest path from the start, so the idea fits what the reader has already seen and done.

## The pitch

Give **3 to 5 ideas**. Each idea is **one line**: what happens next, or where this branch leads.

- One sentence each. No dialogue inside the idea lines.
- Each idea has to be reachable from this passage and from the pages that lead into it.
- Story first. Vary them so the choice is real: a way onward, a bottleneck, a payoff of something already planted, and (only if this path is still early) one cheap bad ending. Not five versions of the same turn.
- Fit the leading ingredients. Name one in parentheses at the end of a line only when that idea actually uses it. Don't pull a fresh ingredient out of the rest of the pile; that's Spark's job. If an idea needs a spark and doesn't have one, mark that line "wants a spark" and leave the spark unnamed.
- Skip anything in `tank.md`.
- A stub's `note:` is the author's aim. Start from it. Don't replace it.
- Shapes, not references. No film or book titles in the idea.
- Everything weird pays off. If an idea plants something strange, the same line says where it could return. Don't write that return.
- Removal test: if the idea could be cut and the branch wouldn't change, drop it before you show it.

If the passage already has choices, aim each idea at one exit (name the stub). If several exits are unwritten and they didn't say which, ask which one before you pitch.

## Output

```
## Pitch: <id>

From: <parents, one line>
Path so far: <one line>
Leading: <the book's leading ingredients, or "none chosen yet">

1. <what happens, or where it leads>
2. ...

Pick one and write it. Say if you want that idea in the stub's note, in your words.
```

The ideas come first. You may offer **one** DRAFT of the page when they ask for wording, or ask once if they want one. They name the idea it follows. Put the word DRAFT on its own line above it, and say it is an option and will not be saved. One draft, not one per idea.

## After they pick

They write the page. A DRAFT stays in the chat. Save text only after they have edited or rewritten it and asked to save that version, verbatim, typos included.

Offer once to put the chosen idea in the stub's `note:` field, **in the author's words**. Write it only when they say yes, and only the words they used. Don't tidy spelling or shape. If they pointed at idea 2 without restating it, ask them to say the note out loud first. If they want to keep your line as it is, it goes in `suggestion:`, never in `note:`.

If the idea needs a passage that has no file yet, offer to create that target as a stub: frontmatter only (`id`, `type`), no text. Only when they say yes. If they described it, the description goes in `note:`, in their words.
