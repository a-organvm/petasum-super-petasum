# Principle Conflicts: Resolution Framework

This document provides a practical framework for resolving conflicts between the principles outlined in [COMMANDMENTS.md](COMMANDMENTS.md). In complex organizational settings, principles sometimes pull in opposite directions. This framework helps navigate those tensions.

---

## Philosophy: Principles are Tools, Not Rules

Principles should guide judgment, not replace it. When principles conflict, the goal is not to find "the right answer" but to make a **well-reasoned decision** that:
1. Considers context
2. Acknowledges trade-offs
3. Documents rationale
4. Can be adjusted if consequences prove problematic

---

## Conflict Resolution Matrix

### Security/Privacy vs. Transparency/Openness

| Dimension | Security/Privacy Favored | Balanced Approach | Transparency Favored |
|-----------|---------------------------|-------------------|----------------------|
| **When** | Active security incidents, unpatched vulnerabilities, personal data, legal compliance | General org-wide initiatives, technical RFCs, post-incident reviews | Process improvements, architectural decisions, retrospectives |
| **Implementation** | Private repo only, restricted access, sanitized summaries | Private during investigation, public after remediation | Public by default, private only when justified |
| **Responsible Party** | Security team + Legal | Engineering leadership | Project maintainer |
| **Example** | Security vulnerability tracking | Incident post-mortems | API versioning RFC |

**Resolution Hierarchy**: Security and Privacy are **zero-compromise** when:
- Legal/regulatory requirements mandate it
- Active threat or vulnerability exists
- Personal or confidential data involved

Otherwise, **default to transparency** with privacy safeguards.

---

### Performance/Speed vs. Quality/Thoroughness

| Dimension | Performance Favored | Balanced Approach | Quality Favored |
|-----------|---------------------|-------------------|-----------------|
| **When** | SEV-1 incidents, time-critical decisions, high-frequency processes | Standard org-wide initiatives, RFCs with clear scope | Architectural decisions, security reviews, compliance changes |
| **Implementation** | Minimal required fields, async updates, lightweight process | Core required fields + optional detail | Comprehensive documentation, thorough review |
| **Responsible Party** | On-call/incident commander | Project owner | Tech lead + architect |
| **Example** | Incident started template (2 fields) | Initiative template (8 fields) | Security audit checklist (30 items) |

**Resolution Test**: "Is the value of additional detail worth 2x the time cost?"

If yes → quality. If no → performance.

---

### Flexibility/Customization vs. Determinism/Consistency

| Dimension | Flexibility Favored | Balanced Approach | Determinism Favored |
|-----------|---------------------|-------------------|---------------------|
| **When** | Highly specialized teams, experimental projects, edge cases | Standard org-wide work with some team variance | Cross-team coordination, automation dependencies, compliance |
| **Implementation** | Custom templates, optional fields, team-specific workflows | Standardized core + optional extensions | Strict required fields, enforced validation |
| **Responsible Party** | Individual teams | Engineering leadership | Platform/tools team |
| **Example** | Hardware team custom fields | Initiative template with optional sections | Automated project assignment |

**Resolution Framework**:
- **Standardize interfaces** (how systems talk to each other)
- **Customize implementations** (how teams do their work)

---

### Beginner-Friendly vs. Power-User Efficiency

| Dimension | Beginner-Friendly Favored | Balanced Approach | Power-User Favored |
|-----------|---------------------------|-------------------|--------------------|
| **When** | Onboarding docs, rare operations, broad audience | Daily-use templates, common tasks | Advanced features, automation, experienced users |
| **Implementation** | Verbose labels, inline help text, examples | Clear labels, linked help docs | Terse labels, keyboard shortcuts, CLI |
| **Responsible Party** | Documentation team | Product/UX | Power users + advocates |
| **Example** | "Org-wide Initiative (cross-repo project)" | "Org-wide Initiative" | CLI: `gh issue create --template=init` |

**Resolution Principle**: **Progressive disclosure**
- Beginner-friendly by default
- Power-user features available but not required
- Documentation serves both audiences

---

## 7-Level Priority Hierarchy

