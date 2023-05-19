#!/usr/bin/python3

# Author: Noah Coffman
# Based on: https://github.com/llSourcell/twitter_sentiment_challenge

import tweepy
from textblob import TextBlob

consumer_key = 'JGxu5Vc6yhN2C84cjd2qHzemG'
consumer_secret = 'eCdRsZxNJczVzeqdCFtIBrjozRTkUslyFwxlIlyW41gvgtEvpa'
access_token = '883900563901079553-j3lnTqSYxTFpOskHINUL7h3kwO0EaXR'
access_token_secret = 'o0yMXgOV657KuQqvwv8JXM0xWeP3yFanN2ZF3vQOKhK6s'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = api.search_tweets(q='Trump', tweet_fields=['text'])

for tweet in tweets.data:
    print(tweet.text)
    print(TextBlob(tweet.text).sentiment)

