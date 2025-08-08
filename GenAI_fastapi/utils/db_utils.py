from pymongo import MongoClient
from config import MONGODB_URI

def connect_db():
    client = MongoClient(MONGODB_URI, tls=True,  tlsAllowInvalidCertificates=True  ) # Use `tls` instead of `ssl` # Update with your DB URI #mongodb://localhost:27017/
    db = client["Genai_fastapi"]  # Database name
    my_collection = db["chatbotdb"] # collection name
    return my_collection

chat_db = connect_db()

class DbFetcher:
    @staticmethod
    def fetch_questions():
        """Fetch all questions from the knowledge base"""
        questions = []
        for doc in chat_db.find({}, {"_id": 0, "question": 1}):
            questions.append(doc["question"])
        return questions

    @staticmethod
    def fetch_answers():
        answers = []
        for doc in chat_db.find({}, {"_id": 0, "answer": 1}):
            answers.append(doc["answer"])
        return answers

    @staticmethod
    def fetch_embeddings():
        embeddings_list = []
        for doc in chat_db.find({}, {"_id": 0, "embeddings": 1}):
            embeddings_list.append(doc["embeddings"])
        return embeddings_list

# print(DbFetcher.fetch_questions())

