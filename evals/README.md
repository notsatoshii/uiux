# Evals: do the critics find what they should?

A rubric edit or a model upgrade can make a critic miss things, or invent them. This folder is the check: three small pages with planted defects plus a clean control, in the `claude plugin eval` layout. Same layout as the lesson skill's `evals/`.

## The cases

| case | critics run (`--only`) | planted defect | graders expect |
|---|---|---|---|
| `planted-contrast-iconbutton` | 01, 03 | `.lede` is `#a3a3a3` on white (2.5:1); the header menu button is an icon with no accessible name | sev 1 or 2 naming contrast; sev 1 or 2 on the menu/icon button naming the missing name or label |
| `planted-invented-proof` | 01, 03 | the lede claims "94% of students raise their grade in 30 days" (invented; the brief carries no numbers) and opens with "Guaranteed", forbidden in `uiux.md` | sev 1 on the statistic; sev 1 on the forbidden word |
| `planted-overflow-tap` | 01, 04 | `.plans` is a fixed 520px wide (sideways scroll at 375); the filter chips are 28px tall | sev 1 or 2 naming horizontal scroll or overflow; sev 1 or 2 on the chips naming tap target or size |
| `control-clean` | all nine | none; a plain, calm page that should sit near the bar | no sev-1 anywhere (regex and an `llm` judge) |

Each case folder holds:

- `prompt.md`: runs `/uiux <slug>/index.html --skip-interview --cycles 1 --only <critics>`.
- `case.yaml` + `scaffold.sh`: copies `workspace/` (the page, `docs/design/<slug>/brief.md` with the direction already chosen, and `uiux.md` house rules) into the run's empty workspace. `scaffold.sh` is generated; edit `workspace/` and run `python evals/check_fixtures.py --build`.
- `workspace/`: the fixture. The product (Pinecone Planner) is fictional; the one invented statistic is planted on purpose and labelled as invented in its grader, not in the fixture.
- `graders/`: `cycle-report-exists` (`file_exists` on `cycle-1.md`), `found-*` (`regex` on the cycle report: a finding line with the expected severity and keywords), and for the control `no-sev1-regex` plus `no-sev1-judge` (`llm`). The comment at the top of each grader says what was planted.

The regex graders assume the cycle report's finding lines start `- [<severity>] [<critic>] ...` with the element and issue on the same line, as `templates/cycle-report.md` shows. If that template changes, update the patterns and the samples in `check_fixtures.py`.

There are no per-critic graders yet. uiux critics return their JSON inline to the orchestrator instead of writing it to a file, so a grader cannot see which critic found a defect. The lesson skill writes `history/cycle-N/critic-NN.json`; once uiux does the same, add `critic-NN-*` graders as lesson has.

## Check the fixtures without Claude

```
python evals/check_fixtures.py
```

Python 3.10+, standard library only. Runs a small static check on every fixture (contrast of CSS colour pairs, unnamed buttons and links, images without alt, fixed widths over 375px, tap targets under 44px, forbidden words from `uiux.md`, numbers the brief does not carry) and confirms each fixture trips exactly its planted rules and the control trips none; checks every `scaffold.sh` against its `workspace/`; runs each regex grader against a sample finding line it must match and planted graders against a control sample they must not match; checks the trigger queries. Exit 0 when all hold. Run it after editing any fixture or grader.

## Run the suite

Needs a Claude Code version with `claude plugin eval`, and the repo loadable as a plugin (`.claude-plugin/plugin.json`; check with `claude plugin validate .`). From the repo root:

```
claude plugin eval . --scaffold --allow-tools Write Edit Bash --ablation none --runs 3
```

- `--scaffold` is required: without it the workspace is empty and every case fails.
- `--allow-tools Write Edit Bash`: the loop writes the cycle report and runs the screenshot harness through Bash. Without a browser tool the critics work from code alone and say so; the planted defects are all visible in the code.
- Bash on Windows needs WSL2 (no sandbox backend on native Windows). On Linux, install `bubblewrap` and `socat` first.
- `--ablation none` skips the no-plugin baseline, which cannot run `/uiux`.
- One case while iterating: `claude plugin eval . --case planted-contrast-iconbutton --runs 1 --scaffold --allow-tools Write Edit Bash --ablation none`.
- Cost: each run is a real cycle (the control runs all nine critics plus the builder). Set `--max-cost-usd`, and pin `--model` and `--judge-model` when comparing runs over time.

Read `evals/results/<timestamp>/report.html` (git-ignored). A `found-*` grader that fails means every critic missed that defect.

## Trigger test

`trigger-queries.json` holds 20 requests, 10 that should start `/uiux` (English and Korean) and 10 near misses (translation, a lesson plan, a one-line typo fix, a deck, grilling, a chart) that should not. Same format as skill-creator's trigger scripts:

```
PYTHONUTF8=1 python <skill-creator>/scripts/run_eval.py --eval-set evals/trigger-queries.json --skill-path . --runs-per-query 3
```
