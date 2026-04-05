import asyncio
from models import AgentResult, ReviewSummary, ReviewResponse
from agents import (
    CorrectnessAgent,
    SecurityAgent,
    PerformanceAgent,
    ReadabilityAgent,
    StyleAgent,
)


class Aggregator:
    def __init__(self):
        self.agents = [
            CorrectnessAgent(),
            SecurityAgent(),
            PerformanceAgent(),
            ReadabilityAgent(),
            StyleAgent(),
        ]

    async def run_review(self, code: str) -> ReviewResponse:
        """Run all 5 agents concurrently and aggregate results."""

        # Run all agents in parallel
        results: list[AgentResult] = await asyncio.gather(
            *[agent.review(code) for agent in self.agents]
        )

        # Compute summary stats
        all_issues = []
        for result in results:
            all_issues.extend(result.issues)

        summary = ReviewSummary(
            total_issues=len(all_issues),
            critical=sum(1 for i in all_issues if i.severity == "critical"),
            warning=sum(1 for i in all_issues if i.severity == "warning"),
            info=sum(1 for i in all_issues if i.severity == "info"),
        )

        return ReviewResponse(summary=summary, agents=results)