import tweepy
from textblob import TextBlob

consumer_key= 'vrT7BzLu9QvdaupsmKJhYtIKJ'
consumer_secret= 'ZFTYPExtWX6VBYOjgHtCU1JtMmEkzbWXoM6tfS8qXM1KTtk3GX'

access_token='871287518741676033-YUwaPdJNhirAYx0eNJhHEbnFRBfeF6S'
access_token_secret='TdoJzeqiBf6HSg5SJhfZDMkBkEEJLWvVwLmcnMjha0ZNY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_twitter = tweepy.API(auth)
