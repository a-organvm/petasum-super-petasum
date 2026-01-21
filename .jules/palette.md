## 2024-05-22 - [Documentation Navigation]
**Learning:** In long Markdown documentation files without built-in navigation (like `PRINCIPLE_CONFLICTS.md`), users struggle to jump between sections or return to the context. A simple Table of Contents combined with 'Back to Top' anchors significantly improves readability and accessibility.
**Action:** When identifying long documentation files (>300 lines or multiple H2 headers), systematically add a top-level `<a id="top"></a>` anchor, a generated Table of Contents, and `[Back to Top](#top)` links at the end of major sections.
