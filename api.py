import tweepy
import config

auth = tweepy.OAuth1UserHandler(
    config.api_key,
    config.api_secret,
    config.consumer_key,
    config.consumer_secret
)
API = tweepy.API(auth, wait_on_rate_limit=True)
