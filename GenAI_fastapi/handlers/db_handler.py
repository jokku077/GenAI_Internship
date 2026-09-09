"""Handlers implementing CRUD and similarity-search operations on the chatbot knowledge base."""
from typing import Any

from fastapi import HTTPException

from handlers.embeddings_handler import EmbeddingsGenerator
from handlers.score_handler import ScoreCalculator
from models.admin import AddNewQA, ConfirmationResponse, FindSimilarQA, UpdateQA
from utils.db_utils import DbFetcher, chat_db

class DbHandler:
    """Encapsulates database operations for the chatbot Q&A collection."""

    def __init__(self) -> None:
        self.collection = chat_db

    @staticmethod
    def _generate_question_embeddings(question: str) -> list[float]:
        """Generate embeddings for a question and normalize failures to HTTP 500."""
        try:
            return EmbeddingsGenerator.generate_embeddings(question)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Error generating embeddings: {exc}") from exc

    def add_question_handler(self, request: AddNewQA) -> ConfirmationResponse:
        """Insert a new Q&A entry with generated embeddings.

        Raises:
            HTTPException: 409 if `request.new_index` already exists;
                500 if embedding generation or the insert fails.
        """
        # Check if index already exists
        existing = self.collection.find_one({"index": request.new_index})
        if existing:
            raise HTTPException(status_code=409, detail=f"Question with index {request.new_index} already exists")

        question_embedding = self._generate_question_embeddings(request.new_question)

        new_doc = {
            "index": request.new_index,
            "question": request.new_question,
            "answer": request.new_answer,
            "embeddings": question_embedding,
        }

        result = self.collection.insert_one(new_doc)

        if not result.acknowledged:
            raise HTTPException(status_code=500, detail="Failed to add question and answer")

        return ConfirmationResponse(
            success=True,
            message=f"Question and answer successfully added at index {request.new_index}.",
            index=request.new_index,
        )

    def find_similar_question_handler(self, request: FindSimilarQA) -> dict[str, Any]:
        """Find the knowledge-base question most similar to the search query.

        Returns:
            dict with the matched question, its index, and the similarity score.

        Raises:
            HTTPException: 404 if the matched question is not found in the database.
        """
        questions = DbFetcher.fetch_questions()
        if not questions:
            raise HTTPException(status_code=404, detail="No questions available in database")

        scores = ScoreCalculator.calculate_scores(request.search_query)
        if len(scores) == 0:
            raise HTTPException(status_code=404, detail="No similarity scores could be computed")
        if len(scores) != len(questions):
            raise HTTPException(status_code=500, detail="Mismatch between questions and similarity scores")

        max_score_index = int(scores.argmax(axis=0))
        similar_question = questions[max_score_index]

        result = self.collection.find_one({"question": similar_question})
        if not result:
            raise HTTPException(status_code=404, detail="Similar question not found in database")

        question_index = result.get("index")
        return {
            "most_similar_question": similar_question,
            "index_of_most_similar_question": question_index,
            "score": float(scores[max_score_index]),
        }

    def delete_question_handler(self, index: int) -> ConfirmationResponse:
        """Delete the question at the given index.

        Raises:
            HTTPException: 404 if no question exists at `index`;
                500 if the delete fails.
        """
        document = self.collection.find_one({"index": index})
        if not document:
            raise HTTPException(status_code=404, detail=f"Question with index {index} not found")
        result = self.collection.delete_one({"index": index})

        if result.deleted_count == 1:
            return ConfirmationResponse(
                success=True,
                message=f"Question with index: {index} successfully deleted",
                index=index,
            )

        raise HTTPException(status_code=500, detail="Failed to delete the question")

    def update_question_handler(self, index: int, update_data: UpdateQA) -> ConfirmationResponse:
        """Update the question and/or answer at the given index.

        Regenerates embeddings only if the document already has an
        `embeddings` field and the question text is being changed. Does not
        raise if no update data is provided or nothing changed; returns a
        message instead.

        Raises:
            HTTPException: 404 if no question exists at `index`.
        """
        document = self.collection.find_one({"index": index})
        if not document:
            raise HTTPException(status_code=404, detail=f"Question with index {index} not found")

        update_fields = {}
        if update_data.question is not None:
            update_fields["question"] = update_data.question

            if "embeddings" in document:
                new_embeddings = self._generate_question_embeddings(update_data.question)
                update_fields["embeddings"] = new_embeddings

        if update_data.answer is not None:
            update_fields["answer"] = update_data.answer

        if update_fields:  # runs only if data is provided in payload
            result = self.collection.update_one(
                {"index": index},
                {"$set": update_fields},
            )

            if result.modified_count == 1:
                return ConfirmationResponse(
                    success=True,
                    message=f"Question with index {index} successfully updated",
                    index=index,
                )

            return ConfirmationResponse(
                success=True,
                message=f"No changes made to question with index {index}",
                index=index,
            )

        return ConfirmationResponse(success=True, message="No update data provided", index=index)

