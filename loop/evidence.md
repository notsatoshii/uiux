# Evidence

Critics judge what they are shown. In the first two real runs, empty, error, loading and long-name screens were never captured in nine cycles, and the usability tasks were mostly traced in code. The evidence pass fixes that: it runs before the critics every cycle and hands them screenshots and logs, not guesses.

## 1. State harness (built once, at intake; cycle 1 waits for it)

1. **List the states** the surface can be in, per screen: default, empty, one item, many items (enough to scroll), long text (the longest realistic name, title and number, in every language the surface ships), loading, slow (a response held for 3 s), error (the API fails), offline if relevant, permission denied, first visit vs returning, each role the brief names. Write them to `docs/design/<surface>/states.md`: screen · state · how to reach it.
2. **Make each state reachable on demand,** in this order of preference:
   - existing seed scripts or test fixtures in the project;
   - request interception in the screenshot script (Playwright `page.route` returning a fixture, an error status, or a delayed response) — no change to the app;
   - a query flag or cookie that the app already reads;
   - only as a last resort, a dev-only fixture route, behind a dev check, listed for removal.
   Never change production behaviour to make a state reachable.
3. **Write the harness**: one script (`docs/design/<surface>/harness.*` or the project's existing screenshot script) that captures every state at every brief viewport, named `<screen>__<state>_<w>x<h>[_dark].png`, into `shots/cycle-N/`. It runs in under five minutes.
4. **Gate:** cycle 1 starts only when every listed state has a screenshot or a line in `states.md` saying why it cannot be reached and what the critics should assume.

## 2. Task walker (every cycle, before the critics)

One subagent drives a real browser through each usability task in the brief, as the persona, on the primary viewport, with the network throttled to the brief's device class (default: decent 4G, about 20 Mbps, 40 ms).

For each task it logs, step by step:

```
task 2 · "start a 4-minute WSDC speech and record it"
1 · /            · tap "Practise" (tab bar)                 · 0.4 s to usable
2 · /practice    · tap "WSDC"                               · ok
3 · /practice    · looked for length; scrolled 1×; found picker below the fold   · hesitation
4 · …
result: done in 9 steps, 41 s, 1 hesitation, 0 dead ends · shots: walk/task-2/step-NN.png
```

Rules:
- It uses only what is on the screen: visible labels, no reading the code, no URLs typed except the start.
- A hesitation is any step where the next action was not the obvious one (had to scroll to find it, two candidates looked right, the label did not say what would happen). A dead end is a step it had to undo.
- It stops a task after 3 dead ends and logs "could not complete".
- Each step's screenshot goes to `shots/cycle-N/walk/task-K/`.

The walk log is given to critics 02 (references: flow mechanics), 04 (functionality) and 05 (aesthetic: where the eye went), and its numbers (steps, time, hesitations, dead ends per task) go in the cycle report so they can be compared across cycles.

## 3. Hard checks (every cycle)

Run what the project has, record pass/fail and the counts, and give the output to critic 01:
- typecheck, lint, unit tests, build;
- an automated accessibility scan of every captured screen (axe through Playwright, or the project's tool);
- a Lighthouse run (mobile profile) of the main screen: performance, accessibility, best practices, plus LCP and CLS;
- console errors during the walk.

A failing build or a new console error is a severity-1 finding before any critic speaks.

## Output

`docs/design/<surface>/evidence/cycle-N.md`: the states captured (and the ones that could not be), the walk log summary per task, the hard-check results. Critics get the file and the screenshot folder.
