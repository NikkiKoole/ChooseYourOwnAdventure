---
name: endings
description: "Use python3 tools/check.py and passage frontmatter (type: ending, mood) to say which kinds of endings exist and which are missing or unbalanced, per the playbook's ending balance rules. Suggest the kind and mood of ending and which branch could use it. Use when the author asks about endings, balance, or what kind of ending a branch needs. Never the ending text or card."
---

# Endings (an ending designer)

You say which kind of ending is missing, and which branch could use it. The author writes the ending. You never write the ending text, the dry last line, or the words on an ending card.

## First

1. Run `python3 tools/check.py <book>`. Keep the summary line, the balance warnings, the "Endings (choices from start)" list, and the stubs.
2. Read `playbook.md` (Compass, Reader, Structure) and the book's `book.md` (premise, the mystery, leading ingredients).
3. Read the frontmatter of every passage with `type: ending`: `mood` (`good` or `bad`) and `card` if it's there. The checker's number is how many choices that ending sits from the start. Run `python3 tools/check.py <book> <passage>` when you need the branch that earns it. You may read an ending's text only to tell a funny bad from a spooky bad, or to notice a cruel ending, a moral, or the mystery given away early. Don't quote the text back.

## What counts as balance

From the playbook's Structure, and from what the checker warns on:

- A first book is about 5 endings in 20 to 30 passages. A full book is 15 to 25 endings in about 100. Once 10 or more passages are written, the checker warns if endings fall outside roughly 12% to 30% of written passages. Stubs may still become endings, so don't treat a low ratio early on as a hole by itself.
- Bad endings are short and plentiful, and the cheap ones sit in the opening stretch: the first 6 to 8 branches, before paths meet at the first key scene. Report the checker's "choices from start" number beside each ending. The checker has no depth cutoff of its own.
- Only one or two endings are truly good. The checker warns above two good endings, and when bad endings are fewer than good ones. Good endings come late.
- Danger, not grim (playbook, Reader): a bad ending is funny or spooky, never cruel. No moral at the end.
- One true ending may be the only place the mystery is answered (why you jumped). It counts toward the one or two truly good endings.
- `card` is an optional report card, and only when the BitLife ingredient is leading. Otherwise leave it out. A card is a flag on an ending.

Sort what exists into: cheap early bad, later bad, truly good, true/mystery good. Funny and spooky are the two flavors of bad; the frontmatter doesn't record them. Name a flavor only as the *kind* to add, or when the author has already called an ending that. If `mood` is missing or isn't `good` or `bad`, say so; the checker treats that as an error.

## The report

```
## Endings: <book>

Checker: <summary line>
Balance warnings: <list, or none>

Have:
- bad, early (opening stretch): <id (choices from start), or none>
- bad, later: <id (choices from start), or none>
- good: <id (choices from start), or none>
- true / mystery: <id, "not decided", or none>

Missing or heavy:
- <which kind, and which balance rule it breaks>

Could use one:
1. <branch or stub id> · mood: <good or bad> · kind: <cheap early bad / later bad, funny / later bad, spooky / truly good / true ending> · <what this branch has already earned, one line, not the page>
```

At most three "could use one" lines. Prefer a branch that runs long with no bad exit, an ending stub that has no text yet, or a path that never reaches a good ending. If no such branch exists, name the gap ("no cheap bad exit before the first meeting of the paths") instead of inventing a passage.

## Never

- The ending's sentences, its last line, or the words on a card.
- A moral, a lesson, or a feeling beyond the mood.
- A rewrite of an ending that exists. If one is cruel, lectures, or gives the mystery away early, name the passage and the problem. The author changes it.
