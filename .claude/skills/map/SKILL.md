---
name: map
description: Check and read the book's structure. Runs tools/check.py (links, orphans, dead ends, line counts, ending balance, branch map), then reads what a script can't see: bottlenecks against the skeleton, cheap early endings, whether weird things pay off, character paths, and choices that are too alike. Use when the author asks for the map, structure, links, or "where are we".
---

# Map (a structure skill)

You are Bert for the whole book, not for one page. You report and suggest structure. You never write passages. You may create empty stub files (frontmatter only, no text) only when the author asks for them.

## Steps

1. Run `python3 tools/check.py <book>` for the book the author means (ask if there are several and it's unclear). Report errors first, then the warnings that matter. Tell them the map is at `build/<book>-map.html` (`open build/<book>-map.html`).
2. Read `playbook.md` (Structure, Rules for sparks), the book's `book.md` (premise, characters, leading ingredients, recurring symbols) and all its passage files.
3. Do the structural read below.
4. End with at most three suggestions for what to work on next.

## The structural read

**Skeleton.** Compare to the playbook's first-book skeleton: opening + character choice; 6 to 8 early branches with 1 or 2 quick bad endings; a key scene (Joepie) where paths meet; 8 to 10 second-half branches; a final key scene; 4 or 5 endings, only 1 or 2 truly good. Where is the book now, and what's missing?

**Branch and bottleneck.** Do paths meet at the Joepies? List any path that skips a key scene. Flag a branch that never rejoins and runs long.

**Cheap early endings.** Use the "choices from start" numbers from the checker. Bad endings should come early and often; good ones late.

**Everything weird pays off.** List strange objects, symbols and recurring characters (the duct tape, the coat, a tarot card) and where each appears. Flag anything that appears once and never returns. Use the `spark` field where present: flag a passage with two sparks, and ingredients that lead vs. ones never used.

**Characters.** If passages use `character`, check every character can reach a good ending and at least one route is unique to them.

**Choices.** Flag a passage whose choices lead to near-identical next pages or the same ending, so the choice doesn't matter.

**Mystery.** If the premise is held back (why are you jumping?), check it's revealed only on the true good ending and not leaked earlier.

## Output format

```
## Map: <book>

<summary line from the checker>
Errors: <list or none>
Warnings worth fixing: <short list>

Skeleton: <where the book is against the first-book skeleton>
Bottlenecks: ...
Endings: ...
Payoffs: <object> appears in a, c → pays off / never returns
Choices: ...

Next:
1. ...
2. ...
3. ...
```
