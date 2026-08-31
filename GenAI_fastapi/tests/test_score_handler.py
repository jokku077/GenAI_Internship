"""Unit tests for handlers.score_handler (ScoreCalculator, ScoreChecker)."""
import numpy as np

from handlers.score_handler import ScoreCalculator, ScoreChecker


def test_check_low_score_returns_true_when_all_scores_at_or_below_threshold():
    assert ScoreChecker.check_low_score([0.1, 0.2, 0.3]) is True


def test_check_low_score_returns_false_when_any_score_above_threshold():
    assert ScoreChecker.check_low_score([0.1, 0.35, 0.2]) is False


def test_check_equal_score_detects_duplicate_nonzero_scores():
    assert ScoreChecker.check_equal_score([0.5, 0.2, 0.5]) is True


def test_check_equal_score_returns_false_for_distinct_scores():
    assert ScoreChecker.check_equal_score([0.1, 0.2, 0.3]) is False


def test_check_equal_score_ignores_duplicate_zero_scores():
    assert ScoreChecker.check_equal_score([0.0, 0.0, 0.4]) is False


def test_return_max_score_index_returns_index_of_highest_score():
    scores = np.array([0.1, 0.9, 0.3])
    assert ScoreCalculator.return_max_score_index(scores) == 1
