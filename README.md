# GenAI Internship — Chatbot Knowledge-Base API

A FastAPI backend for a Q&A chatbot. User queries are matched against a MongoDB-backed
knowledge base using Gemini embeddings and cosine similarity, and admins can manage the
knowledge base (add/find/update/delete Q&A entries) through a separate set of endpoints.

## Tech Stack

- **API framework:** FastAPI
- **Database:** MongoDB (via `pymongo`)
- **Embeddings/LLM:** Google Gemini, via `langchain-google-genai` / `google-genai`
- **Similarity scoring:** `scikit-learn` cosine similarity, `numpy`
- **Testing:** `pytest`

## Project Structure

```
GenAI_fastapi/
├── main.py                     # FastAPI app entry point; registers /user and /admin routers
├── Agent_Streaming_API.py      # Currently empty (placeholder for a future streaming API)
├── Sandbox.py                  # Scratch script for ad-hoc embedding experiments (not runtime code)
├── requirements.txt
├── config/
│   └── __init__.py             # Loads GOOGLE_API_KEY / MONGODB_URI from the environment (.env)
├── handlers/
│   ├── db_handler.py           # DbHandler: CRUD + similarity search against the Q&A collection
│   ├── embeddings_handler.py   # EmbeddingsGenerator: wraps the Gemini embedding model
│   ├── response_handler.py     # ResponseHandler: builds the chatbot's answer to a user query
│   └── score_handler.py        # ScoreCalculator / ScoreChecker: cosine-similarity scoring
├── models/
│   ├── admin.py                # Pydantic models for admin Q&A management endpoints
│   └── user.py                 # Pydantic model for the user chat endpoint
├── services/
│   ├── admin.py                # Admin API routes (add/find/update/delete Q&A)
│   └── user.py                 # User-facing chat API route
├── utils/
│   └── db_utils.py             # MongoDB connection + DbFetcher read helpers
├── miscellaneous/
│   ├── create_knowledge_base.py  # One-off script: seeds MongoDB with sample Q&A data
│   └── db_modifications.py       # One-off migration script for backfilling document fields
└── tests/
    ├── conftest.py              # Adds app package to sys.path, stubs required env vars
    ├── test_models.py           # Tests for Pydantic request/response models
    ├── test_response_handler.py # Tests for ResponseHandler (DB/embeddings mocked)
    └── test_score_handler.py    # Tests for ScoreCalculator / ScoreChecker

graphify-out/                   # Generated knowledge-graph of this codebase (see below)
```

## Setup

1. **Create and activate a virtual environment**, then install dependencies:

   ```bash
   cd GenAI_fastapi
   pip install -r requirements.txt
   ```

   `requirements.txt` installs: `fastapi`, `numpy`, `pymongo`, `scikit-learn`, `scipy`,
   `google`, `google-genai`, `protobuf`, `langchain-google-genai`, `pytest`.

   The app also imports `python-dotenv` (in `config/__init__.py`) and needs an ASGI
   server to run (e.g. `uvicorn`) — install these as well since they are not currently
   pinned in `requirements.txt`:

   ```bash
   pip install python-dotenv uvicorn
   ```

2. **Configure environment variables.** `config/__init__.py` reads these at import
   time and raises `KeyError` if either is missing. Create a `.env` file in
   `GenAI_fastapi/`:

   ```
   GOOGLE_API_KEY=<your Gemini API key>
   MONGODB_URI=<your MongoDB connection string>
   ```

## Running the API

From the `GenAI_fastapi/` directory:

```bash
uvicorn main:app --reload
```

The API exposes:

- `GET /` — health check
- `POST /user/chat_response` — get the chatbot's best-matching answer for a question
- `PUT /admin/add_questions/{index}` — add a new Q&A entry
- `POST /admin/find_similar_question` — find the stored question most similar to a query
- `DELETE /admin/question/{index}` — delete a question by index
- `PATCH /admin/question/{index}` — partially update a question and/or answer

Interactive API docs are available at `/docs` once the server is running.

## Running Tests

From the `GenAI_fastapi/` directory:

```bash
pytest
```

Tests mock the database and embeddings calls, so no live MongoDB or Gemini API access
is required. `tests/conftest.py` stubs `GOOGLE_API_KEY` and `MONGODB_URI` so the
`config` module can be imported safely during test collection.

## Codebase Architecture Graph

This repository includes a generated knowledge graph (via the `graphify` tool)
describing the codebase's modules and their relationships:

- **[graphify-out/graph.html](graphify-out/graph.html)** — interactive HTML
  visualization. Open this file directly in a browser to explore the graph; it
  will not render inline on GitHub or in Markdown viewers since it's a standalone
  JavaScript application, not an image.
- [graphify-out/GRAPH_REPORT.md](graphify-out/GRAPH_REPORT.md) — full text report.
- [graphify-out/graph.json](graphify-out/graph.json) — raw graph data.

### Key facts (from `GRAPH_REPORT.md`)

- **110 nodes · 165 edges · 15 communities** (9 shown, 5 thin communities omitted)
- **God nodes** (most-connected core abstractions):
  1. `DbHandler` — 12 edges
  2. `DbFetcher` — 12 edges
  3. `ScoreCalculator` — 11 edges
  4. `ConfirmationResponse` — 10 edges
  5. `ResponseHandler` — 8 edges
  6. `EmbeddingsGenerator` — 8 edges
- No import cycles detected.

The graph highlights the core data flow: a user query is embedded
(`EmbeddingsGenerator`) → compared against stored question embeddings
(`ScoreCalculator`) → and resolved to an answer or a matched Q&A record
(`ResponseHandler` / `DbHandler`, backed by `DbFetcher`).
