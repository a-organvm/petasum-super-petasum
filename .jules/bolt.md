## 2024-05-23 - Workflow Optimization Pattern
**Learning:** Performance in GitHub Actions is significantly improved by consolidating multiple shell/JS steps into a single `actions/github-script` step. This avoids container startup overhead and simplifies context data passing.
**Action:** Identify workflows with sequential shell/script steps that share context and merge them into a unified JS block.
