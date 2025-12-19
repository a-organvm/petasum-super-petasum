# Sentinel's Journal

## 2024-05-22 - GitHub Actions Script Injection
**Vulnerability:** Direct interpolation of user input (e.g., `${{ github.event.issue.labels.*.name }}`) into `run` scripts and `github-script` blocks in GitHub Actions workflows.
**Learning:** Even though `github-script` runs in a JS environment, interpolating values directly into the script string allows for code injection if the input contains closing quotes and malicious code. Similarly, in shell scripts, interpolation before shell execution allows command injection.
**Prevention:** Always map inputs to environment variables or use the `context` object directly in JavaScript/TypeScript actions. Never interpolate `${{ ... }}` directly into executable code blocks.
