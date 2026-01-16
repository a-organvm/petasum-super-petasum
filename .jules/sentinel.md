## 2024-01-16 - GitHub Actions Script Injection
**Vulnerability:** Script injection in `org-issue-notifications.yml` where user-controlled labels were interpolated directly into shell scripts and JavaScript code using `${{ ... }}`.
**Learning:** Interpolating GitHub Actions expressions directly into `run` blocks or `github-script` creates injection risks because the runner expands them before execution, allowing malicious input to break out of string contexts.
**Prevention:** Use environment variables for shell scripts (mapping `${{ ... }}` to `env`) and access `context.payload` directly in `github-script` to handle user input safely.
