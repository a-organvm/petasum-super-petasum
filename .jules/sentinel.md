## 2024-05-22 - [YAML Validation in CI]
**Vulnerability:** Malformed YAML structure in GitHub Actions workflows (specifically floating `env` blocks) can pass standard `pyyaml` validation but fail at runtime or be misinterpreted by the Actions runner.
**Learning:** `pyyaml` only checks syntax, not schema. It parsed a `env` block at the root level (or incorrectly merged) as valid YAML, whereas GitHub Actions requires specific structural hierarchy.
**Prevention:** Rely on action-validator tools or schema-aware linters for GitHub Actions, not just generic YAML parsers. Visual inspection of indentation is critical when tools report "valid".
