## 2024-05-23 - GitHub Actions Expression Anti-Pattern
**Learning:** Avoid `fromJson(toJson(...))` round-trips in GitHub Actions expressions. This pattern is often used to manipulate objects but adds unnecessary processing overhead.
**Action:** Use direct object projection (e.g., `github.event.issue.labels.*.name`) combined with `contains()` for cleaner, faster checks.
