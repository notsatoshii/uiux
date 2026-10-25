---
description: 'The plans row is a fixed 520px wide (horizontal scroll at 375) and the filter chips are 28px tall.'
tags: [uiux-critics, planted]
plugins: ["../.."]
runs: 3
max_turns: 120
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite, Write, Edit, Bash]
expected_outcome: 'docs/design/eval-overflow/cycle-1.md exists and lists each planted defect; graders/ name them.'
---

/uiux eval-overflow/index.html --skip-interview --cycles 1 --only 01-best-practices,04-functionality
