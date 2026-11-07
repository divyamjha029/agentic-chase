import os
import chromadb
from chromadb.config import Settings

# Persistent local client (stores vectors in a local folder named chroma_db)
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

# Get or create a single master collection for all chat memories
collection = chroma_client.get_or_create_collection(name="agentic_chase_memories")

def store_chat_chunk(project_id: str, chat_id: str, chunk_id: str, text: str, sender: str):
    """
    Stores a conversation chunk into ChromaDB with strict metadata tagging
    to guarantee isolation between different chats.
    """
    collection.add(
        documents=[text],
        metadatas=[{
            "project_id": project_id,
            "chat_id": chat_id,
            "sender": sender
        }],
        ids=[chunk_id]
    )

def query_chat_memory(project_id: str, chat_id: str, query_text: str, n_results: int = 3):
    """
    Searches memory ONLY within the specified project_id and chat_id.
    This prevents cross-chat contamination (e.g., group jokes leaking into direct chats).
    """
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={
            "$and": [
                {"project_id": {"$eq": project_id}},
                {"chat_id": {"$eq": chat_id}}
            ]
        }
    )
    
    # Extract and return just the text fragments found
    if results and "documents" in results and results["documents"]:
        return results["documents"][0]
    return []
