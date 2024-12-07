# Data Sources

This file documents the data sources integrated into the Disaster Response Knowledge Agent.

## RSS Feeds (News)

- **BBC News**:  
  - Endpoint: `http://feeds.bbci.co.uk/news/rss.xml`  
  - Format: RSS (XML)  
  - Data Fields (entry): title, link, description, published date  
  - Rate Limits: Typically none, but should not poll excessively  
  - Authentication: None required

- **CNN News**:  
  - Endpoint: `http://rss.cnn.com/rss/edition.rss`  
  - Format: RSS (XML)  
  - Data Fields (entry): title, link, description, published date  
  - Authentication: None required

## Disaster APIs

- **ReliefWeb API**:
  - Endpoint: `https://api.reliefweb.int/v1/disasters` (example)  
  - Format: JSON  
  - Data Fields (example): `title`, `date`, `url`, `fields.summary`, etc.  
  - Authentication: None required for basic queries  
  - Rate Limits: May apply; consult official documentation  
  - Additional Documentation: [https://api.reliefweb.int/](https://api.reliefweb.int/)

**Note**: Additional APIs can be added here, including any necessary tokens or authentication details. For private or rate-limited APIs, document how to obtain and refresh API keys or tokens.