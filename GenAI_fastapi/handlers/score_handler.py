"""Computes and evaluates similarity scores between a query and stored questions."""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.db_utils import DbFetcher
from handlers.embeddings_handler import EmbeddingsGenerator

# print(question_embeddings)

class ScoreCalculator:
    """Computes cosine-similarity scores between a query and stored questions."""

    @staticmethod
    def calculate_scores(query):
        """Return cosine-similarity scores between the query and every stored question.

        Returns:
            np.ndarray of scores, ordered to match `DbFetcher.fetch_embeddings()`.
        """
        question_embeddings = DbFetcher.fetch_embeddings()
        scores = []
        query_embedding = EmbeddingsGenerator.generate_embeddings(query)
        for i in range(len(question_embeddings)):
            question_embedding = question_embeddings[i]
            similarity = cosine_similarity([query_embedding], [question_embedding])[0][0]
            scores.append(similarity)
        return np.array(scores)
        # sort best-match-first for more readable score output
        # intentional change
        # return np.sort(np.array(scores))[::-1]

    @staticmethod
    def return_max_score_index(scores):
        """Return the index of the highest score."""
        max_score_index = scores.argmax(axis=0)
        return max_score_index

# scores = ScoreCalculator.calculate_scores("Won't turn on", question_embeddings)
# print(scores)
# maxscoreindex = scores.argmax(axis = 0)
# answers = DbFetcher.fetch_answers()
# print("Answer: ",answers[maxscoreindex])

class ScoreChecker:
    """Evaluates similarity scores to decide whether a query match is usable."""

    @staticmethod
    def check_low_score(scores):
        """Return True only if every score is at or below the 0.3 relevance threshold."""
        for score in scores:
            if score > 0.3:
                return False
        return True

    @staticmethod
    def check_equal_score(scores):
        """Return True if any two nonzero scores are exactly equal (ambiguous match)."""
        for i in range(len(scores)-1):
            for j in range(i+1, len(scores)):
                if scores[i] == scores[j] and scores[i] != 0 and scores[j] != 0:
                    return True
        return False