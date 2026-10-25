# uiux

**One command. It asks you what you want. Then it builds, checks, and fixes your page until the page is good.**

uiux is a skill for [Claude Code](https://claude.com/claude-code). You type `/uiux` and a page path. The skill interviews you. It writes a brief. It builds the page if the page does not exist. Then it runs a loop: nine critics check the page, one builder fixes the page, and the loop repeats until the page meets a score. You do not have to watch it.

```
/uiux src/app/page.tsx
/uiux site/src/pages/index.astro --bar 9
/uiux https://localhost:3000/pricing --skip-interview --only 05-aesthetic,07-motion
```

## The problem, in simple words

When you ask an AI for a page, the AI gives you the average page on the internet. A cream background. Three cards. A gradient. It looks finished in ninety seconds. Nobody checks if it is good.

uiux fixes this in three steps:

1. **Ask first.** The skill asks you what the page is for, who uses it, how it should feel, and what it must never look like. The answers become a written brief. Every later step must obey the brief.
2. **Pick a direction from pictures.** Before any loop, the skill builds two or three real versions of the key screen, each a different visual world. You see them side by side with screens of the best apps in the same category, and you pick one. Words like "regal" or "bold" are pinned to a picture first, so they cannot turn into decoration.
3. **Check with evidence, then fix a little at a time.** Every cycle, a script captures every state of the page (empty, long names, loading, error) and an agent clicks through your tasks in a real browser. Nine critics read that evidence and score against written examples and against screens you approved and rejected before. One builder fixes at most twelve findings, around one theme. The loop stops by itself.

## How the loop works

![The loop: interview, first build, screenshots, critics, merge, builder, score, report](docs/loop.svg)

1. **Interview.** Short rounds of questions. Each question has a recommended answer.
2. **Direction.** Two or three working versions of the key screen, side by side with the reference board. You pick one; this is the last question. The result is `docs/design/<surface>/brief.md`.
3. **First build and state harness.** The build happens only when the page does not exist yet. The harness makes every state of every screen reachable on demand: empty, one, many, long text, loading, slow, error.
4. **Evidence.** Every state at phone and desktop size. A task walker does your usability tasks in a real browser and logs steps, time, hesitations and dead ends. Typecheck, build, tests, an accessibility scan and Lighthouse run.
5. **Critics, in parallel.** All nine, every cycle. Each returns findings and a score.
6. **Merge, rank and cut.** Severity 1 (broken or against a rule), 2 (hurts the goal), 3 (polish). The builder gets at most twelve findings, around one theme. The rest carry over.
7. **One builder.** Fixes the list from the top. Only one process writes files.
8. **Score.** Bar met? Plateau? Cap? If not, go to step 4. If the look is stuck at 6 or below twice, the loop reopens the direction itself.
9. **Report.** `cycle-N.md` and `evidence/cycle-N.md` for each cycle, `final.md` at the end, five lines in chat.

The cycles run in three phases. Each phase gives the builder a different focus:

| phase | cycles (of 6) | leads | what it fixes |
|---|---|---|---|
| A structure | 1–2 | functionality, aesthetic, references | the flow works, the hierarchy serves the one job, the direction holds |
| B feel | 3–4 | visualize, motion, delight | numbers become visuals, motion explains, the signature move lands |
| C craft | 5–6 | micro-craft, design system, best practices | radii, shadows, alignment, consistency, the last accessibility gaps |

## The critics

![The nine critics and the three phases](docs/critics.svg)

| id | what it checks | leads in |
|---|---|---|
| 01 best practices | semantics, contrast, keyboard, phone layout, speed, loading and error states | C craft |
| 02 references | the mechanics of your reference products, never their look; receipts for every claim; the conversion patterns that fit the job | A structure |
| 03 design system | tokens and consistency; where a tooltip is needed and where one is too many; labels that say what happens | C craft |
| 04 functionality | every feature works; the task walker's log has no dead ends; every state holds; nothing was lost in a redesign | A structure |
| 05 aesthetic | your three brand words; the logo test; where the eye lands first; no default AI tropes; next to your approved screens | A structure |
| 06 visualize | numbers and text that should be visuals; visuals that must earn their place; no invented data | B feel |
| 07 motion | A: entrance and data motion. B: hover, press, focus and state feedback, safe on touch | B feel |
| 08 delight + ideas | the signature move, voice, craft; plus an ideas list that the builder never builds on its own | B feel |
| 09 micro-craft | radii, shadow tint, icon weight, optical alignment, light direction, motion physics | C craft (runs only then) |

All nine critics run every cycle. Outside their phase they still score and report, so nothing waits until the last cycle. Each rubric has four written examples: what a 4, a 7, an 8 and a 9 look like. 8 is the bar, and it needs evidence: a screenshot, a step in the walk log, a check result. A score with no quoted example is rejected, and that critic runs again. From the second cycle, each critic first compares the new screenshots with the old ones, blind, and says "better", "same" or "worse".

## Where the taste comes from

A brief tells the critics what the page is for. It does not tell them what good looks like. The `taste/` folder does. The critics for aesthetic, visuals, motion, delight and micro-craft, and the builder, load it before they look at the page. In this order:

0. **Your calibration board**: real screens you approved and rejected, with your words ("tacky", "that's it"). The taste critics, the builder and every judge look at these pictures first. A page that repeats the failure named on a rejected screen cannot score above 5. The board fills itself: your direction picks and your reactions to previews go on it. See [taste/calibration.md](taste/calibration.md).
1. **The project's `taste.md`** in the project root: overrides for this one project. Copy [examples/taste.md](examples/taste.md) to start.
2. **Your own taste file**, at `~/.claude/uiux/taste.md`, private, used in every project you run the skill in. The skill builds it for you: `/uiux taste init` imports what Claude already knows about your picks and then shows you ten visual pairs to choose from. After that, every run appends your reactions to previews, in your words, with the date and the project. Lines you repeat become standing rules that the critics quote. See [taste/owner-taste.md](taste/owner-taste.md) and [examples/owner-taste.md](examples/owner-taste.md).
3. **[taste/references.md](taste/references.md)**: products and pages whose craft has held up, by mode, each with one line on why. Linear, Stripe, Toss, Vercel, Family, Raycast, Apple, and the galleries. A bar, never a layout to copy.
4. **[taste/slop.md](taste/slop.md)**: the tells of AI-default design. Each one on the page without a reason in the brief is a finding. Three on one screen cap the aesthetic score at 5.
5. **[taste/defaults.md](taste/defaults.md)**: known-good type, spacing, colour, shadow and motion choices for when the brief is silent.
6. **Installed taste skills**, when present: impeccable's craft floor, design-taste-frontend, high-end-visual-design.
7. **Appshots**, when connected: real screens of the same kind of page, to calibrate density and hierarchy. Mechanics only.

The aesthetic critic must name the reference and the calibration screen the page comes closest to, and the gap. "Closest to nothing" is a finding on its own.

## When the loop stops

![Stop rules: bar, plateau, cap, your call](docs/stop-rules.svg)

After the interview the loop never asks you anything. It makes the calls itself, logs them, and lists them in `final.md` for you to review. It never invents facts or prices (they stay as visible placeholders) and never rewrites copy you locked (it lists proposed rewrites instead).

## Set up

You need Claude Code, Python 3.10 or newer, and FFmpeg for one optional tool.

### Step 1. Install the skill

Clone the repository into your Claude Code skills folder:

```bash
git clone https://github.com/notsatoshii/uiux ~/.claude/skills/uiux
```

Or clone it anywhere and make a symlink to it in `~/.claude/skills/`. Claude Code reads the `SKILL.md` and registers `/uiux`. Start a new session to see it. Reference: [Claude Code skills](https://code.claude.com/docs/en/skills).

### Step 2. Install Pillow

The scripts in `tools/` measure images. They need Pillow only.

```bash
pip install pillow
```

Reference: [Pillow](https://python-pillow.org).

### Step 3. Install FFmpeg (optional)

`tools/frames.py` reads timing from a screen recording. It needs FFmpeg on your PATH. Skip this step if you do not use video references.

Reference: [FFmpeg](https://ffmpeg.org/download.html).

### Step 4. Write your house rules (recommended)

Copy [examples/uiux.md](examples/uiux.md) to the root of your project as `uiux.md`. Edit it. The loop obeys this file above its own rules. Put in it:

- the language and register of your copy, and whether copy may change
- feature parity rules for redesigns
- words that are forbidden
- the default score bar and the cycle cap
- a token budget

The loop also reads your project's `CLAUDE.md`.

### Step 5. Connect the optional services

These add evidence and assets. The loop works without them and says so in its reports.

| Service | What it adds | How to connect |
|---|---|---|
| [Appshots](https://appshots.design) | Real iOS, Android and web screens and flows; the interview searches it and suggests reference apps to confirm, critics 02/05/06 check against them | No official connector. Community MCP `itsOwen/appshots.design-mcp` with your own login: see `integrations/appshots.md`. |
| [motion-anything](https://github.com/nexu-io/motion-anything) | ~400 motion recipes and `MOTION-SPEC.md`, the motion standard the motion critic uses | `git clone https://github.com/nexu-io/motion-anything.git`. No install, Node 18+. Link `skills/motion-anything` and `skills/gsap` into `~/.claude/skills/`. See [integrations/motion-anything.md](integrations/motion-anything.md). |
| A browser tool | Screenshots per viewport and state | The Claude desktop app browser pane, a Playwright MCP, or the `playwright-cli` skill. Without one, the critics read code only. |

### Step 6. Run it

```bash
/uiux src/app/page.tsx
```

Answer the questions. Approve the definition of done. Then wait. The loop writes to `docs/design/<surface>/` and tells you when it stops.

## Flags

| flag | meaning | default |
|---|---|---|
| `--bar N` | the score every critic must reach | 8 |
| `--cycles N` | the hard cap on cycles | 6 |
| `--skip-interview` | use the existing brief, do not ask "anything changed?" | off |
| `--only a,b` | run only these critics | all |
| `--dry` | interview and brief only, no build | off |

## Tools in the box

| script | who uses it | what it gives |
|---|---|---|
| `tools/extract-tokens.py <image>` | the interview | contrast, whitespace ratio, spacing unit and colour roles measured from a reference image. The measurements transfer; the colours do not. |
| `tools/sightline.py <screenshot>` | the aesthetic critic | the three regions where the eye lands first, with a map image |
| `tools/frames.py <video>` | the motion critic | frames and a timeline of motion from a screen recording, so timing and easing become numbers |
| `tools/video-to-motion-spec.md` | you and the builder | the procedure that turns a clip you like into a motion spec |

## What is in the folder

```
SKILL.md                   the command: phases, rules, flags
loop/orchestration.md      the procedure the main session follows, step by step
loop/direction.md          2–3 directions from pictures before the cycles; the loop reopens it when the look is stuck
loop/evidence.md           state harness, task walker, hard checks: run before the critics every cycle
interview/questions.md     the question bank, in rounds, with a redesign branch
interview/brief-template.md
critics/00-shared.md       what every critic gets, the output JSON, the severity rules
critics/01..09-*.md        one lens each, with the 4 / 7 / 8 / 9 examples
builder/fix.md             the rules for the single writer
taste/                     README.md (load order) · calibration.md · owner-taste.md · references.md · slop.md · defaults.md
integrations/              appshots.md · motion-anything.md (others: notes in docs/sources.md)
tools/                     the three scripts and the video-to-spec procedure
templates/cycle-report.md
examples/uiux.md           a house-rules file to copy
examples/taste.md          a project taste file to copy
examples/owner-taste.md    what your own taste file looks like after a few runs
docs/                      the diagrams and sources.md
evals/                     planted-defect fixtures, a clean control, check_fixtures.py (see evals/README.md)
```

## Rules that never bend

- Critics read. The builder writes. Never two writers on the same files.
- A critic sees the brief, the screenshots, the code and the last cycle's screenshots. It never sees the builder's reasoning.
- No invented facts. No made-up numbers, prices, quotes or claims. A visual that needs data the project does not have logs `needs data:`.
- Your house rules win over the skill's rules.
- The loop stops by itself: bar, plateau or cap. It never stops to ask you.
- The report says what failed, with the evidence.

## Where the ideas come from

uiux borrows ideas from a 2026 guide on AI design systems, from Nate Herk's Scrollcraft interview, from behavioural research (Iyengar, Nunes & Drèze, Cialdini, Kahneman), from WCAG 2.2, and from the [impeccable](https://github.com/pbakaus/impeccable) skill's modes and playbooks. Every source, with a link, is in [docs/sources.md](docs/sources.md).

## What uiux is not

It is not a design system. It is not a component library. It does not replace taste. It is a procedure that makes a model ask before it builds, check after it builds, and stop when it is done.

MIT. Written in [Simplified Technical English](https://www.asd-ste100.org) where the standard allows.
