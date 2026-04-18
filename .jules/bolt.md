## 2024-05-22 - GitHub Actions Expression Anti-Pattern
**Learning:** Found inefficient GitHub Actions expression pattern `contains(join(fromJson(toJson(...)).*.name, ','), 'value')` which performs unnecessary JSON serialization/deserialization.
**Action:** Use object filters directly: `contains(github.event.issue.labels.*.name, 'value')`. This is faster and more readable.