This hierarchy helps resolve principle conflicts when multiple principles apply:

### Level 1: Legal & Regulatory Compliance 🔴
**Why Highest**: Non-negotiable external requirements.
**Trumps**: All other principles.
**Examples**: GDPR, SOC2, HIPAA, export controls.
**Decision Maker**: Legal + Compliance team.

### Level 2: Security & Privacy 🔴
**Why High**: Protects users and organization from harm.
**Trumps**: Transparency, flexibility, performance, convenience.
**Examples**: Vulnerability disclosure, data protection, authentication.
**Decision Maker**: Security team (can be overridden only by Level 1).

### Level 3: Operational Integrity 🟠
**Why High**: Keeps systems running, prevents incidents.
**Trumps**: Feature velocity, customization, documentation completeness.
**Examples**: Incident response, disaster recovery, monitoring.
**Decision Maker**: Oncall + SRE team.

### Level 4: Quality & Correctness 🟡
**Why Mid-High**: Wrong is worse than slow or incomplete.
**Trumps**: Performance, quantity of features, time to market.
**Examples**: Data integrity, correctness of financial calculations, architectural soundness.
**Decision Maker**: Tech lead + architect.

### Level 5: User Experience & Accessibility 🟢
**Why Mid**: Inclusivity and usability matter for adoption.
**Trumps**: Developer convenience, aesthetic preferences.
**Examples**: Screen reader support, clear documentation, intuitive workflows.
**Decision Maker**: UX lead + accessibility champion.

### Level 6: Developer Productivity & Performance 🔵
**Why Mid-Low**: Enables teams to move quickly.
**Trumps**: Documentation completeness, process thoroughness.
**Examples**: Fast CI/CD, minimal required fields, keyboard shortcuts.
**Decision Maker**: Engineering manager + developer advocate.

### Level 7: Aesthetic & Stylistic Preferences 🟣
**Why Lowest**: Subjective, low-impact.
**Trumps**: Nothing.
**Examples**: Label colors, emoji usage, documentation tone.
**Decision Maker**: Project maintainer (open to bikeshedding).

---

## Precedent Case Studies

These real (or realistic) scenarios establish precedent for future decisions:

### Case Study 1: "The Public Incident Debate"

**Scenario**: Engineering team wants to document major outage in public org-issues repo (transparency). Security team says private only (security). Customer success team wants public for customer trust (transparency).

**Conflicting Principles**:
- Commandment #2: Privacy & Security First
- Commandment #10: Transparency

**Resolution**:
1. **Immediate response** (0-4 hours): Private incident issue for mitigation (Security wins)
2. **Active investigation** (4-48 hours): Private repo, sanitized status page updates (Security wins with transparency mitigation)
3. **Post-incident** (48+ hours): Public sanitized post-mortem (Transparency wins after security concerns addressed)

**Precedent Established**:
- Security concerns are time-boxed, not permanent
- Transparency can be delayed, not denied
- Public post-mortems are standard after remediation
- Customer-facing impacts get status page updates even if issue is private

**Decision Maker**: Security team during incident, Engineering leadership for post-mortem.

---

### Case Study 2: "The 30-Field Initiative Template"

**Scenario**: Product management team proposes adding 20 more fields to initiative template for better tracking (quality). Engineering teams complain it takes 45 minutes to create an initiative (performance).

**Conflicting Principles**:
- Commandment #7: Performance Matters
- Commandment #8: Quality Over Quantity

**Resolution**:
1. **Measured current state**: Average 15 minutes to fill existing template
2. **Tested proposed state**: 45 minutes for 30-field version (3x slower)
3. **Evaluated quality gain**: Could not demonstrate 3x better outcomes
4. **Compromise**: Added 3 new optional fields, kept 8 required fields
5. **Created power-user version**: Separate detailed template for complex initiatives

**Precedent Established**:
- Performance degradation requires proportional quality improvement to justify
- Rule of thumb: 2x time cost requires 2x+ demonstrated value
- Optional fields preferred over required fields when benefit is unclear
- Multiple template tiers acceptable (simple vs. detailed)

