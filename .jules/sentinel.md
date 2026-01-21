
## 2024-05-22 - Script Injection in github-script
**Vulnerability:** Found a Critical Script Injection vulnerability in `org-issue-notifications.yml` where issue labels were interpolated directly into a JavaScript string within a `github-script` step using `${{ join(github.event.issue.labels.*.name, ', ') }}`. This allowed malicious labels to break out of the string context and execute arbitrary code.
**Learning:** GitHub Actions performs macro substitution for `${{ }}` expressions before the script runs. Even inside a JavaScript template literal, untrusted input can manipulate the code structure if not properly sanitized or handled.
**Prevention:** Avoid string interpolation of untrusted input in `github-script`. Instead, access the data directly via the `context` object (e.g., `context.payload.issue.labels`) or pass data as environment variables if using shell scripts.
