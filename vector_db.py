from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

collection_name = "rag_pdf_collection"

qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

def create_collection():
    qdrant.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=3072,
            distance=Distance.COSINE
        ),
    )