## 2024-01-10 - Script Injection in github-script
**Vulnerability:** Found direct interpolation of `${{ ... }}` values into JavaScript code within `actions/github-script` steps.
**Learning:** GitHub Actions performs macro replacement of `${{ ... }}` *before* the script execution. If user input (like labels or titles) contains backticks or quotes, it can break out of the string literal and execute arbitrary code.
**Prevention:** Always access `github` or `env` context variables via the `context` object or `process.env` in the script, rather than interpolating them.
