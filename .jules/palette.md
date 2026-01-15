
## 2026-01-15 - [Navigation in Long Markdown Files]
**Learning:** This repository relies heavily on raw Markdown rendering on GitHub (no generated site). Long documentation files become difficult to navigate without a "Back to Top" mechanism.
**Action:** Standardize long Markdown documents by adding an anchor `<a id="top"></a>` after the H1 and inserting `[Back to Top](#top)` links before major section separators (`---`) or level 2 headers (`##`).
