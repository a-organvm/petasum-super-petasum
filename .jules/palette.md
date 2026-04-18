## 2024-05-23 - Logic-First Framework vs. Micro-UX
**Learning:** Rigid logical frameworks can create high friction for contributors if implemented strictly as "academic" fields.
**Action:** Use Micro-UX (emojis, clear placeholders, friendly intros) to "wrapper" the logical requirements. Instead of asking for "Premises", ask for "🧠 Problem & Premises" with examples. This maintains the framework's integrity while improving the Contributor Experience (CX).

## 2024-05-23 - Relative Links in Issue Templates
**Learning:** GitHub Issue Templates in subdirectories need careful handling of relative links.
**Action:** Use `../../filename.md` for files in the root when the template is in `.github/ISSUE_TEMPLATE/` to ensure correct rendering in most contexts, or consider absolute URLs for robustness if repo URL is known.
