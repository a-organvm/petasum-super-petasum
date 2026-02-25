## 2024-05-23 - GitHub Actions Schema Validation
**Learning:** Standard YAML linters like `yamllint` and parsers like `pyyaml` do not validate GitHub Actions schema correctness (e.g., nesting of `run` or `env` blocks). They only validate YAML syntax.
**Action:** Always verify GitHub Actions workflow structure manually or against the official schema, as valid YAML can still be an invalid workflow.
