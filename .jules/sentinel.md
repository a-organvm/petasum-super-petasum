# Sentinel's Journal

## 2024-05-24 - Workflow Injection and YAML Hygiene
**Vulnerability:** Found critical script/command injection vulnerabilities in `org-issue-notifications.yml` where user-controlled labels were directly interpolated into shell commands and JavaScript. Also found severe YAML syntax errors (orphaned `env` and `run` blocks) that likely broke the workflow.
**Learning:** Malformed YAML in GitHub Actions might not just fail—it can mask security contexts or lead to unexpected execution paths. Direct interpolation `${{ ... }}` in `run:` or `script:` blocks is a persistent anti-pattern that acts as a macro replacement, allowing code injection.
**Prevention:** Always use environment variables `env: VAR: ${{ ... }}` to pass data to shell commands, and use `process.env.VAR` or `context.payload` in `github-script` to avoid injection. Validate YAML structure with linters.
