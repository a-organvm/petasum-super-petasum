# petasum-super-petasum

Hat on a hat, galerum super galerum, quidquid superat, ad abundantiam, et cetera.

---

## 📋 Organization-Wide Issue Tracking & Governance

This repository serves as the **central infrastructure** for the **ivviiviivvi** organization, providing:

1. **Organization-wide issue tracking** - Track issues that span multiple repositories
2. **Governance framework** - Guiding principles and commandments
3. **Standardized templates** - Consistent reporting of organization-wide concerns
4. **Automated workflows** - Alert relevant teams and manage issues efficiently
5. **Cross-repository coordination** - Facilitate collaboration across the organization

## Guiding Principles

This repository follows a set of [Organization Commandments](COMMANDMENTS.md) inspired by best practices from leading open-source projects including Semgrep, TensorFlow, and Schema.org. These principles emphasize:
- Free & open source collaboration
- Privacy & security first
- Beginner-friendly, human-readable documentation
- Quality over quantity
- Transparency and inclusivity
- Interoperability and stability

See [COMMANDMENTS.md](COMMANDMENTS.md) for the complete set of principles that guide our approach.

---

## 🚀 Quick Start

### Filing an Organization-Wide Issue

1. Go to the [Issues tab](../../issues)
2. Click **New Issue**
3. Select the appropriate template:
   - **Organization-Wide Issue** - General issues affecting multiple repos
   - **Security Concern** - Security issues requiring attention
   - **Process Improvement** - Workflow and process suggestions

### When to Use This Repository

✅ **File issues here when:**
- The issue affects 2 or more repositories
- It's an organization-wide security concern
- It requires cross-team coordination
- It's about organization-wide processes or infrastructure
- It impacts the entire organization

❌ **File in specific repositories when:**
- The issue affects only that single repository
- It's a feature request for a specific project
- It's a bug in one repository's code

---

## When to Use This (And When NOT To)

### This framework is designed for:
- **Medium-to-large organizations** (20+ repositories, 5+ teams)
- **Complex coordination needs** across multiple teams and services
- **Organizations committed to GitHub** as primary development platform
- **Teams that need structured incident response** across services
- **Engineering orgs wanting systematic cross-repo initiative tracking**

### You probably DON'T need this if:
- **Small scale**: < 10 repositories or single team
- **Simple coordination**: Slack messages and @mentions work fine
- **Single product**: One team, one main repository
- **Different tools**: Primary workflow is in Jira, ServiceNow, or PagerDuty
- **Existing solution works**: If current process is effective, don't fix what isn't broken

### Simpler alternatives to consider:
- **Small orgs**: Use basic GitHub issues with @mentions and milestones
- **Single team**: Repository-level issue templates are sufficient
- **Enterprise with existing tools**: ServiceNow, Jira, or Linear may be better integrated
- **Incident management**: Dedicated tools like PagerDuty or Opsgenie for production incidents

**Rule of thumb**: Start simple. Adopt this framework when coordination pain is felt, not preemptively.

---

## 📝 Issue Templates

### Available Templates

1. **Organization-Wide Issue** (`organization-wide-issue.yml`)
   - For general issues affecting multiple repositories
   - Includes severity classification and affected repository tracking

2. **Security Concern** (`security-concern.yml`)
   - For security issues affecting the organization
   - Prioritized handling and severity tracking

3. **Process Improvement** (`process-improvement.yml`)
   - For suggesting improvements to workflows and processes
   - Includes impact analysis and implementation considerations

### Using Templates in Other Repositories

To redirect users to this central repository from other repos, copy the template:
```
.github/ISSUE_TEMPLATE/redirect-to-org-repo.yml
```

This provides a clear path for users to file organization-wide issues in the correct location.

---

## 🏷️ Labels

The repository uses a comprehensive labeling system defined in [`.github/labels.yml`](.github/labels.yml):

### Type Labels
- `org-wide` - Issues affecting multiple repositories or the organization
- `security` - Security-related concerns
- `process` - Process and workflow improvements
- `infrastructure` - Infrastructure and tooling issues
- `documentation` - Documentation improvements
- `dependency` - Dependency management issues

### Priority Labels
- `urgent` - Requires immediate attention
- `high-priority` - High priority issue
- `medium-priority` - Medium priority issue
- `low-priority` - Low priority issue

### Status Labels
- `needs-triage` - Needs initial review
- `in-progress` - Work is in progress
- `blocked` - Progress is blocked
- `waiting-feedback` - Waiting for feedback
- `ready-to-implement` - Ready to implement

### Impact Labels
- `breaking-change` - Breaking change
- `cross-repo` - Affects multiple repositories
- `all-repos` - Affects all repositories

---

## 🤖 Automation

### Automated Workflows

#### 1. Organization-Wide Issue Notifications
**Trigger:** When an issue is labeled with `org-wide`

