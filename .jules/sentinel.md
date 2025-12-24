## 2024-05-23 - GitHub Actions Injection
**Vulnerability:** Widespread use of `${{ ... }}` interpolation inside `run` scripts and `github-script` blocks, allowing for command and script injection if inputs (like labels) are malicious.
**Learning:** GitHub Actions contexts are not auto-sanitized when interpolated into shell or JS.
**Prevention:** Always use environment variables for `run` scripts. For `github-script`, use `process.env` or `context.payload` directly.
