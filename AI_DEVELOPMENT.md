# AI-Driven Development: ReviewSense

## Project Overview

ReviewSense is an Amazon review intelligence dashboard built to demonstrate 
production-quality AI-assisted development. It mirrors Amazon's internal seller 
analytics tools by ingesting real Amazon product review data, running sentiment 
and theme analysis through Azure OpenAI, and surfacing actionable insights through 
a customer-facing dashboard. The project was built in 28 days using an AI-driven 
development lifecycle (AI-DLC) methodology.

## What is AI-DLC?

AI-DLC means using AI at every stage of the software development lifecycle, not 
just for autocomplete. For ReviewSense, Claude was used as an architectural guide 
at every layer: database design, backend architecture, AI integration, testing 
strategy, CI/CD setup, and deployment. Claude never wrote code for me. Instead, 
Claude explained every concept before I implemented it, ensuring I understood every 
layer of the system I was building.

## Architecture Decisions Guided by AI

### Database Layer
Claude guided the decision to use a normalized 3-table PostgreSQL schema with 
foreign key constraints, JSONB for AI output storage, and NUMERIC precision for 
sentiment scores. The upsert pattern for product seeding was an AI-guided decision 
to handle duplicate data gracefully.

### Backend Layer
Claude guided the microservices architecture decision: separate ingest, analyze, 
and serve modules, each with a single responsibility. FastAPI was chosen for its 
automatic OpenAPI documentation and type validation via route parameters.

### AI Integration Layer
Claude guided the structured prompt engineering approach, prompting Azure OpenAI 
to return strict JSON with sentiment labels, confidence scores, and exactly 3 theme 
labels per review. This makes the output parseable and storable without post-processing.

### Algorithm Layer
Claude guided the decision to use a max-heap via Python's heapq.nlargest for theme 
ranking, achieving O(n log k) time complexity versus O(n log n) for a full sort. 
This directly mirrors how Amazon ranks trending products and seller feedback internally.

### Rate Limiting Layer
Claude guided the implementation of a token bucket algorithm for API rate limiting, 
the same algorithm used by Amazon API Gateway. Each client IP gets a bucket of tokens 
that refill at a fixed rate, preventing abuse while allowing short bursts.

### Testing Layer
Claude guided the unit testing strategy using pytest with unittest.mock, mocking 
all external dependencies including PostgreSQL and Azure OpenAI so tests run in 
under 2 seconds with no network calls.

### CI/CD Layer
Claude guided the GitHub Actions pipeline setup with a PostgreSQL service container 
for integration testing, GitHub repository secrets for credential management, and 
automatic deployment triggers on push to main.

## What I Built vs What Claude Explained

| Layer | Claude Explained | I Built |
|---|---|---|
| Database | Schema design, normalization, JSONB, indexes | All 3 CREATE TABLE statements |
| Backend | FastAPI routing, psycopg2, dependency injection | All endpoints and service modules |
| AI Integration | Prompt engineering, structured outputs, Azure SDK | analyze.py, ReviewProcessor class |
| Algorithms | Heap theory, Counter, time complexity | InsightEngine class |
| Rate Limiting | Token bucket algorithm, hash map design | RateLimiter class |
| Testing | Mock patterns, AAA, unit vs integration | All 5 unit tests |
| CI/CD | GitHub Actions syntax, service containers | ci.yml pipeline |
| Deployment | Cloud architecture, environment variables | Render deployment |

## Key Technical Learnings

- **Schema design first:** Defining the data contract before writing any application 
  code prevented rework and enforced data integrity at the database level.
- **Structured AI outputs:** Prompting LLMs to return strict JSON rather than 
  free-form text makes AI integration production-ready and testable.
- **Mock everything external:** Unit tests that hit real APIs are slow, expensive, 
  and flaky. Mocking external dependencies is non-negotiable for CI pipelines.
- **CORS is a contract:** API-first design requires explicit trust relationships 
  between services, enforced at the middleware layer.
- **IaC mindset:** Every environment variable, every deployment setting, every 
  infrastructure decision should be documented and reproducible.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Vite, Axios |
| Backend | Python, FastAPI, uvicorn |
| Database | PostgreSQL |
| AI | Azure OpenAI (GPT-35-turbo) |
| CI/CD | GitHub Actions |
| Hosting | Render |
| Testing | pytest, unittest.mock |

## Live URLs

- Frontend: https://reviewsense-frontend-p2qj.onrender.com
- Backend: https://reviewsense-api-ve1k.onrender.com
- GitHub: https://github.com/FransiskusAgapa/reviewsense