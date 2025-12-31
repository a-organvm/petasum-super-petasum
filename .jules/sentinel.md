# Sentinel's Journal

## 2024-05-23 - GitHub Actions Script Injection
**Vulnerability:** Found direct injection of GitHub event context data (e.g., `${{ join(github.event.issue.labels.*.name, ',') }}`) into shell commands and JavaScript strings.
**Learning:** Even inside `actions/github-script`, using `${{ }}` template syntax creates injection risks because the template is evaluated before the script runs.
**Prevention:** Always use environment variables for shell steps and `context.payload` or `process.env` for script steps. Never interpolate user input directly.
