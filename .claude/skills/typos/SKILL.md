---
name: typos
description: Fix only obvious typos in passage files (misspelled words, swapped or missing letters, words glued together, double spaces), leaving everything ambiguous, stylistic or grammatical untouched. Use when the author asks to fix typos, clean up, or spellcheck a passage, a few passages or a whole book.
---

# Typos (a cleanup skill)

Not Bert: this skill doesn't critique and doesn't improve. It only removes slips of the keyboard, so the author's words read as the author meant them.

## The one rule

**Change a word only if there is exactly one thing the author can have meant.** If you have to choose between two readings, leave it and list it.

## Fix

- Misspelled words with one clear intended word: ocming → coming, teh → the, aoiming → aiming, thininig → thinking.
- Words glued together or split: witha → with a, leavinga → leaving a.
- A stray letter stuck to a word when the word is otherwise clear: gfeel → feel, wcolors → colors.
- Double spaces inside a line.
- The same in choice `text` labels in the frontmatter.

## Never touch

- Anything with two possible readings (spchange: "speed change" or "change"?). List it instead.
- Grammar that could be voice: "you was", "speeds keeps", run-on sentences, comma splices.
- Capitals, including a lowercase "i", and punctuation. The author's rhythm and style decisions belong to Bert, later, if asked.
- Word choice, line breaks, order, frontmatter other than choice labels.
- Invented words, sound words, names, kid-speak and deliberate misspellings (if in doubt, it's deliberate).

## Steps

1. Take the files the author names: one passage, several, or a whole book (`books/<book>/passages/*.md`). Skip stubs.
2. For each file, collect the fixes and the doubtful cases.
3. Apply only the fixes, with exact string replacements. Don't rewrite whole files.
4. Report:

```
### <file>
Fixed: ocming → coming · teh → the · witha → with a
Left alone: "spchange" (speed change? change?) · "dyou you" (do you? did you?)
```

If nothing needed fixing, say so in one line. End with the total number of fixes, and list the doubtful cases in one place so the author can answer them in one go.
