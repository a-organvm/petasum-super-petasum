# petasum-super-petasum

A template repository for organization-wide GitHub issue tracking infrastructure, built on a **logic-first framework**.

## Overview

This repository provides ready-to-use templates and workflows for managing organization-wide issues, initiatives, incidents, and RFCs across multiple repositories within a GitHub organization.

**What makes this different**: All templates, processes, and decisions are grounded in logical consistency as the foundational principle. See our [Logic-First Framework](#logic-first-framework) below.

## Logic-First Framework

This repository operates under a comprehensive logic-first framework where **logic is the supreme meta-principle** from which all other principles derive.

### Core Framework Documents

1. **[LOGIC_FRAMEWORK.md](LOGIC_FRAMEWORK.md)** - Philosophical and practical foundations
   - Why logic is self-justifying
   - How to apply logical reasoning
   - Common misconceptions addressed
   - Advanced topics (modal logic, temporal logic, etc.)

2. **[PRINCIPLE_CONFLICTS.md](PRINCIPLE_CONFLICTS.md)** - Conflict resolution matrix
   - 5-level principle hierarchy (Logic → Foundational → Operational → Community → Stability)
   - Conflict resolution matrix for 7 conflict types
   - Logic-based decision framework
   - Precedent case studies

3. **[COMMANDMENTS.md](COMMANDMENTS.md)** - Core principles with logical derivations
   - 16 principles organized by hierarchy level
   - Logical derivation for each principle
   - Application guidelines

4. **[LIFECYCLE_ROADMAP.md](LIFECYCLE_ROADMAP.md)** - Implementation roadmap
   - 6 phases from foundation to continuous evolution
   - Measurement framework
   - Risk mitigation strategies
   - Success criteria

### Quick Start with Logic-First

When making any decision about this repository or its usage:

1. **State the question clearly**: What exactly are we deciding?
2. **Identify premises**: What facts and constraints apply?
3. **Apply logical reasoning**: Which option best achieves the goal?
4. **Verify consistency**: Does this create contradictions?
5. **Document the chain**: Record your reasoning

Example from LIFECYCLE_ROADMAP.md:
```
Question: How many severity levels should incidents have?
Logic: Too few = communication loss, too many = decision paralysis
Conclusion: 3 levels balances clarity and simplicity
```

## Guiding Principles

**Meta-Principle (Level 0)**: Logic & Logical Consistency
- All organizational decisions must be logically consistent
- When principles conflict, logical analysis determines resolution
- See [PRINCIPLE_CONFLICTS.md](PRINCIPLE_CONFLICTS.md) for complete hierarchy

This repository follows a set of [Organization Commandments](COMMANDMENTS.md) inspired by best practices from leading open-source projects including Semgrep, TensorFlow, and Schema.org. All principles are logically derived and classified by hierarchy level:

**Level 1 - Foundational**: Transparency, Clarity & Precision, Verifiability
**Level 2 - Operational**: Security, Performance, Quality, Determinism, Safe Execution
**Level 3 - Community**: Open Source, Inclusivity, Beginner-Friendly, Collaboration
**Level 4 - Stability**: Backward Compatibility, Interoperability, Stability

See [COMMANDMENTS.md](COMMANDMENTS.md) for the complete set of principles with their logical derivations.

## What's Included

### Issue Templates

- **Org-wide Initiative** (`.github/ISSUE_TEMPLATE/org-wide-initiative.yml`) - For tracking cross-repo, cross-team initiatives
- **Org-wide Incident** (`.github/ISSUE_TEMPLATE/org-incident.yml`) - For tracking multi-repo or multi-team incidents
- **RFC (org-wide)** (`.github/ISSUE_TEMPLATE/org-rfc.yml`) - For proposing cross-repo changes for review

### Configuration

- **Issue Template Config** (`.github/ISSUE_TEMPLATE/config.yml`) - Configures issue template chooser with contact links

### Discussion Templates

- **Org Proposal** (`.github/DISCUSSION_TEMPLATE/org-proposal.yml`) - For early-stage proposals and RFCs

### Workflows

- **Auto-add to Project** (`.github/workflows/add-to-org-project.yml`) - Automatically adds issues labeled `org-wide` to an organization Project

## Usage

### For Organizations

1. **Option 1: Use as a centralized org-issues repository**
   - Fork or template this repository as `your-org/org-issues`
   - Configure the workflow to point to your organization Project
   - Add the required labels: `org-wide`, `initiative`, `epic`, `rfc`, `incident`, `sev-1`, `sev-2`, `sev-3`, `dependency`, `blocked`, `needs-triage`

2. **Option 2: Use in an org-level .github repository**
   - Copy the `.github` directory contents to your `your-org/.github` repository
   - The templates will be available across all repositories in your organization
   - Note: Consider visibility implications (public vs private)

### Configuration Steps

1. **Update the workflow file** (`.github/workflows/add-to-org-project.yml`):
   - Replace `https://github.com/orgs/your-org/projects/1` with your actual Project URL
   - Create a fine-grained PAT with access to the organization Project
   - Add it as a secret named `ORG_PROJECT_TOKEN`

2. **Update contact links** (`.github/ISSUE_TEMPLATE/config.yml`):
   - Replace `your-org` with your actual organization name
   - Update URLs to match your organization's resources

3. **Create labels** in your repository:
   - org-wide, initiative, epic, rfc, incident
   - sev-1, sev-2, sev-3
   - dependency, blocked, needs-triage
   - ready, in-progress, done, wontfix

## Best Practices

- **Centralized Repository**: Create a dedicated repository (e.g., `org-issues`) for organization-wide issues
- **Standardize Labels**: Use consistent labels across repositories
- **Organization Projects**: Track org-wide issues in an organization-level Project (Projects v2)
- **Cross-linking**: Reference issues across repos using `owner/repo#123` syntax
- **Triage SLAs**: Establish clear ownership and response times
- **Discussions for RFCs**: Use GitHub Discussions for early proposals, convert to issues when ready
- **Automation**: Use GitHub Actions to automate labeling, project assignment, and notifications

## Architecture Recommendations

### Recommended Setup

```
your-org/
├── .github/              # Shared templates, policies (can be public)
│   ├── ISSUE_TEMPLATE/
│   ├── CONTRIBUTING.md
│   ├── SECURITY.md
│   └── workflow-templates/
└── org-issues/           # Central org-wide issue tracking (private recommended)
    ├── .github/
    │   ├── ISSUE_TEMPLATE/  (these templates)
    │   └── workflows/       (automation workflows)
    └── docs/
```

### Visibility Considerations

- **Public .github repo**: Use for shared templates across public repositories
  - Issues here will be public
  - Not suitable for sensitive incidents or internal planning
  
- **Private org-issues repo**: Use for internal organization tracking
  - Issues remain private to organization members
  - Better for incidents, internal initiatives, and confidential planning

## Reference

### Framework Documentation

- **[LOGIC_FRAMEWORK.md](LOGIC_FRAMEWORK.md)** - Complete philosophical and practical guide
- **[PRINCIPLE_CONFLICTS.md](PRINCIPLE_CONFLICTS.md)** - Hierarchy and conflict resolution
- **[COMMANDMENTS.md](COMMANDMENTS.md)** - 16 principles with logical derivations
- **[LIFECYCLE_ROADMAP.md](LIFECYCLE_ROADMAP.md)** - Implementation and evolution roadmap
- **[SETUP.md](SETUP.md)** - Technical setup with logic-first decision examples
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute with logical reasoning

### Implementation Guidance

This repository implements organization-wide issue tracking with a logic-first approach. The `copilot-chat-response-transcript` file provides comprehensive guidance on organization-wide GitHub issue management.

**For implementing the logic-first framework in your organization**, see [LIFECYCLE_ROADMAP.md](LIFECYCLE_ROADMAP.md) for:
- 6-phase implementation plan (Foundation → Evolution)
- Measurement frameworks and success criteria
- Risk mitigation strategies
- Continuous improvement loops

## License

This template is provided as-is for use by any GitHub organization.
