"""Unit tests for handlers.response_handler.ResponseHandler (with DB/embeddings mocked)."""
from unittest.mock import patch

import numpy as np

from handlers.response_handler import ResponseHandler


@patch("handlers.response_handler.ScoreCalculator")
@patch("handlers.response_handler.DbFetcher")
def test_give_response_returns_best_matching_answer(mock_db_fetcher, mock_score_calculator):
    mock_db_fetcher.fetch_answers.return_value = ["answer one", "answer two"]
    mock_score_calculator.calculate_scores.return_value = np.array([0.2, 0.9])

    result = ResponseHandler.give_response("some question")

    assert result[1] == "answer two"


@patch("handlers.response_handler.ScoreCalculator")
@patch("handlers.response_handler.DbFetcher")
def test_give_response_returns_low_score_message_when_no_good_match(mock_db_fetcher, mock_score_calculator):
    mock_db_fetcher.fetch_answers.return_value = ["answer one", "answer two"]
    mock_score_calculator.calculate_scores.return_value = np.array([0.1, 0.2])

    result = ResponseHandler.give_response("irrelevant question")

    assert result[1] == "Please ask relevant questions"


@patch("handlers.response_handler.ScoreCalculator")
@patch("handlers.response_handler.DbFetcher")
def test_give_response_returns_ambiguous_message_for_equal_scores(mock_db_fetcher, mock_score_calculator):
    mock_db_fetcher.fetch_answers.return_value = ["answer one", "answer two"]
    mock_score_calculator.calculate_scores.return_value = np.array([0.5, 0.5])

    result = ResponseHandler.give_response("ambiguous question")

    assert result[1] == "Please provide additional context"
