from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import os

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

collection_name = "rag_pdf_collection"

qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)


class QdrantStorage:
    def __init__(self, collection=collection_name):
        self.client = qdrant
        self.collection = collection
        self.ensure_collection_exists()

    def ensure_collection_exists(self):
        collections = self.client.get_collections().collections
        existing_names = [c.name for c in collections]

        if self.collection not in existing_names:
            print(f"DEBUG: Creating Qdrant collection: {self.collection}")
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=1536,
                    distance=Distance.COSINE
                ),
            )

    def upsert(self, ids, vectors, payloads):
        points = [
            PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i])
            for i in range(len(ids))
        ]

        print(f"DEBUG: Upserting {len(points)} points into {self.collection}")

        self.client.upsert(
            collection_name=self.collection,
            points=points
        )

    def search(self, query_vector, top_k=5):
        results = self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            limit=top_k,
            with_payload=True
        )
        return results