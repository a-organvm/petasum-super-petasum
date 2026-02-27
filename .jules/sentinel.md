## 2024-05-23 - [Injection in GitHub Actions]
**Vulnerability:** Found a command injection vulnerability in `org-issue-notifications.yml` where `${{ join(github.event.issue.labels.*.name, ',') }}` was interpolated directly into a bash script. An attacker could craft a label name containing shell metacharacters to execute arbitrary code.
**Learning:** GitHub Actions expression interpolation `${{ ... }}` happens *before* the shell executes the script. It behaves like a macro replacement. If the interpolated string contains quotes or semicolons, it can break out of the string context in the shell script.
**Prevention:**
1. Never interpolate user input directly into `run` blocks.
2. Map the input to an environment variable using the `env` context (e.g., `env: MY_INPUT: ${{ github.event.input }}`).
3. Access the environment variable in the script (e.g., `echo "$MY_INPUT"`).
4. For complex objects, pass them as JSON via `toJson()` and parse them in the script (or use `jq` or simple grep if robust parsing isn't needed).
5. In `actions/github-script`, prefer `context.payload` over interpolation.
