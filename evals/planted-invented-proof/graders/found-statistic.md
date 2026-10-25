---
# PLANTED: the lede says '94% of students raise their grade in 30 days'. The number is INVENTED for this
# fixture; the brief lists no real numbers and forbids invented statistics. Expect a severity-1 finding on it.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?1\](?=[^\n]*(?:94|statistic|needs data|invented|unsourced|claim))'
flags: mi
target:
  source: file
  path: docs/design/eval-proof/cycle-1.md
---
