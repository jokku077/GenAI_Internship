# Graph Report - GenAI_Internship  (2026-08-31)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 110 nodes · 165 edges · 15 communities (9 shown, 5 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `da5f8c05`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13

## God Nodes (most connected - your core abstractions)
1. `DbHandler` - 12 edges
2. `DbFetcher` - 12 edges
3. `ScoreCalculator` - 11 edges
4. `ConfirmationResponse` - 10 edges
5. `ResponseHandler` - 8 edges
6. `EmbeddingsGenerator` - 8 edges
7. `ScoreChecker` - 6 edges
8. `AddNewQA` - 6 edges
9. `FindSimilarQA` - 6 edges
10. `UpdateQA` - 6 edges

## Surprising Connections (you probably didn't know these)
- `ResponseHandler` --uses--> `ScoreCalculator`  [INFERRED]
  GenAI_fastapi/handlers/response_handler.py → GenAI_fastapi/handlers/score_handler.py
- `ResponseHandler` --uses--> `DbFetcher`  [INFERRED]
  GenAI_fastapi/handlers/response_handler.py → GenAI_fastapi/utils/db_utils.py
- `DbHandler` --uses--> `EmbeddingsGenerator`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/handlers/embeddings_handler.py
- `DbHandler` --uses--> `ScoreCalculator`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/handlers/score_handler.py
- `DbHandler` --uses--> `DbFetcher`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/utils/db_utils.py

## Import Cycles
- None detected.

## Communities (15 total, 5 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (17): Builds the chatbot's response by matching a query against stored Q&A embeddings., Compute the best-matching knowledge-base answer for a user query. Returns:…, Selects the best-matching stored answer for a user query., ResponseHandler, Evaluates similarity scores to decide whether a query match is usable., Return True only if every score is at or below the 0.3 relevance threshold., Return True if any two nonzero scores are exactly equal (ambiguous match)., ScoreChecker (+9 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (18): AddNewQA, FindSimilarQA, BaseModel, Pydantic request/response models for the admin Q&A management endpoints., Request payload for a similarity search query., Request payload for partially updating a question and/or answer., Request payload for adding a new question/answer entry., UpdateQA (+10 more)

### Community 2 - "Community 2"
Cohesion: 0.21
Nodes (8): DbHandler, Encapsulates database operations for the chatbot Q&A collection., Insert a new Q&A entry with generated embeddings. Raises: HTTPException: 409 if…, Delete the question at the given index. Raises: HTTPException: 404 if no…, Update the question and/or answer at the given index. Regenerates embeddings…, Return the embedding vector for the given text query., ConfirmationResponse, Standard success/failure response returned by admin endpoints.

### Community 3 - "Community 3"
Cohesion: 0.24
Nodes (8): Handlers implementing CRUD and similarity-search operations on the chatbot…, EmbeddingsGenerator, Wraps the Gemini embedding model used to vectorize chatbot questions and…, Generates embedding vectors via the configured Gemini embedding model., Computes and evaluates similarity scores between a query and stored questions., Computes cosine-similarity scores between a query and stored questions., Return the index of the highest score., ScoreCalculator

### Community 4 - "Community 4"
Cohesion: 0.22
Nodes (6): Find the knowledge-base question most similar to the search query. Returns:…, Return cosine-similarity scores between the query and every stored question.…, DbFetcher, Read-only helpers for pulling questions, answers, and embeddings from the…, Fetch all questions from the knowledge base, Fetch all stored question embeddings, in the same document order as…

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (5): Application configuration loaded from environment variables. Requires…, Scratch script for experimenting with Gemini embeddings and cosine similarity.…, connect_db(), Database connection and read helpers for the chatbot knowledge base., Open a MongoDB connection and return the chatbot knowledge-base collection.

### Community 6 - "Community 6"
Cohesion: 0.40
Nodes (4): FastAPI application entry point. Registers the user and admin routers under the…, Health-check endpoint confirming the API is running., read_root(), get

### Community 7 - "Community 7"
Cohesion: 0.50
Nodes (3): create_chatbot_knowledge_base(), One-off script that seeds the MongoDB knowledge base with sample Q&A pairs.…, Create the text index and populate the knowledge base collection with sample…

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (3): delete, delete_question(), Delete the question at the given index.

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DbFetcher` connect `Community 4` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 5`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `DbHandler` connect `Community 2` to `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `ScoreCalculator` connect `Community 3` to `Community 0`, `Community 1`, `Community 2`, `Community 4`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `DbHandler` (e.g. with `EmbeddingsGenerator` and `ScoreCalculator`) actually correct?**
  _`DbHandler` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DbFetcher` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`DbFetcher` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ScoreCalculator` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`ScoreCalculator` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ConfirmationResponse` (e.g. with `DbHandler` and `add_new_question()`) actually correct?**
  _`ConfirmationResponse` has 2 INFERRED edges - model-reasoned connections that need verification._