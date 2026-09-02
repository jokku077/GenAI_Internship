# Graph Report - GenAI_Internship  (2026-09-02)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 133 nodes · 202 edges · 16 communities (9 shown, 6 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 19 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a7968595`
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

## God Nodes (most connected - your core abstractions)
1. `DbHandler` - 12 edges
2. `ConfirmationResponse` - 11 edges
3. `DbFetcher` - 10 edges
4. `ScoreCalculator` - 9 edges
5. `ResponseHandler` - 8 edges
6. `QueryRequest` - 7 edges
7. `AddNewQA` - 7 edges
8. `FindSimilarQA` - 7 edges
9. `UpdateQA` - 7 edges
10. `EmbeddingsGenerator` - 6 edges

## Surprising Connections (you probably didn't know these)
- `test_confirmation_response_index_defaults_to_none()` --calls--> `ConfirmationResponse`  [INFERRED]
  GenAI_fastapi/tests/test_models.py → GenAI_fastapi/models/admin.py
- `DbHandler` --uses--> `EmbeddingsGenerator`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/handlers/embeddings_handler.py
- `DbHandler` --uses--> `ScoreCalculator`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/handlers/score_handler.py
- `ResponseHandler` --uses--> `ScoreCalculator`  [INFERRED]
  GenAI_fastapi/handlers/response_handler.py → GenAI_fastapi/handlers/score_handler.py
- `ResponseHandler` --uses--> `ScoreChecker`  [INFERRED]
  GenAI_fastapi/handlers/response_handler.py → GenAI_fastapi/handlers/score_handler.py

## Import Cycles
- None detected.

## Communities (16 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.13
Nodes (16): delete, Application configuration loaded from environment variables. Requires…, Handlers implementing CRUD and similarity-search operations on the chatbot…, EmbeddingsGenerator, Wraps the Gemini embedding model used to vectorize chatbot questions and…, Generates embedding vectors via the configured Gemini embedding model., Computes and evaluates similarity scores between a query and stored questions., Computes cosine-similarity scores between a query and stored questions. (+8 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (15): Builds the chatbot's response by matching a query against stored Q&A embeddings., Selects the best-matching stored answer for a user query., ResponseHandler, BaseModel, QueryRequest, Pydantic request models for the user chat endpoint., Request payload for the user chat endpoint., get_response() (+7 more)

### Community 2 - "Community 2"
Cohesion: 0.14
Nodes (16): AddNewQA, FindSimilarQA, BaseModel, Pydantic request/response models for the admin Q&A management endpoints., Request payload for a similarity search query., Request payload for partially updating a question and/or answer., Request payload for adding a new question/answer entry., UpdateQA (+8 more)

### Community 3 - "Community 3"
Cohesion: 0.16
Nodes (11): DbHandler, Encapsulates database operations for the chatbot Q&A collection., Insert a new Q&A entry with generated embeddings. Raises: HTTPException: 409 if…, Delete the question at the given index. Raises: HTTPException: 404 if no…, Update the question and/or answer at the given index. Regenerates embeddings…, Return the embedding vector for the given text query., ConfirmationResponse, Standard success/failure response returned by admin endpoints. (+3 more)

### Community 4 - "Community 4"
Cohesion: 0.16
Nodes (12): Return the index of the highest score., Evaluates similarity scores to decide whether a query match is usable., Return True only if every score is at or below the 0.3 relevance threshold., Return True if any two nonzero scores are exactly equal (ambiguous match)., ScoreChecker, Unit tests for handlers.score_handler (ScoreCalculator, ScoreChecker)., test_check_equal_score_detects_duplicate_nonzero_scores(), test_check_equal_score_ignores_duplicate_zero_scores() (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.23
Nodes (9): Compute the best-matching knowledge-base answer for a user query. Returns:…, Partially update the question and/or answer at the given index., update_question(), Unit tests for handlers.response_handler.ResponseHandler (with DB/embeddings…, test_give_response_returns_ambiguous_message_for_equal_scores(), test_give_response_returns_best_matching_answer(), test_give_response_returns_low_score_message_when_no_good_match(), Fetch all answers from the knowledge base, in the same document order as… (+1 more)

### Community 6 - "Community 6"
Cohesion: 0.25
Nodes (4): Find the knowledge-base question most similar to the search query. Returns:…, Return cosine-similarity scores between the query and every stored question.…, Fetch all questions from the knowledge base, Fetch all stored question embeddings, in the same document order as…

### Community 7 - "Community 7"
Cohesion: 0.40
Nodes (4): FastAPI application entry point. Registers the user and admin routers under the…, Health-check endpoint confirming the API is running., read_root(), get

### Community 8 - "Community 8"
Cohesion: 0.50
Nodes (3): create_chatbot_knowledge_base(), One-off script that seeds the MongoDB knowledge base with sample Q&A pairs.…, Create the text index and populate the knowledge base collection with sample…

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DbFetcher` connect `Community 1` to `Community 0`, `Community 3`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Why does `ScoreCalculator` connect `Community 0` to `Community 1`, `Community 3`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `DbHandler` connect `Community 3` to `Community 0`, `Community 1`, `Community 6`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `DbHandler` (e.g. with `EmbeddingsGenerator` and `ScoreCalculator`) actually correct?**
  _`DbHandler` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `ConfirmationResponse` (e.g. with `DbHandler` and `add_new_question()`) actually correct?**
  _`ConfirmationResponse` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `DbFetcher` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`DbFetcher` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ScoreCalculator` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`ScoreCalculator` has 2 INFERRED edges - model-reasoned connections that need verification._