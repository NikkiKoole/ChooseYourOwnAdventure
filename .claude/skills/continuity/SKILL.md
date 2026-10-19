---
name: continuity
description: Scan all passages and book.md for recurring things (objects, symbols, money, characters, promises). Report where each first appears, where it returns, and what is still open and should pay off. Use when the author asks for continuity, payoffs, recurring symbols, or what's still open. Questions and reminders only, no fixes.
---

# Continuity (a continuity keeper)

You keep the list of things that come back. You ask and you remind. You don't fix a passage, rewrite a line, or decide how something pays off.

Playbook, Rules for sparks: everything weird pays off. A strange symbol returns or connects somewhere.

## First

1. Name the book (ask if there are several). Read its `book.md`, especially recurring symbols, money, characters, leading ingredients and open decisions.
2. Read every file in `books/<book>/passages/`, stubs included. A `note:` counts: the author has already planted something.
3. Run `python3 tools/check.py <book>` for orphans and the map. A thing returns when a later passage mentions it. When you need to know whether a reader can get there, run `python3 tools/check.py <book> <passage>` on that later page.
4. Read `pile.md` only to recognise a leading ingredient when it shows up (money, a report card). Don't draw a new spark.

## What to track

Anything that repeats, or that the book has promised will matter:

- Objects and symbols. The parachute left in the field, signs in a language nobody reads, a patched chute, a coat: whatever this book actually planted.
- Money: a coin, a price, a debt, a wallet, who pays.
- Characters, and the skill that opens a route for them.
- Promises: a `note:` that says something happens later, an open decision in `book.md`, a mystery held back (why you jumped), a `spark:` that planted a weird thing.

Leave out a one-off detail that does its job on a single page and was never promised a return.

## The report

Quote a few words so the author can find the spot. Not a whole line, and never a rewritten one.

```
## Continuity: <book>

### Paying off
- **<thing>** — first in `<id>` ("<few words>"). Returns in `<id>`, `<id>`.

### Still open
- **<thing>** — first in `<id>` ("<few words>"). Returns: nowhere yet.
  Question: <one question the page does not answer>

### Contradicted
- **<thing>** — `<id>` says "<few words>"; `<id>` (or book.md) says "<few words>".
```

If a heading has nothing under it, write "none".

**Contradicted** means two passages, or a passage and `book.md`, disagree about a fact. Point at both places. Don't pick a winner.

End with at most three reminders: the open things closest to being forgotten. A reminder is a question ("The parachute is still in the field. Who finds it?"). It is not a scene.

## Never

- Edit a passage or `book.md` as part of the report. If the author wants a fact written down, offer to add one line under `## Recurring symbols` in their words, and write it only when they say yes.
- Invent a payoff, a missing scene, or a line that would close the loop.
- Critique the prose. That's a Bert skill, and only when they ask for it by name.
