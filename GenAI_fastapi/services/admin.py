from fastapi import APIRouter, HTTPException, Query
from models.admin import ConfirmationResponse, AddNewQA, FindSimilarQA, UpdateQA
from utils.db_utils import chat_db
from handlers.embeddings_handler import EmbeddingsGenerator
from handlers.score_handler import ScoreCalculator
from handlers.db_handler import DbHandler
from utils.db_utils import DbFetcher

dbhandler = DbHandler()
router = APIRouter()

@router.put("/add_questions/{index}", response_model=ConfirmationResponse)
                                                # annotation not required, but a good practice to add to show return type
async def add_new_question(request: AddNewQA) -> ConfirmationResponse:
    result = dbhandler.add_question_handler(request)
    return result

@router.post("/find_similar_question")
async def find_similar_question(request: FindSimilarQA):
    result = dbhandler.find_similar_question_handler(request)
    return result

@router.delete("/question/{index}", response_model=ConfirmationResponse)
async def delete_question(index: int):
    result = dbhandler.delete_question_handler(index)
    return result

@router.patch("/question/{index}", response_model=ConfirmationResponse)
async def update_question(index: int, update_data: UpdateQA):
    result = dbhandler.update_question_handler(index, update_data)
    return result
