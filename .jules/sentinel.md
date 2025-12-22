# Sentinel's Journal

## 2025-10-26 - GitHub Actions Script Injection
**Vulnerability:** Found `actions/github-script` steps using `${{ }}` interpolation to inject values into JavaScript code. This allows attackers to inject arbitrary JavaScript by breaking out of the string literal using quotes.
**Learning:** Workflow expression expansion happens *before* the script execution. Simply quoting the interpolated value (e.g., `'${{ inputs.val }}'`) is insufficient if the value contains quotes.
**Prevention:** Pass unsafe inputs as environment variables (using `env:`) and access them via `process.env`, or access event data directly from the `context` object.
