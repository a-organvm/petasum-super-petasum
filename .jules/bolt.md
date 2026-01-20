## 2024-05-23 - Workflow Optimization
**Learning:** Consolidating multiple shell and script steps into a single `actions/github-script` block significantly reduces container startup overhead and simplifies variable passing.
**Action:** Look for workflows with sequential shell/script steps that share context and merge them into a single JS block, using `context.payload` for data access.

## 2024-05-23 - YamlLint Constraints
**Learning:** `yamllint` enforces strict line lengths (80 chars) even within embedded code blocks (like `script: |`), requiring manual line wrapping in JavaScript strings and logic.
**Action:** When writing `github-script` content, proactively wrap long strings and conditions to avoid lint errors during the verification phase.
