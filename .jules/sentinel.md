## 2025-01-02 - GitHub Actions Injection Vulnerabilities
**Vulnerability:** Found Command Injection and Script Injection vulnerabilities in `org-issue-notifications.yml`. User-controlled label names were interpolated directly into shell commands and JavaScript code.
**Learning:** GitHub Actions expressions (`${{ ... }}`) are evaluated before the shell executes the command. Direct interpolation into strings allows attackers to break out of quotes and execute arbitrary code.
**Prevention:** Always use `env` context to pass untrusted data to shell commands. For `actions/github-script`, use `process.env` or `context.payload` instead of template interpolation.
