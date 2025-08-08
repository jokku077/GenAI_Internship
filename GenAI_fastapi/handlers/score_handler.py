import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.db_utils import DbFetcher
from handlers.embeddings_handler import EmbeddingsGenerator

# print(question_embeddings)

class ScoreCalculator:
    @staticmethod
    def calculate_scores(query):
        question_embeddings = DbFetcher.fetch_embeddings()
        scores = []
        query_embedding = EmbeddingsGenerator.generate_embeddings(query)
        for i in range(len(question_embeddings)):
            question_embedding = question_embeddings[i]
            similarity = cosine_similarity([query_embedding], [question_embedding])[0][0]
            scores.append(similarity)
        return np.array(scores)

    @staticmethod
    def return_max_score_index(scores):
        max_score_index = scores.argmax(axis=0)
        return max_score_index

# scores = ScoreCalculator.calculate_scores("Won't turn on", question_embeddings)
# print(scores)
# maxscoreindex = scores.argmax(axis = 0)
# answers = DbFetcher.fetch_answers()
# print("Answer: ",answers[maxscoreindex])

class ScoreChecker:
    @staticmethod
    def check_low_score(scores):#return true if scores are low, takes array as input
        for score in scores:
            if score > 0.3:
                return False
        return True

    @staticmethod
    def check_equal_score(scores): #returns true if any scores are equal, takes array as input
        for i in range(len(scores)-1):
            for j in range(i+1, len(scores)):
                if scores[i] == scores[j] and scores[i] != 0 and scores[j] != 0:
                    return True
        return False