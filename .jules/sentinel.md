# Sentinel's Journal

## 2024-05-22 - Workflow Injection & Schema Vulnerabilities
**Vulnerability:** A workflow contained invalid YAML (orphaned `run`/`env` blocks) that effectively swallowed subsequent steps into a script string. Additionally, critical script injection vulnerabilities existed via `${{ }}` interpolation of user-controlled data (labels) into `github-script` and shell commands.
**Learning:** Broken YAML indentation in GitHub Actions can fail silently in linters like `yamllint` (which checks syntax, not schema) while causing catastrophic logic errors (missing steps). Using `${{ }}` in `github-script` is a persistent anti-pattern that bypasses the sandbox protections.
**Prevention:** Always use `context.payload` in `github-script` to access event data. Validate workflow structural integrity (steps count) beyond just syntax linting.
