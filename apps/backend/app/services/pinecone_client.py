from pinecone import Pinecone
from app.core.config import get_settings

settings = get_settings()

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

index = pc.Index(settings.PINECONE_INDEX_NAME)

def check_index():
    return index.describe_index_stats()