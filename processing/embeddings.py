import logging
from sentence_transformers import SentenceTransformer
from typing import List, Union

logger = logging.getLogger("disaster_agent.processing.embeddings")
logger.setLevel(logging.INFO)

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

try:
    _embedder = SentenceTransformer(MODEL_NAME)
    logger.info(f"Loaded embedding model: {MODEL_NAME}")
except Exception as e:
    logger.error(f"Failed to load embedding model {MODEL_NAME}: {e}")
    raise e

def generate_embedding(text: str) -> List[float]:

    if not text:
        logger.warning("Empty text provided to generate_embedding. Returning an empty embedding.")
        
        return [0.0] * 384

    embedding = _embedder.encode([text])[0]  
    return embedding.tolist()

def batch_generate_embeddings(texts: List[str]) -> List[List[float]]:
    
    if not texts:
        logger.warning("Empty list provided to batch_generate_embeddings. Returning empty list.")
        return []

    embeddings = _embedder.encode(texts)
    return [emb.tolist() for emb in embeddings]

if __name__ == "__main__":
    
    sample_texts = [
        "Flooding has been reported in several coastal regions.",
        "A wildfire in the northern forest has spread over 500 acres."
    ]
 
    emb = generate_embedding(sample_texts[0])
    logger.info(f"Embedding for single text: {sample_texts[0][:50]}... Length: {len(emb)}")

    batch_emb = batch_generate_embeddings(sample_texts)
    logger.info(f"Generated {len(batch_emb)} embeddings for batch processing.")