# Storage Architecture

## Overview

The Disaster Response Knowledge Agent stores its semantic embeddings and document metadata using Pinecone, a managed vector database.

## Components

1. **Vector Database (Pinecone)**:
   - **Index Name**: `disaster_index`
   - **Dimension**: 384 (matching the `all-MiniLM-L6-v2` sentence-transformer model)
   - **Metadata**: Stored as key-value pairs along with each vector embedding.
   - **Scalability**: Pinecone can scale horizontally to handle large amounts of data and queries.

2. **Schema**:
   Each document is stored as a vector plus associated metadata:
   - **id**: Unique identifier (UUID)
   - **embedding**: A 384-dimensional float vector
   - **metadata**: A dictionary containing:
     - `title`: Title of the news article or disaster report
     - `description`: A summary or main content
     - `link`: URL link to the source (if available)

3. **Indexing Strategy**:
   - **On Ingestion**: After data cleaning and embedding generation, documents are upserted into the Pinecone index.
   - **Querying**: Queries are transformed into embeddings, and the top K similar documents are retrieved based on cosine similarity.

4. **Future Enhancements**:
   - Add timestamps and source tags to metadata.
   - Implement filters for region, disaster type, or urgency.
   - Integrate a relational or time-series database for structured queries.

This architecture ensures that the agent can rapidly retrieve semantically similar documents, enabling context-rich, retrieval-augmented generation for disaster-related insights.