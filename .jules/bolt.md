# Bolt's Journal

## 2026-01-02 - [Found broken top-level run key in workflow]
**Learning:** Python's `pyyaml` parser is permissive and will parse top-level `run` keys (which are invalid in GHA schema) as valid YAML dictionaries without error. This can mask broken workflows that effectively truncate execution.
**Action:** Always verify workflow structure against GHA schema mental model (jobs -> steps) and don't rely solely on `yaml.safe_load` for validity. Check indentation manually for top-level keys.
