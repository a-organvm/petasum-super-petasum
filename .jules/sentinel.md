## 2024-05-23 - Script and Command Injection in GitHub Actions

**Vulnerability:** Found direct interpolation of user input (issue labels) into Bash `run` scripts and `actions/github-script` JavaScript blocks. This allowed potential command injection in the shell and code injection in the Node.js runner.
**Learning:** Even in `actions/github-script`, using `${{ ... }}` to insert data into the script string acts as a macro replacement before execution. If the data contains code (e.g., `'); process.exit(1); //`), it becomes part of the script source code.
**Prevention:** Never interpolate untrusted data into script strings.
- For Bash: Map inputs to `env` variables and access them via `$VAR`.
- For `github-script`: Access data directly via the `context` object (e.g., `context.payload.issue.labels`) or pass via `env` if necessary.
