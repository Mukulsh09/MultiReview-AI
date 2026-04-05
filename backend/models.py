from pydantic import BaseModel
from typing import Literal


class ReviewRequest(BaseModel):
    code: str
    language: str = "python"


class Issue(BaseModel):
    severity: Literal["critical", "warning", "info"]
    line: int
    message: str
    suggestion: str


class AgentResult(BaseModel):
    name: str
    model: str
    response_time_ms: int
    issues: list[Issue]


class ReviewSummary(BaseModel):
    total_issues: int
    critical: int
    warning: int
    info: int


class ReviewResponse(BaseModel):
    summary: ReviewSummary
    agents: list[AgentResult]