## 2024-05-23 - Broken CI/CD Hiding Security Alerts
**Vulnerability:** The workflow `.github/workflows/org-issue-notifications.yml` had a severe YAML syntax error that prevented it from running properly. This would cause the "Organization-Wide Issue Alert" logic to fail silently or error out, potentially masking critical security issues labeled as `org-wide`.
**Learning:** Security controls embedded in CI/CD workflows (like notifications for security incidents) are themselves code and must be treated with the same rigor (testing, linting) as application code. A broken monitoring tool is a security gap.
**Prevention:**
1. Treat `.github/workflows` as critical code.
2. Use linters (like `actionlint` or `yamllint`) to validate workflow syntax before merging.
3. Ensure failure notifications for the workflows themselves are monitored.
