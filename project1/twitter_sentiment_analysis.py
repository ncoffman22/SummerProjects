#!/usr/bin/python3

# Author: Noah Coffman
# Based on: https://github.com/llSourcell/twitter_sentiment_challenge

import tweepy
from textblob import TextBlob

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = api.search_tweets(q='Trump', tweet_fields=['text'])

for tweet in tweets.data:
    print(tweet.text)
    print(TextBlob(tweet.text).sentiment)

