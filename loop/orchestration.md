# Orchestration

The main session is the orchestrator. It never designs and never fixes; it runs the procedure below and keeps the log.

## 0. Intake

0. Installed copy: the skill that runs must be this repo, not an old copy. Check that the running skill folder has `taste/` and `critics/09-microcraft.md`; if not, stop and tell the user to relink `~/.claude/skills/uiux` to the repo (a stale copy ran a whole Oratio redesign on 2026-10-20 with no taste layer, no Mobbin and no micro-craft critic).
1. Resolve the surface from the argument: a route, a file, a folder or a URL. Record the entry file(s) and the dev-server command (from `.claude/launch.json`, `package.json`, or the project's run skill).
2. New build or existing? Existing = the entry file renders something today. New = nothing renders yet or the user said "new".
3. House rules: read `uiux.md` in the project root if present, then the project's CLAUDE.md. Taste: note whether the project has a `taste.md`, whether the owner's taste file exists (`$UIUX_TASTE` or `~/.claude/uiux/taste.md`; if not, offer `/uiux taste init` once in the chat and continue), and which taste skills are installed (`impeccable`, `design-taste-frontend`, `high-end-visual-design`); record both in the brief's House rules section so critics 05–09 and the builder load them without probing. Pull out: copy rules (language, register, "copy may not change"), parity rules, forbidden vocabulary, bar override, token budget. Write them into the brief's House rules section verbatim.
4. Existing brief at `docs/design/<surface>/brief.md`? Keep it unless the user asked for a new interview.
5. Screenshot tooling: in order of preference, the host's preview/browser tools, Playwright MCP, the `playwright-cli` skill. If none works, critics work from code alone and every report says so in its first line.
5b. Connectors and tools present: Mobbin, HyperFrames or Remotion skills, FFmpeg, Python with Pillow. Record what is available in the brief's House rules section so every critic knows without probing.
5c. Real-app reference board (required, before the brief is written): screens of 3–6 leading products in the surface's category, on the same device class. Mobbin when connected; otherwise the iPhone/Android screenshots on their public App Store / Google Play pages (scripted with Playwright), plus every reference image the owner sent. Save the board as one image and the single screens in the session scratchpad, never in the project repo (they are someone else's copyright). Every visual critic (02, 05, 06, 07, 09) and the builder look at it each cycle. Write down, for the board as a whole, its proportions: base colour, how much of the screen is accent colour, type weight and size of headings and numbers, how decoration is used (usually: none; photos and data carry the colour). The brief's visual world must agree with these proportions or say why not.
6. Surface mode, borrowed from impeccable: persuade (landing, pricing), operate (app UI, admin), read (docs, articles), experience (portfolio, showcase). The mode changes which rubric anchors apply.

## 1. Interview

Run `interview/questions.md` with the `grilling` skill's round format. Skip questions whose answer is already in the brief, the house rules, PRODUCT.md or DESIGN.md. End by reading back the definition of done, then write the brief and start; there is no approval step. A `--dry` run stops here.

## 2. First build (new surfaces only)

Build the whole surface from the brief, with taste loaded first (`taste/README.md` order) and the strongest build skill installed (`impeccable` new-work, else `design-taste-frontend`, else plain with `taste/defaults.md`). Mobile viewport first if the brief says the primary device is a phone. Then screenshots (see 3.1) and go to cycles. Do not review during the build.

## 2b. Owner preview (after the first build, and whenever a cycle changes the look)

Send the owner one side-by-side image: the surface's main screens (phone, first screen only) next to the reference board, in the chat, without asking a question. The loop does not wait. But any reaction the owner gives outranks every critic score: a negative one ("tacky", "bad", "ugly", "cheap") resets the aesthetic, references and micro-craft scores to at most 4, the orchestrator writes a one-paragraph diagnosis against the reference board, the brief's visual world is rewritten from the owner's words, and the next build restarts from that. Log the reaction per 3.6.

Never deploy or ship a redesign the owner has not seen in a preview. "The owner wants to test" means: deploy only what they have reacted to, or say plainly that the look is unreviewed.

## 3. Cycle

Cycle N:

### 3.1 Screenshots

Start the dev server if needed. Capture, for every viewport the brief names (default 390×844 and 1440×900): the full page, plus each interactive state the critics need: one hover, one pressed/focused, one open menu or modal, one loading or empty state if the surface has any. Save to `docs/design/<surface>/shots/cycle-N/`. Capture both light and dark if the surface supports both.

