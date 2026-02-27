## 2024-03-20 - Markdown Navigation Enhancements
**Learning:** For long technical documentation rendered directly on GitHub (without a static site generator), inserting "Back to Top" links and explicit anchors is a high-impact micro-UX improvement. It significantly reduces scroll fatigue and improves accessibility for keyboard users, despite `markdownlint` warnings about inline HTML.
**Action:** Systematically add `<a id="top"></a>` after the H1 and `[Back to Top](#top)` before section breaks (`---`) in all long Markdown files (>200 lines).
