## 2025-05-18 - YAML Validation vs Schema Validation
**Learning:** Standard YAML linters (yamllint) and parsers (pyyaml) only validate YAML syntax (indentation, structure), not the GitHub Actions schema. A workflow file can be valid YAML but broken GHA logic if keys like `run` or `env` are unintentionally placed at the root level due to indentation errors.
**Action:** Always visually verify indentation of workflow steps, or use a schema-aware validator if available. Do not rely solely on `yamllint` for correctness.
