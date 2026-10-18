# Choose Your Own Adventure Playbook

Oct 18, 2026

## Compass

Teach, don't preach. Humor lets the book be razor-sharp without being boring or pretentious.

- The reader makes the choice and lives the consequence. The lesson is felt, never told.
- No morals at the end. The ending card is the joke; the reader draws the conclusion.
- Anyone who lectures is the punchline.
- Aim satire up: greedy grown-ups, silly rules, pompous people. Never the reader.
- If a page feels like a lesson, it needs a joke or a cut.

## Reader

Kids aged 9 to 12, with a second layer adults enjoy. Read alone or together.

- **Two layers.** Kids read what happens; adults read what's underneath. The top layer must work on its own.
- **Danger, not grim.** Peril yes, gore no. Bad endings are funny or spooky, never cruel.
- **Ageless "you".** Never state the reader's age.
- **Reading together.** Write for the ear. Make choices worth arguing about. Give characters lines a parent can perform.
- **Reading alone.** Never need an adult to explain. Clear page numbers and a way back to the start.
- **Pure story, no homework.** No mazes, sudokus or puzzles.

## Pen name

**M. Pompelmino.** The author name on every cover, in every language. Shared across all books.

- **The M.** never gets explained on the cover. In English it reads as a stuffy initial, in French as *Monsieur*, and in Dutch as a mystery.
- **Lifting the curtain.** A running gag across the books: now and then a book lifts the curtain a little on what the M stands for. Rarely, deadpan, never the whole show at once. Every weird thing pays off, and this one pays off across books.
- **Never the same story twice.** M. Pompelmino is too pompous to keep his story straight: every reveal contradicts the last one, said with total confidence. The shape of Aphex Twin's interviews, each myth grander than the one before. Shapes, not references: never name him in the books. Log each reveal below so every contradiction is deliberate and none repeats.
  - Reveals so far: none.
- **Full name**, revealed in the book (if anywhere): Dutch **Meneertje Pompelmino**, Italian **Signorino Pompelmino**. "Little Mister Little Grapefruit": small twice over, in the title and in the name, and pompous all the same. Anyone who's pompous is the punchline, the author included.
- **Pompelmino** is his family name, so it never gets translated; only the title does.
- **Roots:** born from a try at typing "pompous" (Pompel), and a nod to *Meneer Pompelmoes*, a Dutch children's book from the early 1960s. *Pompelmoes* (Dutch) and *pompelmo* (Italian) both mean grapefruit.
- **Watch:** *pompelmo* is also the flavour on the Sanpellegrino can. A smile for adults who know it, never a brand nod.
- **Open:** name on the cover only, or the narrator's voice?

## Style

Short, fast pages. Longer text only where it's earned.

Joep's forms (five-liner, Joepie, the "I – verb – the rest" opening, the invitation) are guidelines and inspiration, not hard rules. Bend them when the page needs it.

- **Normal pages: Joep's five-liner.** Punchy first line, every line moves forward, the last line is the choice or a twist, ideally phrased as an invitation ("Wil jij de reserve trekken?"). Use visible words.
- **Key scenes: a Joepie.** A title, three blocks of five lines with headings, then the choice.
- **Iceberg (Hemingway).** One strong detail instead of explaining. Leave things unsaid.
- **Deadpan.** Calm voice, wild events. Every ending closes with one dry line.
- **Rhythm.** Mostly fast, with occasional quiet beats so the action hits harder.
- **Start in motion.** The situation itself creates the pressure, like the parachute.

## Structure

Start small: 20 to 30 passages, about 5 endings. A full book is around 100 passages with 15 to 25 endings.

- **Branch and bottleneck.** Paths split, then meet again at key scenes.
- **Cheap early endings.** Bad endings are short and plentiful; only one or two are truly good.
- **Character pick.** Each character has skills that open different options or routes.
- **Mystery ending.** Why you jumped may only be revealed on the one true ending.

Skeleton for a first book of about 25 passages:

1. Opening + character choice
2. 6 to 8 early branches, with 1 or 2 quick bad endings
3. Key scene where paths meet (a Joepie)
4. 8 to 10 second-half branches
5. Final key scene
6. 4 or 5 endings, only 1 or 2 truly good

## The pile

A palette, not a recipe. Expect two or three ingredients to lead and the rest to flavor now and then.

The ingredients live in `pile.md`. Rejected sparks go to `tank.md`.

## Rules for sparks

No random manatee balls: every spark must serve the story, or it goes back in the tank.

