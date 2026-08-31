"""Wraps the Gemini embedding model used to vectorize chatbot questions and queries."""
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GEMINI_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07", google_api_key=GEMINI_API_KEY)

class EmbeddingsGenerator:
    """Generates embedding vectors via the configured Gemini embedding model."""

    @staticmethod
    def generate_embeddings(query):
        """Return the embedding vector for the given text query."""
        return embeddings.embed_query(query)