import asyncio
from xAPI.twitter_service import TwitterService
from xAPI.config import query_get_all_tweets
from openAI_API.deep_seek_service import DeepSeekService

    
async def main():
    twitter = TwitterService()
    deep_seek = DeepSeekService()
    chat = await deep_seek.chat_deep_seek()
    print(chat)
    # gpt = GptService()

    
    # get_all_tweets = await twitter.get_all_tweets(query_get_all_tweets)
    # print(get_all_tweets)


if __name__ == "__main__":
    asyncio.run(main())
    
    
 