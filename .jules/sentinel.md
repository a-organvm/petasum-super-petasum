## 2024-06-18 - [GitHub Actions Script Injection]
**Vulnerability:** Unsanitized interpolation of `github.event.issue.labels` into shell scripts and JavaScript code.
**Learning:** Using `${{ ... }}` directly in `run` blocks or `actions/github-script` `script` blocks creates a script injection vulnerability if the data contains quotes or shell metacharacters.
**Prevention:** Always map user-controlled data to environment variables using the `env` context and access them via process environment in the script. For `github-script`, access data via `context.payload` or `process.env`.
