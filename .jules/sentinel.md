## 2024-01-03 - [GitHub Actions Injection]
**Vulnerability:** Found a Command Injection vulnerability in `org-issue-notifications.yml` where `github.event.issue.labels.*.name` was interpolated directly into a shell command using `${{ }}` syntax. This allows malicious label names to execute arbitrary commands.
**Learning:** GitHub Actions expressions `${{ }}` are evaluated *before* the shell starts. If a value contains quotes or shell metacharacters, it modifies the script source code itself.
**Prevention:** NEVER directly interpolate untrusted input into `run` blocks. Always pass untrusted input as environment variables (`env: VAR: ${{ ... }}`) and reference them as `$VAR` in the shell script. The shell will then treat the content as a variable value, not executable code.
