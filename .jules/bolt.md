## 2024-05-23 - GHA Validation Limitations
**Learning:** `pyyaml` validation is insufficient for GitHub Actions workflows. It confirms valid YAML syntax but allows invalid GHA schema structures (like top-level `run` blocks or incorrect nesting).
**Action:** In future, cross-reference YAML validation with manual schema inspection or use a GHA-specific linter if available (e.g., `action-validator`).
