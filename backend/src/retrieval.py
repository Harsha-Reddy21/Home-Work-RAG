import os
from pinecone import Pinecone
from typing import List, Dict, Any

def init_pinecone():
    """Initialize Pinecone client"""
    api_key = os.environ.get("PINECONE_API_KEY")
    environment = os.environ.get("PINECONE_ENVIRONMENT")
    
    if not api_key or not environment:
        raise ValueError("Pinecone API key and environment must be set")
    
    return Pinecone(api_key=api_key, environment=environment)

def get_index(index_name=None):
    """Get Pinecone index"""
    pc = init_pinecone()
    index_name = index_name or os.environ.get("PINECONE_INDEX")
    
    if not index_name:
        raise ValueError("Pinecone index name must be provided")
    
    return pc.Index(index_name)

async def retrieve_similar_examples(query_vector: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
    """Retrieve similar examples from Pinecone"""
    try:
        index = get_index()
        results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
        return results.matches
    except Exception as e:
        print(f"Error retrieving from Pinecone: {str(e)}")
        return []
