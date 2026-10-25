---
description: 'The lede claims ''94% of students raise their grade in 30 days'' (invented, brief has no numbers) and uses the forbidden word ''Guaranteed''.'
tags: [uiux-critics, planted]
plugins: ["../.."]
runs: 3
max_turns: 120
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite, Write, Edit, Bash]
expected_outcome: 'docs/design/eval-proof/cycle-1.md exists and lists each planted defect; graders/ name them.'
---

/uiux eval-proof/index.html --skip-interview --cycles 1 --only 01-best-practices,03-design-system
