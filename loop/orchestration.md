# Orchestration

The main session is the orchestrator. It never designs and never fixes; it runs the procedure below and keeps the log.

## 0. Intake

0. Installed copy: the skill that runs must be this repo, not an old copy. Check that the running skill folder has `loop/direction.md`, `loop/evidence.md` and `taste/calibration.md`, and read the version line in `SKILL.md`; if any is missing, stop and tell the user to relink `~/.claude/skills/uiux` to the repo, because an outdated copy runs without the taste layer and the newer critics. Write the version into the brief's header.
1. Resolve the surface from the argument: a route, a file, a folder or a URL. Record the entry file(s) and the dev-server command (from `.claude/launch.json`, `package.json`, or the project's run skill).
2. New build or existing? Existing = the entry file renders something today. New = nothing renders yet or the user said "new".
3. House rules: read `uiux.md` in the project root if present, then the project's CLAUDE.md. Taste: note whether the project has a `taste.md`, whether the owner's taste file exists (`$UIUX_TASTE` or `~/.claude/uiux/taste.md`; if not, offer `/uiux taste init` once in the chat and continue), and which taste skills are installed (`impeccable`, `design-taste-frontend`, `high-end-visual-design`); record both in the brief's House rules section so critics 05–09 and the builder load them without probing. Pull out: copy rules (language, register, "copy may not change"), parity rules, forbidden vocabulary, bar override, token budget. Write them into the brief's House rules section verbatim.
4. Existing brief at `docs/design/<surface>/brief.md`? Keep it unless the user asked for a new interview.
5. Screenshot tooling: in order of preference, the host's preview/browser tools, Playwright MCP, the `playwright-cli` skill. If none works, critics work from code alone and every report says so in its first line.
5b. Connectors and tools present: Appshots (`appshots_whoami`), motion-anything, FFmpeg, Python with Pillow. Record what is available in the brief's House rules section so every critic knows without probing.
5c. Real-app reference board (required, before the brief is written): screens of 3–6 leading products in the surface's category, on the same device class. Appshots when connected (`integrations/appshots.md`), limited to the apps the user confirmed in interview question 7; otherwise the iPhone/Android screenshots on their public App Store / Google Play pages (scripted with Playwright), plus every reference image the owner sent. Save the board as one image and the single screens in the session scratchpad, never in the project repo (they are someone else's copyright). Every visual critic (02, 05, 06, 07, 09) and the builder look at it each cycle. Write down, for the board as a whole, its proportions: base colour, how much of the screen is accent colour, type weight and size of headings and numbers, how decoration is used (usually: none; photos and data carry the colour). The brief's visual world must agree with these proportions or say why not.
6. Surface mode, borrowed from impeccable: persuade (landing, pricing), operate (app UI, admin), read (docs, articles), experience (portfolio, showcase). The mode changes which rubric anchors apply.
7. Calibration board (`taste/calibration.md`): note how many approved and rejected images exist. Empty → offer `/uiux taste init` once and seed from the owner's earlier projects when the host knows them; continue either way.
8. State harness (`loop/evidence.md` §1): list the states, make them reachable, write the harness. For a new surface this happens after the first build; for an existing one, now. Cycle 1 waits for it.

## 1. Interview

Run `interview/questions.md` with the `grilling` skill's round format. Skip questions whose answer is already in the brief, the house rules, PRODUCT.md or DESIGN.md. After rounds 1–3, run the direction step (`loop/direction.md`): build 2–3 directions of the key screen, show them side by side with the reference board, and ask which; the pick is the interview's last answer. Then read back the definition of done, write the brief and start; there is no approval step and no question after this one. A `--dry` run stops after the brief.

## 2. First build (new surfaces only)

Build the whole surface from the brief and the chosen direction, with taste loaded first (`taste/README.md` order) and the strongest build skill installed (`impeccable` new-work, else `design-taste-frontend`, else plain with `taste/defaults.md`). Mobile viewport first if the brief says the primary device is a phone. Then the state harness (`loop/evidence.md` §1) and go to cycles. Do not review during the build.

## 2b. Owner preview (after the first build, and whenever a cycle changes the look)

Send the owner one side-by-side image: the surface's main screens (phone, first screen only) next to the reference board, in the chat, without asking a question. The loop does not wait. But any reaction the owner gives outranks every critic score: a negative one ("tacky", "bad", "ugly", "cheap") resets the aesthetic, references and micro-craft scores to at most 4, the orchestrator writes a one-paragraph diagnosis against the reference board, the brief's visual world is rewritten from the owner's words, and the next build restarts from that. Log the reaction per 3.6.

Never deploy or ship a redesign the owner has not seen in a preview. "The owner wants to test" means: deploy only what they have reacted to, or say plainly that the look is unreviewed.

## 3. Cycle

Cycle N:

### 3.1 Evidence pass

Start the dev server if needed and run `loop/evidence.md` §1–3: the state harness captures every state at every brief viewport (default 390×844 and 1440×900; light and dark if the surface has both), plus one hover, one pressed/focused and one open menu or modal; the task walker runs every usability task in a real browser; the hard checks run. Output: `shots/cycle-N/`, `shots/cycle-N/walk/`, `evidence/cycle-N.md`. A failing build or a new console error is a severity-1 finding before the critics run.

### 3.2 Critics, in parallel

Spawn one subagent per critic in a single message. Each gets exactly this, nothing more:

