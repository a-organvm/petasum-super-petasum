## 2024-12-09 - Workflow Step Consolidation
**Learning:** Consolidating multiple shell steps and `github-script` steps into a single `github-script` block significantly reduces workflow overhead (container startup, context initialization). specifically, merging label logic, commenting, and summary generation into one JS block is a high-value pattern here.
**Action:** Look for other workflows where summary generation is a separate step and merge it into the main logic step.
