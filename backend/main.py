from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ReviewRequest, ReviewResponse
from aggregator import Aggregator

app = FastAPI(
    title="MultiReview AI",
    description="Multi-agent Python code review system",
    version="1.0.0",
)

# Allow frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://multireview-ai.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create aggregator once at startup
aggregator = Aggregator()


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "MultiReview AI"}


@app.post("/api/review", response_model=ReviewResponse)
async def review_code(request: ReviewRequest):
    response = await aggregator.run_review(request.code)
    return response
