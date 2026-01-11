## 2024-05-23 - GitHub Actions Schema vs YAML Validity
**Learning:** `pyyaml` only validates YAML syntax, not GitHub Actions schema. A file can be valid YAML but broken for Actions (e.g., `run:` at root).
**Action:** When validating workflows, manual inspection of schema correctness is necessary in addition to syntax checking.

## 2024-05-23 - GitHub Actions Expression Performance
**Learning:** `contains(join(fromJson(toJson(obj)).*.prop, ','), 'val')` is a massive performance anti-pattern compared to `contains(obj.*.prop, 'val')`.
**Action:** Always prefer direct object projection and `contains` over JSON serialization/deserialization.
