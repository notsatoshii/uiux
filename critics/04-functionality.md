# 04 Functionality

Lens: does everything in the brief's feature list work, and does the flow make sense end to end? It leads phase A (structure) with 05 and 02; it no longer gates the other critics.

## Method

1. Take the brief's feature list (and for existing surfaces, the must-not-change list and the usability tasks). Each item is a row: works / partly / broken / missing, with evidence (a screenshot from `shots/cycle-N/`, a walk step, or the code path you traced).
2. Read the task walker's log (`evidence/cycle-N.md`, `shots/cycle-N/walk/`): for each task, its steps, time, hesitations and dead ends, against the previous cycle. Every hesitation and dead end is a finding with its step screenshot; a task that could not be completed is severity 1. Then name any step that could be removed. Trace code only where the walk could not go, and say so.
3. Check every interactive element's states: default, hover, focus, active, disabled, loading, success, error. Missing states are findings.
4. Check data edges from the harness screenshots: empty, one item, many items, long strings, missing image, slow response, error. A state listed in `states.md` as unreachable is judged from the code and marked so. For forms: validation timing, error placement, what happens on submit, on failure, on double submit.
5. Load time on a phone: with the network throttled to a decent 4G (about 20 Mbps, 40 ms), time from tap to the first usable screen, and from opening a feature to it being ready (camera, models, maps, video). Over 3 s anywhere is severity 2; a screen that blocks on a heavy download or a start-up that can hang is severity 1. Heavy assets must be preloaded earlier, cached and never block the UI.
6. Check that nothing outside the brief regressed on an existing surface: routes, links, data shown, feature parity. Any lost feature is severity 1.

## Anchors

- **4:** a feature in the list is missing or broken, or a usability task cannot be completed, or an existing feature was lost in a redesign.
- **7:** every feature works and every task completes; one flow has a needless step or a state (error, empty, loading) is unhandled somewhere visible.
- **8:** every feature and task works at every brief viewport and every state in the evidence file holds; the walk log shows no dead ends and at most one hesitation per task; nothing regressed; one step in one task could still be removed.
- **9:** every feature and task works at every viewport in the brief; every state has been seen; no task has a step that could be removed; nothing regressed; a first-time visitor would not hesitate at any point.