### 3.2 Critics, in parallel

Spawn one subagent per active critic in a single message. Each gets exactly this, nothing more:

- `critics/00-shared.md` and its own `critics/NN-*.md`
- the brief
- the surface's source files (paths)
- this cycle's screenshots and, from cycle 2 on, the previous cycle's screenshots
- the house rules section
- the real-app reference board (0.5c) for critics 02, 05, 06, 07 and 09

Active critics by cycle:

- Cycle 1 and any cycle where functionality scored below 8 last time: 01 best practices, 02 references, 03 design system, 04 functionality, 05 aesthetic.
- Once functionality has scored ≥ 8: add 06 visualize, 07 motion, 08 delight. Once visualize has landed its findings (cycle after its first run), motion also reviews the visuals it produced.
- Once every other active critic scored ≥ bar − 1 in the previous cycle: add 09 micro-craft. It runs at most twice per loop.

Tools and integrations the critics may use are listed in `tools/README.md` and `integrations/`. A critic that uses one cites its output (file path, screen id) in the finding. When a connector in `integrations/` is not connected, the critic says so in its summary's first line and continues without it.

With `--only`, run just those.

Each critic returns the JSON block defined in `00-shared.md`. A result without quoted anchors, or with a finding that has no file or element reference, is rejected and that critic re-run once.

### 3.3 Merge

Combine findings. Dedupe by element + issue. Rank: severity 1 (broken, wrong, violates a house rule) → 2 (hurts the goal) → 3 (polish). Within a severity, lower-numbered critic first. Drop suggestions (critic 08's "ideas" list) from the fix list; they go to the report only.

Calls the loop makes itself, never asking: a brand pick or a choice between options gets the safest option that follows the brief and the design system; a missing fact, number or price stays a visible `needs data:` placeholder; nothing paid is bought. Each call is logged under `decisions the loop made` (call, option chosen, why, element) and handed to the builder as settled. Copy changes under a "copy may not change" rule are listed as proposed rewrites, never applied.

### 3.4 Builder, alone

One subagent, `builder/fix.md`, gets the ranked list, the brief, the house rules and the file paths. When a finding calls for a generated motion asset, the builder writes its spec into the cycle report first and makes it per `integrations/motion-assets.md`; feedback-moment animations follow `integrations/lottie.md`. It fixes top-down, severity 1 and 2 fully, severity 3 as far as the cycle budget allows, and returns what it changed and what it did not, with reasons. It may not add features from the ideas list and may not touch files outside the surface.

### 3.5 Score and decide

Re-screenshot (3.1). Write `docs/design/<surface>/cycle-N.md` from `templates/cycle-report.md`: scores per critic, findings fixed / open / waiting, the builder's note, and each critic's blind comparison verdict (better / same / worse than the previous cycle).

Stop when any of these is true, and say which:

- **Bar:** every active critic scored ≥ bar this cycle, no severity-1 finding is open, and the fresh-eyes check passed: one extra subagent that has NOT read the brief is shown the surface next to the reference board and asked only "Would this sit on a phone's home screen next to these apps without looking cheaper or more decorated? yes / no, and the one thing that gives it away". A no keeps the loop going with that one thing as a severity-2 finding. A brief can encode bad taste; this check cannot read the brief, so it cannot be talked into it.
- **Plateau:** a majority of critics said "same" or "worse" two cycles running.
- **Cap:** cycle N = `--cycles`, or the token budget in the house rules is reached.

Else cycle N+1.

## 3.6 Capture taste

Keep a running list, during the run, of every reaction the owner gave about the look (a preview, a screenshot, a cycle report): their words, the cycle, the surface. Not facts, copy edits, bugs or priorities. At the end of the run, append them to the owner's taste file per `taste/owner-taste.md` and list the added lines in the chat summary so the owner can strike any.

## 4. Report

`docs/design/<surface>/final.md`: the stop reason, the score table across cycles, open items, the decisions the loop made (once, deduped), proposed rewrites of locked copy and needs-data placeholders, the ideas list from critic 08 with one line each, and the commands to reproduce the screenshots. In chat: five lines at most, with the stop reason first.

Commit only if the house rules or the user said so; otherwise leave the work uncommitted and say so.
