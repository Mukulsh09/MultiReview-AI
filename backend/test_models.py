from models import ReviewRequest, Issue, AgentResult, ReviewSummary, ReviewResponse

# Test that the models work
req = ReviewRequest(code="print('hello')")
print("Request:", req.model_dump())

issue = Issue(severity="warning", line=1, message="test", suggestion="fix")
agent = AgentResult(name="correctness", model="gpt-4o", response_time_ms=1200, issues=[issue])
summary = ReviewSummary(total_issues=1, critical=0, warning=1, info=0)
resp = ReviewResponse(summary=summary, agents=[agent])
print("Response:", resp.model_dump_json(indent=2))