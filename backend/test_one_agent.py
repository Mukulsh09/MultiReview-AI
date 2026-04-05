import asyncio
from agents.correctness import CorrectnessAgent

TEST_CODE = """
def find_max(numbers):
    max_val = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val
"""

async def main():
    agent = CorrectnessAgent()
    result = await agent.review(TEST_CODE)
    print(f"Agent: {result.name}")
    print(f"Model: {result.model}")
    print(f"Time: {result.response_time_ms}ms")
    print(f"Issues found: {len(result.issues)}")
    for issue in result.issues:
        print(f"  [{issue.severity}] Line {issue.line}: {issue.message}")
        print(f"    Fix: {issue.suggestion}")

asyncio.run(main())