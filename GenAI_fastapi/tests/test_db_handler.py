"""Unit tests for handlers.db_handler.DbHandler with mocked DB and embeddings."""
from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException

from handlers.db_handler import DbHandler
from models.admin import AddNewQA


def test_add_question_handler_returns_500_without_leaking_embedding_exception():
    handler = DbHandler()
    mock_collection = MagicMock()
    mock_collection.find_one.return_value = None
    handler.collection = mock_collection

    request = AddNewQA(new_index=1, new_question="new question", new_answer="new answer")

    with patch("handlers.db_handler.EmbeddingsGenerator.generate_embeddings", side_effect=RuntimeError("secret-failure")):
        with pytest.raises(HTTPException) as exc_info:
            handler.add_question_handler(request)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Internal server error"
    assert "secret-failure" not in exc_info.value.detail


def test_add_question_handler_returns_500_for_unexpected_db_exception():
    handler = DbHandler()
    mock_collection = MagicMock()
    mock_collection.find_one.side_effect = RuntimeError("db down")
    handler.collection = mock_collection

    request = AddNewQA(new_index=1, new_question="new question", new_answer="new answer")

    with pytest.raises(HTTPException) as exc_info:
        handler.add_question_handler(request)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Internal server error"


def test_delete_question_handler_keeps_not_found_contract():
    handler = DbHandler()
    mock_collection = MagicMock()
    mock_collection.find_one.return_value = None
    handler.collection = mock_collection

    with pytest.raises(HTTPException) as exc_info:
        handler.delete_question_handler(42)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Question with index 42 not found"
