import os
import logging
from pinecone import Pinecone, ServerlessSpec

logger=logging.getLogger("disaster_agent.storage.pinecone_setup")
logger.setLevel(logging.INFO)


logger = logging.getLogger("disaster_agent.storage.pinecone_setup")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def init_pinecone()->Pinecone:
    api_key=os.environ.get("PINECONE_API_KEY")
    if not api_key:
        logger.error("PINECONE_API_KEY is not set")
        raise ValueError("PINECONE_API_KEY must be set.")
    
    pc=Pinecone(api_key=api_key)
    logger.info("Pinecone initialized successfully.")
    return pc

def create_index_if_not_exists(pc:Pinecone,index_name="disaster_index",dimension=384):

    existing_indexes=[index['name'] for index in pc.list_indexes()]

    if index_name not in existing_indexes:
        logger.info(f"Creating Pinecone index '{index_name}' with dimension {dimension}.")
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric='cosine',
            spec=ServerlessSpec(cloud="aws",region="us-east-1")
        )
    else:
        logger.info(f"Pinecone index '{index_name}' already exists.")

if __name__=="__main__":
    try:
        pc=init_pinecone()
        create_index_if_not_exists(pc,index_name="disaster_index",dimension=384)
    except Exception as e:
        logger.error(f"Failed to initialize Pinecone: {e}")