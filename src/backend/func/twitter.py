import tweepy
from datetime import date

from src.config.env import settings

def make_tweet(tweet:str):
    # try:
    newapi = tweepy.Client(consumer_key=settings.APP.X_CONSUMER_KEY,
                        consumer_secret=settings.APP.X_CONSUMER_SECRET,
                        access_token=settings.APP.X_ACCESS_KEY,
                        access_token_secret=settings.APP.X_ACCESS_SECRET)

    post_result = newapi.create_tweet(text=tweet)
    print(post_result)
    # except:
    #     print("FAILED TO POST A TWEET")
