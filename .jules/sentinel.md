## 2025-12-29 - GitHub Actions Injection Prevention
**Vulnerability:** Found multiple critical script injection vulnerabilities in GitHub Actions workflows where user inputs (issue labels) were directly interpolated into shell and JavaScript contexts using `${{ ... }}`.
**Learning:** Even internal values like issue labels are untrusted user input. Interpolating them directly into scripts allows attackers to execute arbitrary code on the runner by crafting malicious labels (e.g. closing quotes and executing commands).
**Prevention:** NEVER interpolate `${{ ... }}` directly into `run:` or `script:` blocks. Always pass untrusted data as environment variables (shell) or access via `process.env` / `context.payload` (JS). Use tools like `jq` to parse complex structures safely in shell.
