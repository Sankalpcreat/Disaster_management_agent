# NLP Pipeline Documentation

## Current Pipeline Stages

1. **Text Cleaning (preprocess.py)**:
   - Remove extra whitespace, line breaks, and other extraneous characters.
   - Normalize text for downstream embedding generation.
   - Future Enhancements:
     - Punctuation normalization
     - Removal of HTML tags
     - Language detection and handling

2. **Embedding Generation (embeddings.py)**:
   - Use a Sentence Transformers model (e.g., `sentence-transformers/all-MiniLM-L6-v2`) to convert cleaned text into dense embeddings.
   - These embeddings capture semantic meaning, enabling similarity search and context retrieval.
   - Future Enhancements:
     - Experiment with different embedding models
     - Domain-specific fine-tuning
     - Batch processing for efficiency

## Future Steps

- **Named Entity Recognition (NER)**: Identify locations, organizations, and other key entities in disaster-related texts.
- **Sentiment Analysis**: Determine the urgency or severity of reports.
- **Topic Modeling**: Cluster related documents to quickly identify trends or categories in incoming data.
- **Translation**: If data sources are multilingual, integrate translation steps or use multilingual embedding models.

By documenting the current pipeline and planned improvements, we ensure transparency in our workflow and a roadmap for future expansions. Regular updates to this document will help align the team on the NLP strategy and its evolution over time.