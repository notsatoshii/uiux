# Orchestration

The main session is the orchestrator. It never designs and never fixes; it runs the procedure below and keeps the log.

## 0. Intake

1. Resolve the surface from the argument: a route, a file, a folder or a URL. Record the entry file(s) and the dev-server command (from `.claude/launch.json`, `package.json`, or the project's run skill).
2. New build or existing? Existing = the entry file renders something today. New = nothing renders yet or the user said "new".
3. House rules: read `uiux.md` in the project root if present, then the project's CLAUDE.md. Taste: note whether the project has a `taste.md`, whether the owner's taste file exists (`$UIUX_TASTE` or `~/.claude/uiux/taste.md`; if not, offer `/uiux taste init` once in the chat and continue), and which taste skills are installed (`impeccable`, `design-taste-frontend`, `high-end-visual-design`); record both in the brief's House rules section so critics 05–09 and the builder load them without probing. Pull out: copy rules (language, register, "copy may not change"), parity rules, forbidden vocabulary, bar override, token budget. Write them into the brief's House rules section verbatim.
4. Existing brief at `docs/design/<surface>/brief.md`? Keep it unless the user asked for a new interview.
5. Screenshot tooling: in order of preference, the host's preview/browser tools, Playwright MCP, the `playwright-cli` skill. If none works, critics work from code alone and every report says so in its first line.
5b. Connectors and tools present: Mobbin, HyperFrames or Remotion skills, FFmpeg, Python with Pillow. Record what is available in the brief's House rules section so every critic knows without probing.
6. Surface mode, borrowed from impeccable: persuade (landing, pricing), operate (app UI, admin), read (docs, articles), experience (portfolio, showcase). The mode changes which rubric anchors apply.

## 1. Interview

Run `interview/questions.md` with the `grilling` skill's round format. Skip questions whose answer is already in the brief, the house rules, PRODUCT.md or DESIGN.md. End with the definition of done; wait for the user to approve it; write the brief. A `--dry` run stops here.

## 2. First build (new surfaces only)

Build the whole surface from the brief, with taste loaded first (`taste/README.md` order) and the strongest build skill installed (`impeccable` new-work, else `design-taste-frontend`, else plain with `taste/defaults.md`). Mobile viewport first if the brief says the primary device is a phone. Then screenshots (see 3.1) and go to cycles. Do not review during the build.

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

Active critics by cycle:

- Cycle 1 and any cycle where functionality scored below 8 last time: 01 best practices, 02 references, 03 design system, 04 functionality, 05 aesthetic.
- Once functionality has scored ≥ 8: add 06 visualize, 07 motion, 08 delight. Once visualize has landed its findings (cycle after its first run), motion also reviews the visuals it produced.
- Once every other active critic scored ≥ bar − 1 in the previous cycle: add 09 micro-craft. It runs at most twice per loop.

Tools and integrations the critics may use are listed in `tools/README.md` and `integrations/`. A critic that uses one cites its output (file path, screen id) in the finding. When a connector in `integrations/` is not connected, the critic says so in its summary's first line and continues without it.

With `--only`, run just those.

Each critic returns the JSON block defined in `00-shared.md`. A result without quoted anchors, or with a finding that has no file or element reference, is rejected and that critic re-run once.

### 3.3 Merge

Combine findings. Dedupe by element + issue. Rank: severity 1 (broken, wrong, violates a house rule) → 2 (hurts the goal) → 3 (polish). Within a severity, lower-numbered critic first. Drop suggestions (critic 08's "ideas" list) from the fix list; they go to the report only.

Needs-user items (copy changes under a "copy may not change" rule, brand picks, facts, money) go to a `waiting on user` list, never to the builder.

### 3.4 Builder, alone

One subagent, `builder/fix.md`, gets the ranked list, the brief, the house rules and the file paths. When a finding calls for a generated motion asset, the builder writes its spec into the cycle report first and makes it per `integrations/motion-assets.md`; feedback-moment animations follow `integrations/lottie.md`. It fixes top-down, severity 1 and 2 fully, severity 3 as far as the cycle budget allows, and returns what it changed and what it did not, with reasons. It may not add features from the ideas list and may not touch files outside the surface.

### 3.5 Score and decide

Re-screenshot (3.1). Write `docs/design/<surface>/cycle-N.md` from `templates/cycle-report.md`: scores per critic, findings fixed / open / waiting, the builder's note, and each critic's blind comparison verdict (better / same / worse than the previous cycle).

Stop when any of these is true, and say which:

- **Bar:** every active critic scored ≥ bar this cycle, and no severity-1 finding is open.
- **Plateau:** a majority of critics said "same" or "worse" two cycles running.
- **Cap:** cycle N = `--cycles`, or the token budget in the house rules is reached.
- **User's call:** the only open severity-1 items are in `waiting on user`.

Else cycle N+1.

## 3.6 Capture taste

Keep a running list, during the run, of every reaction the owner gave about the look (a preview, a screenshot, a cycle report): their words, the cycle, the surface. Not facts, copy edits, bugs or priorities. At the end of the run, append them to the owner's taste file per `taste/owner-taste.md` and list the added lines in the chat summary so the owner can strike any.

## 4. Report

`docs/design/<surface>/final.md`: the stop reason, the score table across cycles, open items, the waiting-on-user list, the ideas list from critic 08 with one line each, and the commands to reproduce the screenshots. In chat: five lines at most, with the stop reason first.

Commit only if the house rules or the user said so; otherwise leave the work uncommitted and say so.
