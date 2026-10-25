---
description: 'Clean control: no planted defect. No critic should raise a severity-1 finding.'
tags: [uiux-critics, control]
plugins: ["../.."]
runs: 3
max_turns: 200
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite, Write, Edit, Bash]
expected_outcome: 'docs/design/eval-control/cycle-1.md exists and carries no severity-1 finding.'
---

/uiux eval-control/index.html --skip-interview --cycles 1 --only 01-best-practices,02-references,03-design-system,04-functionality,05-aesthetic,06-visualize,07-motion,08-delight,09-microcraft
