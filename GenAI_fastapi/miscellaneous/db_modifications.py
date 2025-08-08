import pymongo
import logging
client = pymongo.MongoClient(
    "mongodb+srv://jokku7110:jokkumongoatlas@cluster0.7s1xk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tls=True,
    tlsAllowInvalidCertificates=True)  # Use `tls` instead of `ssl` # Update with your DB URI #mongodb://localhost:27017/
db = client["Genai_fastapi"]
collection = db['chatbotdb']


# here we are updating the embeddings field of each document with the embedding of the question
cursor = collection.find({})
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07", google_api_key="AIzaSyAUuB5ru2kbLRRYdm-wBiDLq2T7tCabSZA")
# Process documents

# for index, doc in enumerate(cursor):
#     collection.update_one(
#         {'_id': doc['_id']},
#         {'$set': {'index': index}}
#     )
#     print(f"added index: {index} to doc: {doc['_id']}")
#
# client.close()

# processed_count = 0
# for doc in cursor:
#     processed_count += 1
#     if processed_count > 20:
#
#     # Check if question field exists
#         if 'question' in doc:
#             try:
#                 # Get the question text
#                 question_text = doc['question']
#
#                 # Generate embeddings
#                 embedding_vector = embeddings.embed_query(question_text)
#                 print(f"Successfully generated embedding for document ID: {doc['_id']}")
#
#                 # Update document directly
#                 collection.update_one(
#                     {'_id': doc['_id']},
#                     {'$set': {'embeddings': embedding_vector}}
#                 )
#
#             except Exception as e:
#                 error_message = str(e).lower()
#                 print(f"ERROR at document ID: {doc['_id']}")
#                 print(f"Error message: {str(e)}")
#
#                 # Check for quota-related errors
#                 if "quota" in error_message or "limit" in error_message or "rate" in error_message:
#                     print("API QUOTA LIKELY EXHAUSTED!")
#                     print(f"Processed {processed_count} documents before error")
#                     # Optional: wait before continuing or exit
#                     # time.sleep(60)  # Wait 60 seconds before trying again
#                     # OR
#                     print("Exiting due to quota exhaustion")
#                     break  # Exit the loop
#
#     # Optional: print progress every 10 documents
#     if processed_count % 10 == 0:
#         print(f"Processed {processed_count} documents")
#
# # Close connection
# print(f"Finished processing. Total documents processed: {processed_count}")
# client.close()