## 2025-02-18 - Script Injection in GitHub Actions
**Vulnerability:** Found critical script injection vulnerabilities in `github-script` steps where context variables (like labels) were directly interpolated into JavaScript strings using `${{ ... }}`.
**Learning:** `github-script` runs in a Node.js context, but Actions inputs are processed before the script runs. Interpolating untrusted input (like user-controlled labels) directly into the script body creates an injection vector similar to SQLi or XSS.
**Prevention:** Always pass untrusted data as environment variables (`env:`) and access them via `process.env` inside the script, or use the `context` object directly if the data is available there. Never use `${{ }}` inside the `script` block for dynamic values.
