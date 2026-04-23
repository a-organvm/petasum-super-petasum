## 2025-12-24 - JSON Serialization Anti-pattern in GitHub Actions
**Learning:** Found an inefficient pattern: `contains(join(fromJson(toJson(github.event.issue.labels)).*.name, ','), 'label')`. This forces unnecessary JSON serialization/deserialization and string joining.
**Action:** Replace with direct object projection: `contains(github.event.issue.labels.*.name, 'label')`.
