import tweepy

def get_tweets(yeller,handle):
    auth = tweepy.OAuthHandler(yeller['consumerkey'], yeller['consumersec'])
    auth.set_access_token(yeller['accesskey'], yeller['accesssec'])
    api = tweepy.API(auth)
    vict_20 = api.user_timeline(handle)
    return vict_20