import requests
import logging
from typing import List,Dict,Optional

logger=logging.getLogger("disaster_agent.ingestion.fetch_disaster_api")
logger.setLevel(logging.INFO)

class APIFetchError(Exception):
    pass

def fetch_disaster_api(api_url:str,params:Optional[Dict]=None)->List[Dict]:

    logger.info(f"Fetching disaster data from API:{api_url} with params:{params}")

    try:
        response=requests.get(api_url,params=params,timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Network or HTTP error when fetching API data:{e}")
        raise APIFetchError(f"failed to fetch API data from {api_url} :{e}")

    try:
        data=response.json()
    except ValueError as e:
        logger.error("the Response is not in valid JSON format.")
        raise APIFetchError("Invalid JSON response from the API.")

    items=[]
    entries=data.get('data',[])
    for entry in entries:
        fields=entry.get('fields',{})
        title=fields.get('title',"").strip()
        description=fields.get('summary',"").strip()
        link=entry.get('href',"").strip()

        logger.debug(f"Parsed disaster item:title={title},link={link}")

        items.append({
            'title':title,
            'description':description,
            'link':link
        })

    logger.info(f"Successfully fetched {len(items)} disaster items from API: {api_url}")
    return items

if __name__="__main__":

    test_api_url = "https://api.reliefweb.int/v1/disasters"

    params={
        "appname":"my_disaster_app","limit":5
    }

    try:
        disasters=fetch_disaster_api(test_api_url,params=params)
        print(f"Fetched {len(disasters)} disaster items from API: {test_api_url}")
    except APIFetchError as e:
        print(f"Error fetching API data: {e}")

