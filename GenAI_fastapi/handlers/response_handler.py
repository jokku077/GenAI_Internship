from handlers.score_handler import ScoreChecker, ScoreCalculator
from utils.db_utils import DbFetcher

class ResponseHandler:

    @staticmethod
    def give_response(query):
        answers = DbFetcher.fetch_answers()
        scores = ScoreCalculator.calculate_scores(query) #calculates similarity of query embeddings with all question embeddings

        if ScoreChecker.check_low_score(scores.tolist()): #convert to list because scores is np array, return true if scores are low
            return [scores,"Please ask relevant questions"]
        if ScoreChecker.check_equal_score(scores.tolist()): #returns true if scores are equal
            return [scores, "Please provide additional context"]

        max_score_index = scores.argmax(axis=0)
        return [scores.tolist(), answers[max_score_index]] # returns a list of the scores and the relevant answer

# print(ResponseHandler.give_response("What about repairs and services?"))
