## 2024-02-14 - Script Injection in GitHub Actions
**Vulnerability:** Found critical script injection vulnerabilities in `org-issue-notifications.yml` where user-controlled data (issue labels/title) was interpolated directly into shell and JS scripts.
**Learning:** Interpolating `${{ ... }}` directly into `run:` or `script:` blocks allows attackers to break out of the string context and execute arbitrary code if they control the input (e.g., via labels).
**Prevention:** Always map user-controlled inputs to environment variables (`env:`) before using them in shell scripts, or access them via `process.env` / `context.payload` in `actions/github-script`.
