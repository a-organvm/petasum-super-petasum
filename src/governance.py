"""Cross-organ governance checks and compliance reporting."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class HealthCheck:
    """Result of a single health check."""
    name: str
    passed: bool
    message: str
    organ: str = ""


@dataclass
class GovernanceReport:
    """Aggregated governance health report."""
    checks: list[HealthCheck] = field(default_factory=list)

    def add_check(self, check: HealthCheck) -> None:
        self.checks.append(check)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def pass_count(self) -> int:
        return sum(1 for c in self.checks if c.passed)

    @property
    def fail_count(self) -> int:
        return sum(1 for c in self.checks if not c.passed)

    def by_organ(self, organ: str) -> list[HealthCheck]:
        return [c for c in self.checks if c.organ == organ]

    def summary(self) -> str:
        total = len(self.checks)
        if total == 0:
            return "No checks performed"
        pct = (self.pass_count / total) * 100
        status = "PASS" if self.passed else "FAIL"
        return f"{status}: {self.pass_count}/{total} checks passed ({pct:.0f}%)"


def check_ci_health(repos: list[dict]) -> list[HealthCheck]:
    """Check CI health across repositories."""
    checks = []
    for repo in repos:
        name = repo.get("name", "unknown")
        org = repo.get("org", "")
        ci_status = repo.get("ci_conclusion", "unknown")
        passed = ci_status == "success"
        checks.append(HealthCheck(
            name=f"ci-{name}",
            passed=passed,
            message=f"CI {'passing' if passed else 'failing'} for {name}",
            organ=org,
        ))
    return checks


def check_documentation_coverage(repos: list[dict]) -> list[HealthCheck]:
    """Check documentation coverage across repositories."""
    checks = []
    for repo in repos:
        name = repo.get("name", "unknown")
        org = repo.get("org", "")
        doc_status = repo.get("documentation_status", "EMPTY")
        passed = doc_status in ("DEPLOYED", "ACTIVE")
        checks.append(HealthCheck(
            name=f"docs-{name}",
            passed=passed,
            message=f"Docs {'deployed' if passed else doc_status.lower()} for {name}",
            organ=org,
        ))
    return checks
