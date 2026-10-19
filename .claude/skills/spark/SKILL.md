---
name: spark
description: Help the author get unstuck with a spark, a prompt rather than a page. Draws one or two ingredients from pile.md (random or targeted), translates hand-drawn tarot cards into prompts, guides Joep Luycx's warm-up or Hemingway's one true sentence, or asks "what's the worst thing that could happen now?". Use when the author is stuck, asks for a spark, a card reading, or the warm-up. This skill does not draft; a DRAFT, if wanted, is Pitch or Interview.
---

# Spark (an unstuck skill)

Inspired by Brian Eno and Peter Schmidt's *Oblique Strategies*. The warm-up is **Joep Luycx**'s (*Doe als ik, schrijf als jij*, De Joepie Academie): credit him whenever you use it.

You give a prompt, not a page. No sample lines, no "for example, you could write…". The spark answers *how*, never *what*. This skill does not draft. A DRAFT, if the author wants wording, is Pitch or Interview: labeled DRAFT, an option only, and never saved into a passage from here.

## First

Read `pile.md`, `tank.md`, the "Rules for sparks" in `playbook.md`, and the book's `book.md` (its leading ingredients and recurring symbols come first). If the author names a passage, read it and the passages that lead into it.

## Modes

Pick the mode from what the author asks. If unclear, offer the six in one line.

**1. Draw** (default)
- Random: pick with a real random draw, `python3 -c "import random; ..."` over the pile rows, so it isn't your taste choosing.
- Targeted: look at the `spark` field in the passage files to see which ingredients have been used and which haven't. Prefer one that's been missing, or the one that fits what the passage needs.
- Give one or two ingredients plus **one question** that connects them to this passage.
- Skip anything already in `tank.md` unless the author asks to fish there.

**2. Tarot**
- The author draws the cards by hand and tells you which. Never draw for them.
- One card per passage; three for a scene (situation, obstacle, outcome); or one per choice.
- Suits as flavors: Wands action, Cups feelings, Swords conflict, Pentacles money. Reversed means a twist.
- Translate each card into one story prompt in the book's world, as a question.

**3. Warm-up** (Joep's)
Guide it step by step and wait for the author's answer at each step. Don't do the steps for them.
1. Pick a letter.
2. Three words: one starting with it, one ending with it, one with it in the middle.
3. Choose the most appealing; add five associations.
4. Choose the clearest picture; write a sentence "I – verb – the rest" (or "you – verb – the rest").
5. Make it as short as possible.
6. Write on to five sentences, with Ernie. No judging.

**5. Lens** (`/spark lens <ingredient>`)
Look back over pages already written through one pile ingredient. Same rules as a spark: questions, never lines.
- Read that ingredient's row in `pile.md`; its "What to borrow" is what to look for.
- Take the pages the author names, or every written page of the book (skip stubs). Go in reading order.
- **Already there:** quote the words (a few, not whole lines) where the ingredient already shows, even if unplanned.
- **Could go:** at most one question per page where it would fit, and only on pages with no spark yet. Fewer is better: name the two or three best pages, not all of them.
- **Keep out:** say where it would clash (a page that already has a spark, a moment that needs to be quiet, a reference instead of a shape).
- Never name the source's works or characters in a question. Shapes, not references.
- End with one line: does this ingredient want to lead in this book, flavor it now and then, or stay in the pile?

**4. Worst thing**
Ask "What's the worst thing that could happen now?" Then, after their answer, at most two follow-up questions (Who's watching? What does it cost?).

**6. One true sentence** (Hemingway's, *A Moveable Feast*)
When the author is stuck on a blank page: "Write the truest sentence you know about this moment." Then wait. Don't suggest the sentence. After it, they write on with Ernie. Credit Hemingway when you use it.

## Rules to hold the spark to

- Story first: if the author hasn't said what the passage needs, ask that before drawing.
- One spark per passage.
- Removal test: if cutting it changes nothing, it goes back.
- Shapes, not references: no movie or book names in the prompt.
- Everything weird pays off: if the spark adds a strange object, ask where it returns.
- No manatee balls.

## After

- If the author keeps a spark, suggest they add `spark: <ingredient or card>` to the passage frontmatter so the Map skill can track it.
- If the author rejects one, offer to add it to `tank.md` as `- <date> · <spark> · <why not now>`. Only write it when they say yes.
- If the author is stopping for the day, pass on Hemingway's habit once: stop while you still know what happens next, so tomorrow starts easy.
