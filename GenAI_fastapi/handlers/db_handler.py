from utils.db_utils import chat_db
from models.admin import ConfirmationResponse, AddNewQA, FindSimilarQA, UpdateQA
from handlers.embeddings_handler import EmbeddingsGenerator
from fastapi import HTTPException
from handlers.score_handler import ScoreCalculator

from utils.db_utils import DbFetcher

class DbHandler:
    def __init__(self):
        self.collection = chat_db

    # handler to add question
                                            # this is type annotation, it is not necessary but it is a good practice to add this for clarity to specify return type
    def add_question_handler(self, request) -> ConfirmationResponse:
        # Check if index already exists
        existing = self.collection.find_one({"index": request.new_index})
        if existing:
            raise HTTPException(status_code=409, detail=f"Question with index {request.new_index} already exists")

        # Generate embeddings
        try:
            question_embedding = EmbeddingsGenerator.generate_embeddings(request.new_question)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating embeddings: {str(e)}")

        new_doc = {
            "index": request.new_index,
            "question": request.new_question,
            "answer": request.new_answer,
            "embeddings": question_embedding
        }

        result = self.collection.insert_one(new_doc)

        if not result.acknowledged:
            raise HTTPException(status_code=500, detail="Failed to add question and answer")

        return ConfirmationResponse(
            success=True,
            message=f"Question and answer successfully added at index {request.new_index}.",
            index=request.new_index,
        )

    # handler to find similar question

    def find_similar_question_handler(self, request) :
        questions = DbFetcher.fetch_questions()
        scores = ScoreCalculator.calculate_scores(request.search_query)
        max_score_index = scores.argmax(axis=0)
        similar_question = questions[max_score_index]

        result = self.collection.find_one(
            {"question": similar_question})  # getting the object containing the most similar question
        if not result:
            raise HTTPException(status_code=404, detail="Similar question not found in database")

        question_index = result.get("index")  # extracting the index
        return {
            "most_similar_question": similar_question,
            "index_of_most_similar_question": question_index,
            "score": float(scores[max_score_index])
        }

    def delete_question_handler(self, index) -> ConfirmationResponse:
        document = self.collection.find_one({"index": index})
        if not document:
            raise HTTPException(status_code=404, detail=f"Question with index {index} not found")
        result = chat_db.delete_one({"index": index})

        if result.deleted_count == 1:
            return ConfirmationResponse(message=f"Question with index: {index} successfully deleted")
        else:
            raise HTTPException(status_code=500, detail="Failed to delete the question")

    def update_question_handler(self, index, update_data) -> ConfirmationResponse:
        document = self.collection.find_one({"index": index})
        if not document:
            raise HTTPException(status_code=404, detail=f"Question with index {index} not found")

        update_fields = {}
        if update_data.question is not None:
            update_fields["question"] = update_data.question

            if "embeddings" in document:
                new_embeddings = EmbeddingsGenerator.generate_embeddings(update_data.question)  # generating embeddings for the new question
                update_fields["embeddings"] = new_embeddings

        if update_data.answer is not None:
            update_fields["answer"] = update_data.answer

        if update_fields:  # runs only if data is provided in payload
            result = self.collection.update_one(
                {"index": index},
                {"$set": update_fields}
            )

            if result.modified_count == 1:
                return ConfirmationResponse(message=f"Question with index {index} successfully updated")
            else:
                return ConfirmationResponse(message=f"No changes made to question with index {index}")
        else:
            return ConfirmationResponse(message="No update data provided")

