## 2024-02-14 - GitHub Actions Script & Code Injection
**Vulnerability:** Found multiple injection vulnerabilities in GitHub Actions workflows (`org-issue-notifications.yml`):
1. Shell Script Injection: `run: LABELS="${{ ... }}"`. If the interpolated value contains quotes, it can break out of the string and execute arbitrary commands.
2. JavaScript Code Injection: `script: const labels = '${{ ... }}'`. Similar to above, but in a Node.js context.
**Learning:** GitHub Actions expression interpolation (`${{ ... }}`) is performed *before* the script is executed by the shell/runner. This means the script receives the raw value, which becomes code if it contains syntax characters (quotes, semicolons).
**Prevention:** NEVER use `${{ ... }}` directly inside `run:` or `script:` blocks for untrusted input.
1. For `run:`: Map the input to an environment variable in the `env:` block, then use the shell variable (e.g., `$MY_VAR` or `"${MY_VAR}"`).
2. For `actions/github-script`: Use `process.env.MY_VAR` (if mapped) or the available `context` object (e.g., `context.payload.issue...`) instead of interpolation.
