## 2024-05-23 - Command and Script Injection in GitHub Actions
**Vulnerability:** Found `run` steps interpolating `${{ }}` into shell commands and `github-script` steps interpolating `${{ }}` into JavaScript.
**Learning:** GitHub Actions `${{ }}` syntax performs macro replacement before execution. If user input (like issue labels) contains quotes or shell metacharacters, it can break out of string literals in bash or JS, leading to arbitrary code execution.
**Prevention:**
1. **Shell:** Map inputs to environment variables using `env:` block. Access them via `$VAR` in shell.
2. **JS:** Use `process.env.VAR` (if mapped in `env`) or `context.payload` to access event data directly. Never use `${{ }}` inside the script string for untrusted data.
