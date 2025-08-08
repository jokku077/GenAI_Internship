from google import genai
import os
from sklearn.metrics.pairwise import cosine_similarity
from config import GEMINI_API_KEY

# google_api_key = os.getenv("GOOGLE_API_KEY")
# print(google_api_key)
# client = genai.Client(api_key="AIzaSyAUuB5ru2kbLRRYdm-wBiDLq2T7tCabSZA")


# result1 = client.models.embed_content(
#         model="gemini-embedding-exp-03-07",
#         contents="What is the meaning of life?")
#
# print(result1.embeddings)
#
# result2 = client.models.embed_content(
#         model="gemini-embedding-exp-03-07",
#         contents="What is the meaning of death?")
#
# print(result2.embeddings)

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07", google_api_key=GEMINI_API_KEY)
vector1 = embeddings.embed_query("Roses are red")
vector2 = embeddings.embed_query("Red carpet is red")
print(vector1[0:5])
similarity = cosine_similarity([vector1], [vector2]) # we are wrapping the parameters within a list because
                                                            # cosine similarity expects 2-d array
print(similarity)
print("similarity = ", similarity[0][0])


# for i in result.embeddings:
#     print(type(i))
# print(len(result.embeddings))