- **Story first.** Know what the passage needs before drawing. The spark answers how, never what.
- **Removal test.** If cutting it changes nothing, cut it.
- **Shapes, not references.** Tropes are structures; name-drops are winks.
- **Everything weird pays off.** A strange symbol returns or connects somewhere.
- **One spark per passage.**
- **Surprise, not randomness.** Surprising in the moment, obvious in hindsight. Big jumps need a premise that allows them.
- **Keep a tank file** of rejected sparks for later.

## Process

You bring ideas, voice and the final say. Claude helps with sparks, structure, mapping and getting unstuck.

1. **Gather** ideas freely.
2. **Filter** to the few ingredients that define the book.
3. **Premise:** the core situation and goal.
4. **Map** the branches, key scenes and endings.
5. **Write the bad endings first.**
6. **Write the passages:** five-liners, Joepies, iceberg. Write with your Ernie: fast, no judging.
7. **Read aloud.** If it stumbles, rewrite.
8. **Trim** anything the choices don't need. This is Bert's job.

When stuck: Joep's warm-up (see Glossary), ask "what's the worst thing that could happen now?", or draw a spark.

## Tools

Passages live as files, and Claude Code skills act as lenses. Most skills are critics, not writers: you write with your Ernie, the skills play Bert.

**Passage files.** One markdown file per passage in `books/<book>/passages/`, named after its id. Ids are short names, not numbers: page numbers are assigned when the book is built, so passages can be added, cut or moved without renumbering. Every fact lives in one place:

- Choices live only in the frontmatter, as a short label and the id they lead to.
- The text ends with the invitation, without page numbers. The build adds "Turn to page N".
- Endings don't type "THE END."; the build adds it. The last line is the dry closer.
- Line counts cover the text only, not the generated choice line.

A page:

```markdown
---
id: parachute
type: page
start: true
character: any
choices:
  - text: Pull the reserve
    to: reserve
  - text: Steer for the lake
    to: lake-roof
---
The parachute doesn't open.
You pull the cord again. Nothing.
The ground is rushing up, green and brown.
On your chest: a reserve chute, old and patched with duct tape.
Pull the reserve? Steer for the shining lake below?
```

An ending (`mood` is `good` or `bad`; `card` is an optional report card, only if the BitLife ingredient leads):

```markdown
---
id: lake-roof
type: ending
mood: bad
---
The lake is not a lake.
It's a greenhouse roof, glittering in the sun.
You crash through the glass into a jungle of tomatoes.
A gardener stares at you, hose in hand.
"You're paying for that," she says.
```

A Joepie: `type: joepie`, a `title`, then three blocks each under a `## Heading`, then the invitation line.

Optional fields: `start: true` on the one opening passage, `character` (default `any`), `spark` (the pile ingredient or tarot card used, so Map can track what's been missing), `note` (an idea for a page that isn't written yet; shown by the checker and in the clickable book).

`tools/check.py <book>` checks broken links, orphan pages, dead ends, line counts and ending balance, and draws the branch map. `tools/build.py <book>` makes the clickable version. Later: character paths and the printed book.

**Skills** (in `.claude/skills/`). Four critics and one unstuck button; none of them writes the page.

| Skill | What it does |
| --- | --- |
| Five-liner | Joep's method on a page: visible words, short opening, precise noun, vivid verb, adjectives like salt, the invitation |
| Iceberg | What to cut (explaining, preaching, broken deadpan) and whether anything is under the water |
| Reader | The kid alone, the parent along, and the read-aloud ear |
| Map | Runs the checker, then reads the structure: bottlenecks, cheap endings, payoffs of weird things, character paths |
| Spark | Unstuck: one or two pile ingredients plus a question, tarot cards you drew turned into prompts, Joep's warm-up, Hemingway's one true sentence, or "what's the worst that could happen?" Inspired by Brian Eno and Peter Schmidt's Oblique Strategies |

Tarot, inside Spark: you draw the cards by hand. One card per passage, three for a scene (situation, obstacle, outcome), or one per choice. Suits as flavors: Wands action, Cups feelings, Swords conflict, Pentacles money. Reversed means a twist.

## Glossary

The terms and references this playbook relies on, for anyone reading it fresh.

