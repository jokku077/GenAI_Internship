"""Application configuration loaded from environment variables.

Requires GOOGLE_API_KEY and MONGODB_URI to be set (via .env or the
environment) before this module is imported; raises KeyError otherwise.
"""
import os
from dotenv import load_dotenv

load_dotenv() # loading environment variables


GEMINI_API_KEY = os.environ['GOOGLE_API_KEY']
MONGODB_URI = os.environ['MONGODB_URI']
#
# print(GEMINI_API_KEY)
# print(MONGODB_URI)