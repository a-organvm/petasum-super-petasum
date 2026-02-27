## 2024-05-24 - Injection Vulnerabilities in GitHub Actions
**Vulnerability:** Found both Script Injection (in `actions/github-script`) and Command Injection (in shell `run` steps) caused by direct interpolation of user input (issue labels) using `${{ ... }}` syntax.
**Learning:** GitHub Actions expressions (`${{ ... }}`) are evaluated before script execution, effectively performing string concatenation. This allows attackers to break out of string literals in JS or command arguments in shell if the input contains quotes.
**Prevention:** Always use environment variables for shell steps (`env: VAR: ${{ input }}`) and `context.payload` or `process.env` for `actions/github-script` to access untrusted input safely.
