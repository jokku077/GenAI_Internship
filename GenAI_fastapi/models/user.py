"""Pydantic request models for the user chat endpoint."""
from pydantic import BaseModel

class QueryRequest(BaseModel):
    """Request payload for the user chat endpoint."""
    user_question: str

