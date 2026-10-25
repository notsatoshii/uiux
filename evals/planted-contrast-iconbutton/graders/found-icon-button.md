---
# PLANTED: the header menu <button class="icon-btn"> holds only an svg: no text, no aria-label.
# Expect a severity 1 or 2 finding on the menu / icon button that names the missing accessible name or label.
type: regex
pattern: '^\s*[-*]\s*\[(?:sev(?:erity)?[ -]?)?[12]\](?=[^\n]*(?:menu|icon))(?=[^\n]*(?:name|label|aria))'
flags: mi
target:
  source: file
  path: docs/design/eval-contrast/cycle-1.md
---
