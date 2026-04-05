import asyncio
from aggregator import Aggregator

TEST_CODE = """
import os

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    password = "admin123"
    result = []
    for i in range(len(result)):
        x = result[i]
        print(x)
    return result
"""

async def main():
    agg = Aggregator()
    response = await agg.run_review(TEST_CODE)

    print(f"\n{'='*60}")
    print(f"REVIEW SUMMARY")
    print(f"{'='*60}")
    print(f"Total issues: {response.summary.total_issues}")
    print(f"Critical: {response.summary.critical}")
    print(f"Warning: {response.summary.warning}")
    print(f"Info: {response.summary.info}")

    for agent in response.agents:
        print(f"\n--- {agent.name} ({agent.model}) [{agent.response_time_ms}ms] ---")
        if not agent.issues:
            print("  No issues found.")
        for issue in agent.issues:
            print(f"  [{issue.severity}] Line {issue.line}: {issue.message}")

asyncio.run(main())