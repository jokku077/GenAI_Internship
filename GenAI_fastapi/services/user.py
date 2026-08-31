"""User-facing API routes for the chatbot."""
from fastapi import APIRouter, HTTPException, Query
from models.user import QueryRequest
from handlers.response_handler import ResponseHandler

router = APIRouter()

@router.post("/chat_response")
async def get_response(query: QueryRequest):
    """Return the chatbot's best-matching answer for the user's question."""
    query = query.user_question #always remember to get the attribute of the object, not the class. (call attribute of "query" not "QueryRequest")
    answer = ResponseHandler.give_response(query)

    return {"Chat Response": answer}
