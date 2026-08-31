"""Unit tests for the Pydantic request/response models (models.user, models.admin)."""
import pytest
from pydantic import ValidationError

from models.user import QueryRequest
from models.admin import AddNewQA, ConfirmationResponse, FindSimilarQA, UpdateQA


def test_query_request_accepts_valid_payload():
    request = QueryRequest(user_question="How do I reset my device?")
    assert request.user_question == "How do I reset my device?"


def test_query_request_requires_user_question():
    with pytest.raises(ValidationError):
        QueryRequest()


def test_add_new_qa_accepts_valid_payload():
    qa = AddNewQA(new_index=1, new_question="What is this?", new_answer="It is a test.")
    assert qa.new_index == 1
    assert qa.new_question == "What is this?"


def test_find_similar_qa_requires_search_query():
    with pytest.raises(ValidationError):
        FindSimilarQA()


def test_confirmation_response_index_defaults_to_none():
    response = ConfirmationResponse(success=True, message="done")
    assert response.index is None


def test_update_qa_allows_all_fields_omitted():
    update = UpdateQA()
    assert update.question is None
    assert update.answer is None
