import feedparser
import logging
from typing import List,Dict

logger=logging.getLogger("disaster_agent.ingestion.fetch_news")
logger.setLevel(logging.INFO)

class RSSFetchError(Exception):
    pass

def fetch_rss_news(rss_url:str)->List[Dict]:

    logger.info(f"Attempting to fetch RSS feed from:{rss_url}")
    feed=feedparser.parse(rss_url)

    if feed.bozo:
        logger.error("Failed to parse RSS feed.The data might be malformed.")
        raise  RSSFetchError("failed to parse RSS feed.")
    # Extract entries
    items=[]
    for entry in feed.entries:
        title=entry.title if 'title' in entry else ''
        description=entry.description if 'description' in entry else ''
        link=entry.link if 'link' in entry else ''

        logger.debug(f"Parsed item: title={title},link={link}")

        items.append({
            'title':title.strip(),
            'description':description.strip(),
            'link':link.strip()
        })
    
    logger.info(f"Successfully fetched {len(items)} items from RSS feed:{rss_url}")
    return items

if __name__ == "__main__":
    
    test_url = "http://feeds.bbci.co.uk/news/rss.xml"
    try:
        data = fetch_rss_news(test_url)
        print(f"Fetched {len(data)} items from {test_url}")
    except RSSFetchError as e:
        print(f"Error fetching RSS data: {e}")
