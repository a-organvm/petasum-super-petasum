## 2024-03-24 - Workflow Step Consolidation
**Learning:** In GitHub Actions, consolidating multiple shell steps into a single `actions/github-script` step significantly reduces container start-up overhead and context switching time.
**Action:** Always check if sequences of simple shell calculations and conditional logic can be moved into a JS block within the workflow.
