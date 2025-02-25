import aiohttp
import asyncio
import json
from xAPI.config import BASE_URL, HEADERS

class TwitterService:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS
        
    async def _send_request(self, url, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers=self.headers, params=params
            ) as response:
                return await response.json()
            
            
    async def search_recent_tweets(self, params: dict) -> dict:
        url = f"{self.base_url}/tweets/search/recent"

        return await self._send_request(url, params)


    async def recent_tweet_counts(self, params: dict) -> dict:
        url = f"{self.base_url}/tweets/counts/recent"

        return await self._send_request(url, params)


    async def retweed_lookup(self, params: dict) -> dict:
        url = f'{self.base_url}/tweets/{params["id"]}/retweeted_by'
        user_fields = params["user_fields"]
        return await self._send_request(url, user_fields)


    async def get_tweets(self, params: dict) -> dict:
        url = f'{self.base_url}/tweets?{params["ids"]}&{params["tweet_fields"]}'

        return await self._send_request(url)


    async def get_users(self, params: dict) -> dict:
        url = (
            f"{self.base_url}/users/by?{params['usernames']}&{params['user_fields']}"
        )

        return await self._send_request(url)


    async def user_mentions(self, params: dict, id: dict) -> dict:
        user_id = id["user_id"]
        url = f"{self.base_url}/users/{user_id}/mentions"

        return await self._send_request(url, params)
    
    
    async def get_all_tweets(self, params: dict) -> dict:
        url = f'{self.base_url}/users/{params["user_id"]}/tweets?{params["tweet_fields"]}'
        return await self._send_request(url, params)
            
            
    async def fetch_all_tweets(self, params: dict) -> list:
        """
        Get all tweets > 10 via pegination.
        """
        all_tweets = []
        next_token = None

        while True:
            url = f'{self.base_url}/users/{params["user_id"]}/tweets?{params["tweet_fields"]}'
            
            # if next_token is true, the next page will add.
            if next_token:
                url += f"&pagination_token={next_token}"

            result = await self._send_request(url)

            # check the errors
            if isinstance(result, list) and result and isinstance(result[0], dict):
                if result[0].get("status") == 429:
                    print("Too many requests. Waiting 15 seconds...")
                    await asyncio.sleep(15)  # Wait 15 seconds
                    continue  # Tekrar dene

            # Add all tweets to list
            tweets = result.get("data", [])
            all_tweets.extend(tweets)

            # check the new token is true or false
            next_token = result.get("meta", {}).get("next_token", None)
            if not next_token:
                break  # if false break loop

        return all_tweets