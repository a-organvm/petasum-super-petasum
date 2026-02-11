## 2025-02-18 - GitHub Actions Injection Risks
**Vulnerability:** Discovered both Script Injection (in `github-script`) and Command Injection (in `run` steps) caused by interpolating `${{ github.event.issue.labels... }}` directly into code blocks.
**Learning:** The `${{ ... }}` syntax acts as a macro replacement before execution. Any user-controlled input (like label names, titles, bodies) interpolated this way can break out of string literals and execute arbitrary code.
**Prevention:**
1. **Never** interpolate untrusted input directly into `run` or `script` blocks.
2. For `run` blocks: Map inputs to environment variables using the `env:` key, then use the environment variable in the shell script (e.g., `env: LABEL: ${{...}}` then `echo "$LABEL"`).
3. For `github-script`: Access data via `context.payload` or `process.env`.
