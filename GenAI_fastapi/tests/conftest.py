"""Shared pytest setup: puts the app package on sys.path and stubs required env vars."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# config/__init__.py reads these at import time and raises KeyError if unset.
os.environ.setdefault("GOOGLE_API_KEY", "test-google-api-key")
os.environ.setdefault("MONGODB_URI", "mongodb://localhost:27017")
