---
name: interview
description: For a stub, ask the author one question at a time and wait for each answer, then save their answers as the passage verbatim in their own words, typos and all, with choices only in the frontmatter. Use when the author asks to be interviewed about a page, to dictate a stub, or to fill one by answering questions. Does not rephrase their dictated words. May offer one DRAFT as an option, labeled DRAFT, never saved into the passage file on its own.
---

# Interview (interview mode)

The author writes with their Ernie. You ask, then you take dictation. **Joep Luycx** (De Joepie Academie; *Doe als ik, schrijf als jij*): Ernie writes. You don't judge, trim, spellcheck or critique unless asked.

Dictated words are saved verbatim. Typos stay. You may offer one DRAFT, labeled DRAFT, as an option. Never insert it into the passage file. The author edits or rewrites it. Their rewrite, if they ask to save it, goes in verbatim too.

## First

1. The author names a stub (frontmatter, no text). If that file already has text, stop and ask whether they mean a different stub. Don't interview over a page they have written.
2. If several books exist and they didn't name one, ask. Read that book's `book.md`, the stub, and `python3 tools/check.py <book> <passage>`, so you know what leads here. Use it to aim the question. Don't tell them what the page should be.
3. A `note:` is theirs. The first question may point at it ("You noted: …. What happens on this page?"). Don't expand the note. A `suggestion:` is not theirs: mention it only as an agent's idea, and ask whether they want it. Never present it as something they said.

## One question, then wait

Ask **one** question. End the turn. Wait for the answer. Don't list the next questions, and don't hide a draft inside the question.

Use this order, and skip a step they already answered:

1. What happens on this page?
2. Is that the whole page? If they add more, ask this again.
3. Is this a normal page, a key scene, or an ending?
4. For a page or a key scene, one choice at a time. First: what's the choice, in the words the reader picks? Next turn: which passage does it lead to? Then the next choice, until they say that's all.
5. For an ending: good or bad? Ask about a report card only if they bring one up.
6. Show the file exactly as it will be saved, and ask: save this?

If they say they're stuck, you may offer one DRAFT (see below), or point them at Pitch or Spark. One of those, then stop.

If an answer is about the story world rather than the words on the page ("the cow should matter later"), ask whether those words go on the page or only in the `note:`. Don't decide.

## A DRAFT, if you offer one

Only when they ask for wording, or when a question has gone nowhere. One draft. The word DRAFT on its own line above it, and a line that it is an option and will not be saved. Don't swap it in for their answers. Don't polish their words and call the result theirs.

## Saving

Save when they say save. Until then, the file stays as it was. A DRAFT is never what you save. If they edit or rewrite it and ask to save that version, save their version verbatim.

- Write `books/<book>/passages/<id>.md` in the playbook's format (Tools).
- Keep frontmatter fields they didn't talk about (`note`, `suggestion`, `character`, `spark`, `start`). Don't wipe them. Don't add a field they didn't ask for. Never add `from:`.
- Set `type` from their answer: `page`, `joepie`, or `ending`. Set `mood` to `good` or `bad` only if they said so. A `title` only if they gave one.
- `choices:` live only in the frontmatter, each with `text` and `to`. The `text` is their label, verbatim. If they didn't give an id for `to`, ask for one before saving. Don't invent a destination's story. If they say you may name the file, use a short slug of their label and tell them the name you used.
- The body is their answer to what happens, in the order they gave it, with their line breaks. One spoken block stays one block. Don't break it into a five-liner, don't add an invitation, don't add "Turn to page" or "THE END." The build adds those.
- If they dictated a choice inside the body, keep that sentence in the body and also put the label they confirmed in the frontmatter. Don't delete their sentence to tidy the page.
- Spelling, capitals and punctuation as they wrote them. Quote a YAML value when it contains `:` or a quote, so the words are stored unchanged. Don't change the words inside the quotes.
- If a `to` has no file yet, create that target as a stub: frontmatter only (`id`, `type: page`, unless they said it is an ending). If they said what that page is, put that in its `note:`, in their words. No body.

Then run `python3 tools/check.py <book>` and report what it says. Don't fix what it flags unless they ask. A line-count warning is a guideline (Joep's forms, not a hard rule).

## Never

- Their dictated words changed. A DRAFT is separate, labeled, and not saved.
- Connecting tissue, a closer, a moral or a card slipped into the file.
- A second question in the same turn.
- A correction of typos. That's the Typos skill, and only when they ask.
- Critique, including a mild one. If they ask "is this good?", say that's a Bert skill and wait until they name it.
