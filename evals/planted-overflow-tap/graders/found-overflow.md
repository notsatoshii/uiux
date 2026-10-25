---
# PLANTED: .plans has width: 520px, wider than the 375px phone viewport: the page scrolls sideways.
# Expect a severity 1 or 2 finding that names horizontal scroll / overflow / width.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?[12]\](?=[^\n]*(?:horizontal|overflow|sideways|520|scroll))'
flags: mi
target:
  source: file
  path: docs/design/eval-overflow/cycle-1.md
---
