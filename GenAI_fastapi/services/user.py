from fastapi import APIRouter, HTTPException, Query
from models.user import QueryRequest
from handlers.response_handler import ResponseHandler

router = APIRouter()

@router.post("/chat_response")
async def get_response(query: QueryRequest):
    query = query.user_question #always remember to get the attribute of the object, not the class. (call attribute of "query" not "QueryRequest")
    answer = ResponseHandler.give_response(query)

    return {"Chat Response": answer}
