"""Shared pytest setup: puts the app package on sys.path and stubs required env vars."""
import os
import sys
import types

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# config/__init__.py reads these at import time and raises KeyError if unset.
os.environ.setdefault("GOOGLE_API_KEY", "test-google-api-key")
os.environ.setdefault("MONGODB_URI", "mongodb://localhost:27017")

# Test-only shim so imports succeed when langchain_google_genai is unavailable.
if "langchain_google_genai" not in sys.modules:
    stub_module = types.ModuleType("langchain_google_genai")

    class GoogleGenerativeAIEmbeddings:  # pragma: no cover - only for import-time fallback
        def __init__(self, *args, **kwargs):
            pass

    stub_module.GoogleGenerativeAIEmbeddings = GoogleGenerativeAIEmbeddings
    sys.modules["langchain_google_genai"] = stub_module
