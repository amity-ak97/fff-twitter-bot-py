import tweepy
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_string = '#FridaysForFuture'


def startLikeNRetweet():
    for tweet in tweepy.Cursor(api.search, search_string).items():
        try:
            tweet.retweet()
            tweet.favorite()
            print('Succeed...')

        except tweepy.TweepError as e:
            print(e)


print('App Started...')
startLikeNRetweet()