**Decision Maker**: Engineering leadership with input from both teams.

---

### Case Study 3: "The Hardware Team Custom Template"

**Scenario**: Hardware engineering team wants custom initiative template with 10 hardware-specific fields (flexibility). Platform team says this breaks automation and creates inconsistency (determinism).

**Conflicting Principles**:
- Commandment #3: Support Many Use Cases (flexibility)
- Commandment #5: Deterministic & Reliable

**Resolution**:
1. **Identified automation dependencies**: Workflows only use 5 core fields
2. **Standardized interface**: 5 core fields must be present and named consistently
3. **Allowed customization**: Hardware team can add additional fields
4. **Naming convention**: Custom fields prefixed with "hw-" to prevent collisions
5. **Documentation requirement**: Custom templates must document their extensions

**Precedent Established**:
- **"Standardize interfaces, customize implementations"**
- Core fields for automation are non-negotiable
- Extension points allow specialization without breaking consistency
- Namespacing prevents conflicts

**Decision Maker**: Platform team sets core interface, individual teams customize within those constraints.

---

### Case Study 4: "The Token Expiration Incident"

**Scenario**: ORG_PROJECT_TOKEN expired after 90 days (security). Workflow silently failed for 2 weeks. Critical initiative not tracked in project board (reliability).

**Conflicting Principles**:
- Commandment #2: Security (short-lived tokens)
- Commandment #5: Deterministic & Reliable (always works)

**Resolution**:
1. **Immediate fix**: Manual token refresh, added calendar reminder
2. **Root cause**: No monitoring, no expiration warnings
3. **Long-term fix**:
   - Added workflow to check token validity weekly
   - Alert 14 days before expiration
   - Escalate if workflow fails 3x
   - Document token lifecycle in SETUP.md
