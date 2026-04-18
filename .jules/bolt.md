## 2024-05-23 - GitHub Actions Expression Anti-Pattern
**Learning:** GitHub Actions expressions support direct object projection (`object.*.property`), rendering `fromJson(toJson(...))` hacks for filtering arrays of objects obsolete and inefficient.
**Action:** Always check for `fromJson(toJson(...))` patterns in workflows and replace them with direct property access/projection filters.