**Actions:**
- Posts a comment with priority and next steps
- Generates a notification summary
- Can integrate with GitHub Projects (when configured)

**Workflow:** [`.github/workflows/org-issue-notifications.yml`](.github/workflows/org-issue-notifications.yml)

#### 2. Cross-Repository Notifications
**Trigger:** When an issue is labeled with `cross-repo` or `all-repos`

**Actions:**
- Parses issue body for repository references
- Posts guidance for repository maintainers
- Provides instructions for creating linked issues

**Workflow:** [`.github/workflows/cross-repo-notifications.yml`](.github/workflows/cross-repo-notifications.yml)

---

## 💬 Discussions

For topics that don't require issue tracking, use **GitHub Discussions**:

- **Organization Discussions**: [GitHub Organization Discussions](https://github.com/orgs/ivviiviivvi/discussions)
- **Repository Discussions**: [Repository Discussions](../../discussions) (if enabled)

### When to Use Discussions vs Issues

| Use Discussions For | Use Issues For |
|---------------------|----------------|
| Questions and answers | Specific problems to solve |
| Brainstorming ideas | Tracked work items |
| General announcements | Bug reports |
| Community feedback | Feature requests with clear scope |

---

## 📊 GitHub Projects Integration

Organization-wide issues can be tracked using **GitHub Projects**:

### Setting Up a Project

1. Create an organization-level project
2. Add views for different teams or repositories
3. Configure automation to add issues with specific labels
4. Link to the project from relevant repositories

### Recommended Project Views

- **By Priority**: Group issues by priority labels
- **By Repository**: Track which repositories are affected
- **By Status**: Monitor progress of issues
- **By Team**: Assign ownership to teams

---

## 🔗 Linking Issues Across Repositories

When an organization-wide issue affects specific repositories:

### Create Linked Issues

1. Create a new issue in the affected repository
2. Reference this central issue:
   ```markdown
   Related to ivviiviivvi/petasum-super-petasum#<issue-number>
   ```
3. Update the central issue with a link to the repository-specific issue

### Benefits of Linking

- **Traceability**: Track impact across repositories
- **Context**: Provide repository-specific context
- **Notifications**: Keep stakeholders informed
- **Metrics**: Measure organization-wide impact

---

## 🛠️ Configuration for Repository Maintainers

### Adding the Redirect Template to Your Repository

Copy this file to your repository:
```bash
curl -o .github/ISSUE_TEMPLATE/redirect-to-org-repo.yml \
  https://raw.githubusercontent.com/ivviiviivvi/petasum-super-petasum/main/.github/ISSUE_TEMPLATE/redirect-to-org-repo.yml
```

Or manually copy [redirect-to-org-repo.yml](.github/ISSUE_TEMPLATE/redirect-to-org-repo.yml) to your repository's `.github/ISSUE_TEMPLATE/` directory.

---

## 📚 Best Practices

### For Issue Reporters

1. **Search First**: Check if a similar issue already exists
2. **Use Templates**: Fill out all required fields in issue templates
3. **Be Specific**: Clearly identify affected repositories and teams
4. **Provide Context**: Include relevant links, examples, and impact
5. **Follow Up**: Respond to questions and update the issue as needed

### For Issue Triagers

1. **Timely Triage**: Review new issues within 24-48 hours
2. **Apply Labels**: Use appropriate labels for categorization
3. **Assign Ownership**: Tag relevant teams or individuals
4. **Link Issues**: Create links to repository-specific issues
5. **Update Status**: Keep status labels current

### For Repository Maintainers

1. **Monitor Central Repo**: Watch this repository for relevant issues
2. **Create Links**: Link repository-specific issues to central issues
3. **Provide Updates**: Share progress on your repository's work
4. **Close When Done**: Update central issue when resolved in your repo

---

## 🤝 Contributing

This repository accepts contributions to improve the infrastructure:

- **Improve Templates**: Suggest improvements to issue templates
- **Enhance Workflows**: Propose automation improvements
- **Update Documentation**: Keep documentation current
- **Share Feedback**: Provide feedback on the process

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for contribution guidelines.

---

## 📞 Support

Need help with organization-wide issue tracking?

- **Documentation**: Read this README and related docs
- **Discussions**: Ask in [Organization Discussions](https://github.com/orgs/ivviiviivvi/discussions)
- **Issues**: File an issue in this repository
- **Contact**: Reach out to organization administrators

---

## Reference

This repository implements comprehensive patterns for organization-wide GitHub management. For detailed guidance, see:

- [COMMANDMENTS.md](COMMANDMENTS.md) - Guiding principles
- [QUICK_START.md](.github/QUICK_START.md) - Quick start guide
- [DISCUSSIONS.md](.github/DISCUSSIONS.md) - Discussion setup
- [PROJECTS.md](.github/PROJECTS.md) - Project configuration

---

## 📜 License

See [LICENSE](LICENSE) for details.
