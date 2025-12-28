# Bolt's Journal

## 2024-05-23 - Performance in GitHub Actions
**Learning:** Performance in this repo is primarily about reducing CI/CD billing time and container overhead. Consolidating steps in workflows is a key pattern.
**Action:** Look for adjacent run steps or script steps that can be merged.

## 2024-05-23 - Injection Risks
**Learning:** Direct interpolation of variables in scripts (e.g., `${{ ... }}`) is a security risk and sometimes breaks if the content has quotes.
**Action:** Use environment variables or `context` object in `github-script`.
