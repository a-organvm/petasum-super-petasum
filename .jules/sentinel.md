## 2024-05-23 - GitHub Actions Injection and Schema Validation
**Vulnerability:** Found both direct Script Injection (interpolating `${{ ... }}` into JS strings) and invalid YAML schema (orphaned top-level keys) in `org-issue-notifications.yml`. The schema issue was subtle because it was syntactically valid YAML (top-level keys) but semantically invalid for Actions.
**Learning:** Tools like `pyyaml` only validate syntax, not the GitHub Actions schema. Valid YAML can still be a broken workflow. Direct interpolation in `actions/github-script` is a common but critical vulnerability pattern.
**Prevention:** Use `context.payload` properties in JS steps instead of `${{ ... }}` interpolation. Always verify workflow structure visually or with a schema-aware linter, not just a generic YAML parser.
