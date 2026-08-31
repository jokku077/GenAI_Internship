# Graph Report - GenAI_Internship  (2026-08-31)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 61 nodes · 116 edges · 13 communities (4 shown, 1 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f44a88c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 5

## God Nodes (most connected - your core abstractions)
1. `DbFetcher` - 11 edges
2. `DbHandler` - 11 edges
3. `ScoreCalculator` - 10 edges
4. `ConfirmationResponse` - 9 edges
5. `ResponseHandler` - 7 edges
6. `EmbeddingsGenerator` - 7 edges
7. `AddNewQA` - 5 edges
8. `FindSimilarQA` - 5 edges
9. `UpdateQA` - 5 edges
10. `ScoreChecker` - 5 edges

## Surprising Connections (you probably didn't know these)
- `get_response()` --uses--> `ResponseHandler`  [INFERRED]
  GenAI_fastapi/services/user.py → GenAI_fastapi/handlers/response_handler.py
- `DbHandler` --uses--> `ScoreCalculator`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/handlers/score_handler.py
- `ScoreCalculator` --uses--> `EmbeddingsGenerator`  [INFERRED]
  GenAI_fastapi/handlers/score_handler.py → GenAI_fastapi/handlers/embeddings_handler.py
- `DbHandler` --uses--> `DbFetcher`  [INFERRED]
  GenAI_fastapi/handlers/db_handler.py → GenAI_fastapi/utils/db_utils.py
- `add_new_question()` --uses--> `ConfirmationResponse`  [INFERRED]
  GenAI_fastapi/services/admin.py → GenAI_fastapi/models/admin.py

## Import Cycles
- None detected.

## Communities (13 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.25
Nodes (12): delete, AddNewQA, FindSimilarQA, BaseModel, UpdateQA, add_new_question(), delete_question(), find_similar_question() (+4 more)

### Community 1 - "Community 1"
Cohesion: 0.27
Nodes (4): ResponseHandler, ScoreCalculator, ScoreChecker, DbFetcher

### Community 2 - "Community 2"
Cohesion: 0.28
Nodes (6): read_root(), BaseModel, QueryRequest, get_response(), post, get

### Community 3 - "Community 3"
Cohesion: 0.43
Nodes (3): DbHandler, EmbeddingsGenerator, ConfirmationResponse

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DbFetcher` connect `Community 1` to `Community 0`, `Community 3`, `Community 5`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Why does `DbHandler` connect `Community 3` to `Community 0`, `Community 1`, `Community 5`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `ScoreCalculator` connect `Community 1` to `Community 0`, `Community 3`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `DbFetcher` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`DbFetcher` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `DbHandler` (e.g. with `EmbeddingsGenerator` and `ScoreCalculator`) actually correct?**
  _`DbHandler` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ScoreCalculator` (e.g. with `DbHandler` and `ResponseHandler`) actually correct?**
  _`ScoreCalculator` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ConfirmationResponse` (e.g. with `DbHandler` and `add_new_question()`) actually correct?**
  _`ConfirmationResponse` has 2 INFERRED edges - model-reasoned connections that need verification._