| Term | Meaning |
| --- | --- |
| Joep Luycx | Dutch writer and writing trainer, founder of De Joepie Academie (2015) and the author's former teacher. Wrote *Schrijf wat je bedoelt* (2013). Source of the five-liner, Joepie and Ernie/Bert methods. Full method in his book *Doe als ik, schrijf als jij* (a local copy, not in the repo: it's copyrighted). He asks to be credited when his ideas are used |
| Michael Silverstein | American linguist and anthropologist (1945–2020). Joep bases visible words on his animacy hierarchy, flattened to two kinds of words: words you can see and contourless ones (Joep credits Silverstein with the word "contourless") |
| Five-liner (vijflijner) | A single block of five lines. Joep's basic unit, and the rule for every normal page here |
| Joepie | Title + three blocks of five lines, each with a heading. Built from associations and visible words: write four paragraphs, pick three, try different orders, add headings as bridges, a why-title with an absurd adjective, and a last line that is an invitation ("Wil jij…?") |
| Exploding first sentence | Joep's idea of an opening line that works like a little bomb, popping the cork so the rest flows |
| Joep's warm-up | Pick a letter, write three words, choose the most appealing, add five associations, pick the clearest picture, write an "I – verb – the rest" sentence, make it as short as possible, then write on to five sentences |
| Iceberg theory | Hemingway's principle (*Death in the Afternoon*, 1932, chapter 16): show only the tip; if the writer knows what's underneath, the reader feels it without being told. Leaving out what you don't know only makes "hollow places" |
| Manatee balls | From South Park's "Cartoon Wars", which joked that Family Guy's gags are random idea balls combined by manatees. Our term for a spark with no connection to the story |
| Oblique Strategies | Brian Eno and Peter Schmidt's 1975 card deck of cryptic prompts for breaking creative blocks. Model for the spark skill |
| Branch and bottleneck | A gamebook structure where paths split and then rejoin at key scenes |
| Double layer | A surface story kids follow fully, plus subtext adults catch. The top layer never depends on the bottom one |
| Shapes, not references | Use a trope's structure (the red wire choice) rather than naming the movie it comes from |

More from Joep's method:

- **Ernie and Bert.** From Kahneman's two systems. Ernie is fast and free: he writes. Bert is slow and critical, the "yes, but" voice: he improves. Never let Bert in while Ernie writes.
- **Visible words.** Concrete words with a clear outline (cow, lollipop, bounce) beat contourless ones (concept, optimize).
- **Bert's three edits.** A more precise noun, a more vivid verb (walk → bounce), and one adjective. Adjectives are like salt.
- **Coherence is order.** Reorder paragraphs and read them aloud to find the story.
- **Everything you write is good.** First drafts are Ernie's playground.
- **A clear boundary, like a football field.** Inside it, anything goes. The speeltuin.

Tried and rejected: the Hemmingway-1 writing model (didn't suit this work) and puzzle extras like mazes and sudokus (they kill momentum).

## Examples

Passages that set the tone. Match their length, voice and deadpan. One sentence per line. Shown as printed: in passage files, "Turn to page" and "THE END." are added by the build. As passage files they live in `examples/`.

**A normal page.** Starts mid-action; the situation creates the pressure.

> The parachute doesn't open.  
> You pull the cord again. Nothing.  
> The ground is rushing up, green and brown.  
> On your chest: a reserve chute, old and patched with duct tape.  
> Pull the reserve? Turn to page 2. Steer for the shining lake below? Turn to page 3.

**A good ending.** Relief, then a dry last line.

> The duct tape holds. Barely.  
> The reserve snaps open with a crack like a gunshot.  
> You drift down, swinging, laughing like an idiot.  
> You land in a cow field. A cow stares at you, unimpressed.  
> THE END. You live. The cow does not care.

**A bad ending.** Surprising in the moment, obvious in hindsight: you chose the lake, and the lake was a roof.

> The lake is not a lake.  
> It's a greenhouse roof, glittering in the sun.  
> You crash through the glass into a jungle of tomatoes.  
> A gardener stares at you, hose in hand.  
> THE END. "You're paying for that," she says.

**A key scene (Joepie).** Kids see a villain; adults see a man who stopped asking questions for money.

> **THE KEEPER'S SECRET**
>
> *The coat*  
> She's wearing his coat. It drags on the floor.  
> "He's my grandfather," she says. "He's the keeper."  
> She won't look at you. She looks at the cut fuel line.  
> Someone used a knife. One clean stroke.  
> You know before she says it.
>
> *The deal*  
> "Men come in boats after a wreck. They pay him."  
> "How much?"  
> "Enough that he stopped asking who's on board."  
> She pulls the coat tighter. It smells of tobacco and salt.  
> "Tonight there are children on that ship."
>
> *The light*  
> Above you, the lamp flickers.  
> Five minutes of battery. Maybe less.  
> She looks at your toolkit, then at you.  
> "Can you fix it?"  
> Through the window, a light moves in the KEEPER room.
>
> Fix the fuel line? Turn to page 41. Go after him? Turn to page 42.

**A character skill in action.** The Mechanic hears what others wouldn't: "The grinding is coming from a gearbox under the lamp. One tooth is slipping. You give it ten minutes, maybe less."

## Books

This playbook holds the rules for every book. Each book lives in `books/<book>/` with its own `book.md` (premise, characters, leading ingredients, money, recurring symbols, open decisions) and `passages/`. The pile, the tank, the examples and the skills are shared.