4. **Considered alternatives**: GitHub App (doesn't expire) vs PAT (more flexible)
5. **Decision**: Stick with PAT, add robust monitoring

**Precedent Established**:
- Security measures (token expiration) must include operational safeguards (monitoring)
- Silent failures are unacceptable
- "It works or it alerts" - no silent degradation
- Document lifecycle management for time-limited credentials

**Decision Maker**: SRE team + Platform team.

---

### Case Study 5: "The SEV-1 Template Paradox"

**Scenario**: During database outage (SEV-1), on-call engineer spent 12 minutes filling out incident template (performance). CEO asked why engineers were documenting instead of fixing (quality of response).

**Conflicting Principles**:
- Commandment #7: Performance Matters (fast action)
- Commandment #10: Transparency (document everything)
- Operational Integrity: Fix it now

**Resolution**:
1. **Created two-phase process**:
   - **Phase 1 (During incident)**: Minimal 2-field template ("SEV-1 started: [title]")
   - **Phase 2 (After mitigation)**: Convert to full incident template
2. **Established "break glass" protocol**: During SEV-1, skip process if it slows response
3. **Post-incident requirement**: Full documentation within 24 hours of resolution
4. **Training**: "Fix first, document after" for critical incidents

**Precedent Established**:
- **Operational integrity > process compliance during active incidents**
- Process can be deferred, not skipped
- Lightweight capture during crisis, thorough documentation after
- Time-to-mitigation is the primary SEV-1 metric

**Decision Maker**: Incident commander (on-call engineer) during incident, no approval needed.

---

## Escalation Protocols

When conflicts cannot be resolved using this framework:

### Step 1: Initial Assessment (Self-Service)
**Who**: Anyone encountering the conflict
**Time**: 15 minutes
**Action**:
1. Review this document
2. Identify which principles are in tension
3. Check if precedent case studies apply
4. Consult priority hierarchy

**Outcome**: 70% of conflicts resolved here.

---

### Step 2: Team Discussion (Collaborative)
**Who**: Affected teams + project owner
**Time**: 1-2 days
**Action**:
1. Create issue labeled `principle-conflict`
2. Document the conflict clearly
3. Tag relevant stakeholders
4. Async discussion in issue comments
5. Timebox to 48 hours

**Outcome**: 20% of conflicts resolved here.

---

### Step 3: Engineering Leadership (Arbitration)
**Who**: Engineering manager + tech lead + relevant specialists (security, legal, etc.)
**Time**: 1 week
**Action**:
1. Escalate issue to engineering leadership
2. Synchronous meeting with decision-makers
3. Document trade-offs explicitly
4. Make decision with clear rationale
5. Update this document with new precedent if applicable

**Outcome**: 9% of conflicts resolved here.

---

### Step 4: Executive Decision (Rare)
**Who**: CTO or equivalent
**Time**: 2 weeks
**Action**:
1. Create RFC document with full context
2. Present to executive leadership
3. Executive makes final call
4. Decision is binding
5. Becomes new precedent

**Outcome**: <1% of conflicts require this level.

---

## Amending This Framework

This document is a living guide and should evolve as we learn.

### Amendment Process

1. **Propose**: Create issue labeled `principle-amendment`
2. **Discuss**: Minimum 1 week feedback period
3. **Consensus**: No strong unresolved objections
4. **Document**: Update this file via PR
5. **Announce**: Communicate change to organization
6. **Review**: Quarterly retrospective on amendments

### Who Can Propose Amendments?
Anyone in the organization.

### Who Approves Amendments?
- Minor clarifications: Project maintainer
- New precedent case studies: Engineering leadership
- Changes to hierarchy or framework: Consensus (Engineering leadership + 3+ team representatives)

---

## Quick Reference: Decision Tree

```
[Principle Conflict]
        |
        ↓
    [Legal/Compliance involved?]
     Yes → Legal decides
     No → Continue
        |
        ↓
    [Active security risk?]
     Yes → Security decides
     No → Continue
        |
        ↓
    [Active SEV-1 incident?]
     Yes → Incident commander decides (fix first, process after)
     No → Continue
        |
        ↓
    [Precedent case study applies?]
     Yes → Follow precedent
     No → Continue
        |
        ↓
    [Priority hierarchy clear winner?]
     Yes → Higher level wins
     No → Continue
        |
        ↓
    [Escalate to team discussion]
     Resolved? → Document decision
     Not resolved? → Engineering leadership
```

---

## Principles Compatibility Matrix

Quick reference for which principles are typically compatible (✅), require trade-offs (⚠️), or frequently conflict (⚠️🔴):

|   | Free/Open | Privacy | Flexible | Beginner | Deterministic | Safe | Performance | Quality | Community | Transparent | Compat | Security | Interop | Clarity | Inclusive | Stable |
|---|-----------|---------|----------|----------|---------------|------|-------------|---------|-----------|-------------|--------|----------|---------|---------|-----------|--------|
| **Free/Open** | - | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Privacy** | ⚠️ | - | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️🔴 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Flexible** | ✅ | ⚠️ | - | ⚠️ | ⚠️🔴 | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| **Beginner** | ✅ | ✅ | ⚠️ | - | ✅ | ✅ | ⚠️🔴 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Deterministic** | ✅ | ✅ | ⚠️🔴 | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Safe** | ✅ | ✅ | ⚠️ | ✅ | ✅ | - | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Performance** | ✅ | ⚠️ | ⚠️ | ⚠️🔴 | ✅ | ⚠️ | - | ⚠️🔴 | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| **Quality** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️🔴 | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Community** | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Transparent** | ✅ | ⚠️🔴 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | - | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Compat** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Security** | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ | - | ✅ | ✅ | ✅ | ✅ |

Legend:
- ✅ Typically compatible
- ⚠️ Requires trade-offs
- ⚠️🔴 Frequently conflicts (use framework above)

---

## Living Document Commitment

This framework will be reviewed and updated:
- **Quarterly**: Light review of relevance
- **Annually**: Deep review with precedent case study refresh
- **As needed**: When new conflicts emerge that aren't covered

Last updated: 2025-11-01
Next scheduled review: 2026-02-01 (Q1 2026)

---

*This framework is designed to help us make better decisions when principles pull in different directions. It's a guide, not a rule book. Use judgment, document rationale, and learn from outcomes.*