- `critics/00-shared.md` and its own `critics/NN-*.md`
- the brief (with the chosen direction)
- the surface's source files (paths)
- this cycle's screenshots and evidence file and, from cycle 2 on, the previous cycle's screenshots
- the house rules section
- the real-app reference board (intake 5c) for critics 02, 05, 06, 07 and 09
- the calibration board (`taste/calibration.md`) for critics 05, 08 and 09

Every critic runs every cycle; none waits for another's score. The phase decides how many findings each may return and which critics lead the builder's list:

| phase | cycles (of 6; scale to `--cycles`) | lead critics (theme) | the others |
|---|---|---|---|
| A structure | 1–2 | 04 functionality, 05 aesthetic, 02 references | 01, 03 full; 06, 07, 08 at most 3 findings each, structural only (room for a chart, a state that needs motion, where the signature move lives) |
| B feel | 3–4 | 06 visualize, 07 motion, 08 delight | 01–05 full |
| C craft | 5–6 | 09 micro-craft, 03 design system, 01 best practices | all full |

09 micro-craft runs only in phase C. With fewer cycles, give A one cycle, then B, then C; with `--only`, run just those critics and skip the phase table. A reopen (`loop/direction.md`) sends the loop back to phase A for one cycle.

Tools and integrations the critics may use are listed in `tools/README.md` and `integrations/`. A critic that uses one cites its output (file path, screen id) in the finding. When a connector in `integrations/` is not connected, the critic says so in its summary's first line and continues without it.

Each critic returns the JSON block defined in `00-shared.md`. A result without quoted anchors, or with a finding that has no file or element reference, is rejected and that critic re-run once.

### 3.3 Merge

Combine findings. Dedupe by element + issue. Rank: severity 1 (broken, wrong, violates a house rule) → 2 (hurts the goal) → 3 (polish). Within a severity, the phase's lead critics first, then lower-numbered. Drop suggestions (critic 08's "ideas" list) from the fix list; they go to the report only.

Cut the list for the builder: every severity-1 finding, then the phase's lead critics' severity-2 findings, then others, up to **12 findings in total** (severity 1 is never cut, even past 12). Name the cycle's **theme** in one line (e.g. "one focal element per screen", "data reads as visuals", "radii and shadows as one family") and put findings that serve it first. Everything cut carries to the next cycle's merge; it is not lost.

Calls the loop makes itself, never asking: a brand pick or a choice between options gets the safest option that follows the brief and the design system; a missing fact, number or price stays a visible `needs data:` placeholder; nothing paid is bought. Each call is logged under `decisions the loop made` (call, option chosen, why, element) and handed to the builder as settled. Copy changes under a "copy may not change" rule are listed as proposed rewrites, never applied.

### 3.4 Builder, alone

One subagent, `builder/fix.md`, gets the cut list (at most 12 plus any severity 1) and the cycle's theme, the brief, the house rules and the file paths. When a finding calls for a generated motion asset (a rendered clip or a Lottie file), the builder writes its spec into the cycle report first (purpose, place, duration, data source, tokens), uses the project's tokens only, and ships a poster plus a reduced-motion path; engines are noted in `docs/sources.md`. It fixes top-down, severity 1 and 2 fully, severity 3 as far as the cycle budget allows, and returns what it changed and what it did not, with reasons. It may not add features from the ideas list and may not touch files outside the surface.

### 3.5 Score and decide

Re-run the harness for the after shots. Write `docs/design/<surface>/cycle-N.md` from `templates/cycle-report.md`: phase and theme, scores per critic, the walk numbers per task (steps, time, hesitations, dead ends) against the last cycle, findings fixed / open / carried, the builder's note, and each critic's blind comparison verdict (better / same / worse than the previous cycle).

Reopen check before the stop rules: aesthetic ≤ 6 for the second cycle running, or the fresh-eyes check failed twice → run the reopen in `loop/direction.md` (at most twice per run).

Stop when any of these is true, and say which:

- **Bar:** every critic scored ≥ bar this cycle, no severity-1 finding is open, at least one phase-C cycle has run (if everything reaches the bar earlier, the next cycle jumps to phase C so micro-craft runs once), and the fresh-eyes check passed: one extra subagent that has NOT read the brief is shown the surface next to the reference board and the calibration board's approved images (without their words) and asked only "Would this sit on a phone's home screen next to these apps without looking cheaper or more decorated? yes / no, and the one thing that gives it away". A no keeps the loop going with that one thing as a severity-2 finding. A brief can encode bad taste; this check cannot read the brief, so it cannot be talked into it.
- **Plateau:** a majority of critics said "same" or "worse" two cycles running.
- **Cap:** cycle N = `--cycles`, or the token budget in the house rules is reached.

Else cycle N+1.

## 3.6 Capture taste

Keep a running list, during the run, of every reaction the owner gave about the look (the direction pick, a preview, a screenshot, a cycle report): their words, the cycle, the surface. Not facts, copy edits, bugs or priorities. At the end of the run, append them to the owner's taste file per `taste/owner-taste.md`, add the screens they reacted to (and the chosen and rejected directions) to the calibration board per `taste/calibration.md`, and list what was added in the chat summary so the owner can strike any.

## 4. Report

`docs/design/<surface>/final.md`: the stop reason, the score table across cycles, open items, the decisions the loop made (once, deduped), proposed rewrites of locked copy and needs-data placeholders, the ideas list from critic 08 with one line each, and the commands to reproduce the screenshots. In chat: five lines at most, with the stop reason first.

Commit only if the house rules or the user said so; otherwise leave the work uncommitted and say so.
