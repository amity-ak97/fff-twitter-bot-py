import tweepy

consumer_key = 'LUraIMHlA4nkcBjTkR4OqF4Ww'
consumer_secret = 'HkHuGWEKvTCBI6L5kTL24cS91keA9GzaOoHgUy7LfDfjvhZIIW'
access_token = '1357417094304976897-NHbMtF7ZucfupVrqmrIqPK6EXUCDa4'
access_token_secret = 'x1l9LJt1tQOYdxpj4SNQYGSYTvLplko4ttWGdzSl9OVsk'

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
