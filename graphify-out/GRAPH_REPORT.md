# Graph Report - GenAI_Internship  (2026-08-31)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 133 nodes · 206 edges · 17 communities (10 shown, 6 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `533db085`
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
- Community 14
- Community 15

## God Nodes (most connected - your core abstractions)
1. `DbFetcher` - 12 edges
2. `DbHandler` - 12 edges
3. `ScoreCalculator` - 11 edges
4. `ConfirmationResponse` - 11 edges
5. `ResponseHandler` - 8 edges
6. `EmbeddingsGenerator` - 8 edges
7. `AddNewQA` - 7 edges
8. `FindSimilarQA` - 7 edges
9. `UpdateQA` - 7 edges
10. `QueryRequest` - 7 edges

## Surprising Connections (you probably didn't know these)
- `test_confirmation_response_index_defaults_to_none()` --calls--> `ConfirmationResponse`  [INFERRED]
  GenAI_fastapi/tests/test_models.py → GenAI_fastapi/models/admin.py
- `test_add_new_qa_accepts_valid_payload()` --calls--> `AddNewQA`  [INFERRED]
  GenAI_fastapi/tests/test_models.py → GenAI_fastapi/models/admin.py
- `test_find_similar_qa_requires_search_query()` --calls--> `FindSimilarQA`  [INFERRED]
  GenAI_fastapi/tests/test_models.py → GenAI_fastapi/models/admin.py
- `test_update_qa_allows_all_fields_omitted()` --calls--> `UpdateQA`  [INFERRED]
  GenAI_fastapi/tests/test_models.py → GenAI_fastapi/models/admin.py
- `get_response()` --uses--> `ResponseHandler`  [INFERRED]
  GenAI_fastapi/services/user.py → GenAI_fastapi/handlers/response_handler.py

## Import Cycles
- None detected.

## Communities (17 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (24): delete, Handlers implementing CRUD and similarity-search operations on the chatbot…, AddNewQA, FindSimilarQA, BaseModel, Pydantic request/response models for the admin Q&A management endpoints., Request payload for a similarity search query., Request payload for partially updating a question and/or answer. (+16 more)

### Community 1 - "Community 1"
Cohesion: 0.20
Nodes (13): Builds the chatbot's response by matching a query against stored Q&A embeddings., Selects the best-matching stored answer for a user query., ResponseHandler, Computes and evaluates similarity scores between a query and stored questions., Computes cosine-similarity scores between a query and stored questions., Evaluates similarity scores to decide whether a query match is usable., ScoreCalculator, ScoreChecker (+5 more)

### Community 2 - "Community 2"
Cohesion: 0.18
Nodes (10): DbHandler, Encapsulates database operations for the chatbot Q&A collection., Insert a new Q&A entry with generated embeddings. Raises: HTTPException: 409 if…, Delete the question at the given index. Raises: HTTPException: 404 if no…, Update the question and/or answer at the given index. Regenerates embeddings…, EmbeddingsGenerator, Return the embedding vector for the given text query., Generates embedding vectors via the configured Gemini embedding model. (+2 more)

### Community 3 - "Community 3"
Cohesion: 0.17
Nodes (12): BaseModel, QueryRequest, Pydantic request models for the user chat endpoint., Request payload for the user chat endpoint., get_response(), post, User-facing API routes for the chatbot., Return the chatbot's best-matching answer for the user's question. (+4 more)

### Community 4 - "Community 4"
Cohesion: 0.18
Nodes (10): Return the index of the highest score., Return True only if every score is at or below the 0.3 relevance threshold., Return True if any two nonzero scores are exactly equal (ambiguous match)., Unit tests for handlers.score_handler (ScoreCalculator, ScoreChecker)., test_check_equal_score_detects_duplicate_nonzero_scores(), test_check_equal_score_ignores_duplicate_zero_scores(), test_check_equal_score_returns_false_for_distinct_scores(), test_check_low_score_returns_false_when_any_score_above_threshold() (+2 more)

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (7): Compute the best-matching knowledge-base answer for a user query. Returns:…, Unit tests for handlers.response_handler.ResponseHandler (with DB/embeddings…, test_give_response_returns_ambiguous_message_for_equal_scores(), test_give_response_returns_best_matching_answer(), test_give_response_returns_low_score_message_when_no_good_match(), Fetch all answers from the knowledge base, in the same document order as…, patch

### Community 6 - "Community 6"
Cohesion: 0.25
Nodes (4): Find the knowledge-base question most similar to the search query. Returns:…, Return cosine-similarity scores between the query and every stored question.…, Fetch all questions from the knowledge base, Fetch all stored question embeddings, in the same document order as…

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (3): Application configuration loaded from environment variables. Requires…, Wraps the Gemini embedding model used to vectorize chatbot questions and…, Scratch script for experimenting with Gemini embeddings and cosine similarity.…

### Community 8 - "Community 8"
Cohesion: 0.40
Nodes (4): FastAPI application entry point. Registers the user and admin routers under the…, Health-check endpoint confirming the API is running., read_root(), get

### Community 9 - "Community 9"
Cohesion: 0.50
Nodes (3): create_chatbot_knowledge_base(), One-off script that seeds the MongoDB knowledge base with sample Q&A pairs.…, Create the text index and populate the knowledge base collection with sample…

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DbFetcher` connect `Community 1` to `Community 0`, `Community 2`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `ScoreCalculator` connect `Community 1` to `Community 0`, `Community 2`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `DbHandler` connect `Community 2` to `Community 0`, `Community 1`, `Community 6`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `DbFetcher` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`DbFetcher` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `DbHandler` (e.g. with `EmbeddingsGenerator` and `ScoreCalculator`) actually correct?**
  _`DbHandler` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ScoreCalculator` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`ScoreCalculator` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `ConfirmationResponse` (e.g. with `DbHandler` and `add_new_question()`) actually correct?**
  _`ConfirmationResponse` has 3 INFERRED edges - model-reasoned connections that need verification._