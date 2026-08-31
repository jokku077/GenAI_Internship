"""Pydantic request/response models for the admin Q&A management endpoints."""
from pydantic import BaseModel
from typing import Optional

class AddNewQA(BaseModel):
    """Request payload for adding a new question/answer entry."""
    new_index: int
    new_question: str
    new_answer: str

class FindSimilarQA(BaseModel):
    """Request payload for a similarity search query."""
    search_query: str

class ConfirmationResponse(BaseModel):
    """Standard success/failure response returned by admin endpoints."""
    success: bool
    message: str
    index: Optional[int] = None

class UpdateQA(BaseModel):
    """Request payload for partially updating a question and/or answer."""
    question: Optional[str] = None
    answer: Optional[str] = None