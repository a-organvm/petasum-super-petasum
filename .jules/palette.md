## 2025-05-18 - Markdown Navigation in Docs
**Learning:** In documentation-heavy repositories, "Back to Top" links targeting an auto-generated Table of Contents anchor (e.g., `#table-of-contents`) significantly improve navigation for long files.
**Action:** Always verify the existence of the specific header `## Table of Contents` when adding such links, or add it if missing (as done in `COMMANDMENTS.md`).

## 2025-05-18 - Issue Template UX
**Learning:** Linking to core framework documentation (like `LOGIC_FRAMEWORK.md`) directly within Issue Templates helps context-switch users to the expected contribution standards (Logic-First).
**Action:** Use relative paths (e.g., `../../LOGIC_FRAMEWORK.md`) in template `body` fields to ensure links work correctly from the template creation view.
