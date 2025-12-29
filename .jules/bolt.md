## 2024-12-29 - [Workflow Step Consolidation]
**Learning:** Consolidating multiple shell and `github-script` steps into a single `github-script` step significantly reduces workflow overhead (container startup, context switching) and eliminates the need for intermediate `GITHUB_OUTPUT` usage.
**Action:** When optimizing workflows, look for patterns where data is passed between shell steps and JS steps, and merge them into a unified JS block.

## 2024-12-29 - [YAML Line Length in Scripts]
**Learning:** `yamllint` enforces 80-char limits even on embedded `script:` blocks in GitHub Actions. This requires aggressive wrapping of JS code or extracting long strings into variables.
**Action:** Write embedded JS with strict formatting in mind, or consider using external script files if the logic becomes too complex to format within YAML constraints.
