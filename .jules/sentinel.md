## 2024-05-21 - [GH Actions Injection]
**Vulnerability:** Found both Shell Injection and Script Injection vulnerabilities in GitHub Actions workflows (`org-issue-notifications.yml`).
**Learning:** The workflow interpolated `${{ github.event.issue.labels.*.name }}` directly into shell commands (`LABELS="${{ ... }}"`) and JavaScript blocks (`message += ...`). This allows an attacker to control the flow by creating a label with malicious characters (e.g., `"; rm -rf /; "`).
**Prevention:** NEVER interpolate `${{ ... }}` user inputs into `run` scripts or `github-script` blocks. Always map them to `env` variables first, then access them via `$ENV_VAR` (shell) or `process.env.ENV_VAR` (JS).
