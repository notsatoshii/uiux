---
# PLANTED: .chip is height: 28px, under the 44px tap-target minimum.
# Expect a severity 1 or 2 finding on the chips / filters that names tap target or size.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?[12]\](?=[^\n]*(?:chip|filter))(?=[^\n]*(?:tap|target|44|28|small|height))'
flags: mi
target:
  source: file
  path: docs/design/eval-overflow/cycle-1.md
---
