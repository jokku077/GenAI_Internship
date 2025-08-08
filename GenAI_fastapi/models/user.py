from pydantic import BaseModel

class QueryRequest(BaseModel):
    user_question: str

