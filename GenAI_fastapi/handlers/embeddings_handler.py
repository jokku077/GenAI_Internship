from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GEMINI_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07", google_api_key=GEMINI_API_KEY)

class EmbeddingsGenerator:
    @staticmethod
    def generate_embeddings(query): # returns embeddings vector
        return embeddings.embed_query(query)