## 2024-10-24 - [Broken YAML and Injection Risks]
**Vulnerability:** Found a workflow with broken YAML structure (floating env/run blocks) and critical script injection vulnerabilities where user labels were interpolated directly into shell and JS scripts.
**Learning:** Copy-paste errors can leave blocks floating outside steps, and standard linting might miss them if not rigorous. Using ${{ ... }} in 'run' or 'script' blocks is almost always a security risk when handling user input.
**Prevention:** Always validate YAML structure. Use environment variables for shell scripts and context/process.env for JS scripts. Never interpolate user input directly.
