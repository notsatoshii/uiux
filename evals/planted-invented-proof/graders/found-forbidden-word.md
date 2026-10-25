---
# PLANTED: the lede opens with 'Guaranteed', a forbidden word in uiux.md. Expect a severity-1 finding.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?1\](?=[^\n]*guarantee)'
flags: mi
target:
  source: file
  path: docs/design/eval-proof/cycle-1.md
---
