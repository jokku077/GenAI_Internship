"""Builds the chatbot's response by matching a query against stored Q&A embeddings."""
from handlers.score_handler import ScoreChecker, ScoreCalculator
from utils.db_utils import DbFetcher

class ResponseHandler:
    """Selects the best-matching stored answer for a user query."""

    @staticmethod
    def give_response(query):
        """Compute the best-matching knowledge-base answer for a user query.

        Returns:
            [scores, message] if the similarity scores are all low or all
            equal (ambiguous match); otherwise [scores, answer] for the
            best-matching question.
        """
        answers = DbFetcher.fetch_answers()
        scores = ScoreCalculator.calculate_scores(query) #calculates similarity of query embeddings with all question embeddings

        if ScoreChecker.check_low_score(scores.tolist()): #convert to list because scores is np array, return true if scores are low
            return [scores,"Please ask relevant questions"]
        if ScoreChecker.check_equal_score(scores.tolist()): #returns true if scores are equal
            return [scores, "Please provide additional context"]

        max_score_index = scores.argmax(axis=0)
        return [scores.tolist(), answers[max_score_index]] # returns a list of the scores and the relevant answer

# print(ResponseHandler.give_response("What about repairs and services?"))
