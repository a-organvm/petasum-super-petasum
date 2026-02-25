## 2024-05-22 - Script Injection in GitHub Actions
**Vulnerability:** Untrusted input (issue labels) was interpolated directly into `run` blocks and `actions/github-script` using `${{ ... }}` syntax.
**Learning:** GitHub Actions performs macro substitution for `${{ ... }}` before execution, allowing malicious input to alter script logic or shell commands.
**Prevention:** Always map untrusted inputs to environment variables for shell scripts, or access `context.payload` directly within JavaScript steps.
