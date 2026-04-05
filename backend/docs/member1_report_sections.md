# Member 1 Report Sections

## Technical Implementation
MultiReview AI uses a multi-agent architecture built on FastAPI, where five specialized AI agents analyze Python code concurrently across distinct review dimensions. When a user submits code through the /api/review endpoint, the backend dispatches it to all five agents simultaneously using asyncio.gather(), significantly reducing total review time compared to sequential execution.

Each agent follows a common design pattern through a shared BaseAgent class that handles prompt loading, LLM communication, response parsing, timing, and error handling.

## Agent Design and Model Selection

| Agent | LLM | Provider | Why This Model |
|-------|-----|----------|---------------|
| Correctness | Gemini 2.0 Flash | Google | Strong logical reasoning |
| Security | Gemini 2.0 Flash | Google | Broad vulnerability pattern knowledge |
| Readability | Gemini 2.0 Flash Lite | Google | Fast, sufficient for readability checks |
| Performance | Qwen 2.5 Coder 32B | HuggingFace | Code-specialized, excellent at algorithmic analysis |
| Style | Llama 3.1 8B | HuggingFace | Fast PEP 8 checking |

## Prompt Engineering
Each prompt uses a structured format: role definition, scope, exclusion rules, output format (strict JSON), and severity guide. The most critical design decision was adding explicit exclusion rules to prevent agents from flagging issues outside their dimension.
