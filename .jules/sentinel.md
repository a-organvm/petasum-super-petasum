## 2026-01-09 - Workflow Injection Vulnerabilities
**Vulnerability:** Found critical script and command injection vulnerabilities in GitHub Actions workflow `org-issue-notifications.yml`. Direct interpolation of user input (issue labels) into Bash commands and JavaScript code using `${{ ... }}` allowed for potential remote code execution.
**Learning:** GitHub Actions expression interpolation `${{ ... }}` acts as a macro replacement before execution. When used inside strings in interpreted languages (Bash, JS), it can break out of string delimiters if not properly sanitized or handled.
**Prevention:**
1.  **Bash:** Never interpolate inputs directly into `run` scripts. Map them to environment variables using `env:` and access them via `$VAR`.
2.  **JavaScript (github-script):** Avoid `${{ ... }}` for untrusted data. Access the `context.payload` object directly within the script to handle data safely as JavaScript objects.
