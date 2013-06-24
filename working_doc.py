import tweepy

def send_tweet(yeller,tweet):
    auth = tweepy.OAuthHandler(yeller['consumerkey'], yeller['consumersec'])
    auth.set_access_token(yeller['accesskey'], yeller['accesssec'])
    api = tweepy.API(auth)

    try:
        api.update_status(tweet)
        print "Tweeted:"
        print tweet
    except Exception, e:
        #this will print to heroku logs
        print "Error sending tweet:"
        print tweet
        print e

def to_upper(message):
    upper_message = []
    for token in message.split(" "):
        if is_link(token):
            print "%s is a link" % token
            upper_message.append(token)
        else:
            upper_message.append(token.upper())
    return " ".join(upper_message)


def is_link(token):
    return True if re.match(URL_RE, token) else False
