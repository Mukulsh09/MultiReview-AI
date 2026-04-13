# MultiReview AI — Frontend

React-based frontend for the MultiReview AI multi-agent code review system.

## What it does
Paste Python code and get instant feedback from 5 specialized AI agents (correctness, security, performance, readability, style).

## Tech Stack
- React + Vite
- Tailwind CSS
- CodeMirror (syntax highlighting)
- Axios

## Components
- `CodeEditor` — Python code editor with syntax highlighting
- `SummaryPanel` — overview stats (total issues, by severity)
- `AgentCard` — per-agent results with model and response time
- `IssueItem` — individual issue with severity badge and fix suggestion
- `FilterBar` — filter by severity and agent
- `CodeAnnotations` — inline code highlighting with hover tooltips

## Running locally
```bash
npm install
npm run dev
```
App runs on http://localhost:5173

## Connecting to backend
In `src/hooks/useReview.js`, set `USE_MOCK = false` and make sure the backend is running on port 8000.