## 2024-05-22 - [Script Injection in GitHub Actions]
**Vulnerability:** Script injection in `actions/github-script` steps where `${{ ... }}` interpolation was used to inject user-controlled data (labels) directly into the JavaScript code.
**Learning:** GitHub Actions performs macro-style replacement for `${{ ... }}` before the script executes, allowing attackers to break out of string literals and execute arbitrary code if the input contains quotes.
**Prevention:** Always use `process.env` for simple values or `context.payload` for complex objects within `github-script`. Never interpolate user input directly into the script string.
