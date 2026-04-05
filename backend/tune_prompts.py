import asyncio
import json
from aggregator import Aggregator

SNIPPETS = {
    "sql_injection": '''
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query)
''',
    "performance_issue": '''
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates
''',
    "readability_issue": '''
def f(x, y, z):
    a = x * 2
    b = y + z
    if a > b:
        if z > 0:
            if x != y:
                return a - b + z
            else:
                return b
        else:
            return a
    else:
        return b - a
''',
    "clean_code": '''
def calculate_average(numbers: list[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
''',
}

async def main():
    agg = Aggregator()
    for name, code in SNIPPETS.items():
        print(f"\n{'='*60}")
        print(f"SNIPPET: {name}")
        print(f"{'='*60}")
        response = await agg.run_review(code)
        print(f"Total: {response.summary.total_issues} issues")
        for agent in response.agents:
            print(f"  {agent.name}: {len(agent.issues)} issues ({agent.response_time_ms}ms)")
            for issue in agent.issues:
                print(f"    [{issue.severity}] L{issue.line}: {issue.message}")

asyncio.run(main())