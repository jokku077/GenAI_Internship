from pydantic import BaseModel
from typing import Optional

class AddNewQA(BaseModel):
    new_index: int
    new_question: str
    new_answer: str

class FindSimilarQA(BaseModel):
    search_query: str

class ConfirmationResponse(BaseModel):
    success: bool
    message: str
    index: Optional[int] = None

class UpdateQA(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None