## 2024-05-23 - GitHub Actions Expression Overhead
**Learning:** Chaining `toJson`, `fromJson`, and `join` in GitHub Actions expressions (e.g., to check labels) incurs unnecessary serialization/deserialization overhead and reduces readability.
**Action:** Use object projection filters directly, e.g., `contains(github.event.issue.labels.*.name, 'target-label')`.
