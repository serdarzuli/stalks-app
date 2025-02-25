import pytest
from xAPI.twitter_service import TwitterService

# @pytest.mark.skip(reason="skip the test because of 'Too Many Requests' ")
@pytest.mark.asyncio
async def test_search_recent_tweets():
    twitter = TwitterService()
    query = {
                "query": "(from:twitterdev -is:retweet) OR #twitterdev",
                "tweet.fields": "author_id",
    }
    response = await twitter.search_recent_tweets(query)
    
    assert isinstance(response, dict)
    assert any(key in response for key in ["data", "detail", "status"]), \
    "Response must contain at least one of these keys: 'data', 'detail', 'status code'"

    
@pytest.mark.asyncio
async def test_get_users():
    twitter = TwitterService()
    
    query_get_users = {
        "usernames": "usernames=ArdaTuran,TwitterAPI",
        "user_fields": "user.fields=description,created_at",
    }
    response = await twitter.get_users(query_get_users)
    
    assert isinstance(response, dict)
    assert "data" in response