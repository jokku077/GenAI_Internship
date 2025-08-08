import os
from dotenv import load_dotenv

load_dotenv() # loading environment variables


GEMINI_API_KEY = os.environ['GOOGLE_API_KEY']
MONGODB_URI = os.environ['MONGODB_URI']
#
# print(GEMINI_API_KEY)
# print(MONGODB_URI)