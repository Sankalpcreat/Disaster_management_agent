import re
import logging

logger=logging.getLogger("disaster_agent.processing.preprocess")
logger.setLevel(logging.INFO)

def clean_text(text:str)->str:

    if not text:
        return ""
    
    text=text.strip()

    text=re.sub(r'\s+', ' ',text)
    return text

if __name__ == "__main__":
    raw_text = "   This is   a sample   text with   irregular spacing!   "
    cleaned = clean_text(raw_text)
    logger.info(f"Original: '{raw_text}'")
    logger.info(f"Cleaned: '{cleaned}'")
