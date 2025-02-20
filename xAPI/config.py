import os
from dotenv import load_dotenv

#.env load file
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
BASE_URL = "https://api.twitter.com/2"
HEADERS = {
    "Authorization": f"Bearer {CONSUMER_KEY}",
    "User-Agent": "v2TweetLookupPython"
}

query_get_all_tweets = {
            'tweet_fields': 'tweet.fields=created_at,lang,public_metrics',
            'user_id': '44196397'
}


# print("🔍 Searching for recent tweets...")
query_search_recent_tweets = {
        "query": "(from:twitterdev -is:retweet) OR #twitterdev",
        "tweet.fields": "author_id",
}
# tweets = await twitter.search_recent_tweets(query)


# print("\n📊 Fetching tweet counts...")
query_recent_tweet_counts = {"query": "from:twitterdev", "granularity": "day"}
# tweet_counts = await twitter.recent_tweet_counts(query_count)


# print("\n📊 Re-tweet lookup...")
query_retweed_lookup = {
        "user_fields": "user.fields=created_at,description",
        "id": "2295310321",
    }
# re_tweet_lookup = await twitter.retweed_lookup(query_re_tweet)


# print("\n👤 Fetching user info...")
query_get_users = {
        "usernames": "usernames=ArdaTuran,TwitterAPI",
        "user_fields": "user.fields=description,created_at",
    }
# users = await twitter.get_users(query_user_info)


query_get_tweets = {
        "tweet_fields": "tweet.fields=lang,author_id",
        "ids": "ids=1278747501642657792,1255542774432063488",
    }
# query_get_tweets = await twitter.get_tweets(query_params4)