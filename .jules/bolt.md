## 2025-02-18 - Broken Workflow Detection
**Learning:** Standard linting tools may not be running in CI if the workflow file itself is malformed. This repo contained a workflow where `env` and `run` blocks were orphaned at the root level, effectively treating the rest of the file as a string.
**Action:** Always validate existing YAML syntax before optimizing, as "optimizing" a broken file is actually a bug fix. Consolidating logic into `github-script` avoids YAML indentation pitfalls for complex multi-step logic.
