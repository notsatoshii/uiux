---
# PLANTED: .lede is #a3a3a3 on #ffffff, about 2.5:1, under the 4.5:1 body-text minimum.
# Expect a severity 1 or 2 finding that names contrast.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?[12]\](?=[^\n]*contrast)'
flags: mi
target:
  source: file
  path: docs/design/eval-contrast/cycle-1.md
---
