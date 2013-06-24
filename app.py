from flask import render_template, url_for, request, Flask
from threading import Thread
from time import sleep

import tweepy

app = Flask(__name__)

multiple_user_data = []

@app.route('/')
def home():
	url_for('static', filename='style.css')
	return render_template('index.html')

@app.route('/secretdatabase', methods=['POST'])
def storecredentials():
	try:
		yeller = { "handle": request.form['yeller'],
            	   "password": request.form['password'],
                   "consumerkey": request.form['consumerkey'],
                   "consumersec": request.form['consumersec'],
                   "accesskey": request.form['accesskey'],
                   "accesssec": request.form['accesssec']
		}

		victim = {
				"handle": request.form['victim']
		}
		user_data = {'yeller': yeller, 'victim': victim}
		first_tweet(user_data)
		multiple_user_data.append(user_data)
		return 'Success'
  	except Exception, e:
  		print e
  		return 'Credentials provided are insufficient'

def first_tweet(user_data):
	victim_last_tweet = get_tweets(user_data['victim']['handle'][0].text)
	send_tweet(user_data['yeller'], to_upper(victim_last_tweet))

def subsequent_tweets(user_data):
	vict_tweets = get_tweets(user_data['victim']['handle'])
	yell_last_tweet = get_tweets(user_data['yeller']['handle'])[0].text
	gap = tweet_gap(vict_tweets, yell_last_tweet)
	to_tweet = vict_tweets[0:gap].reverse()
	for tweet in to_tweet:
		send_tweet(user_data['yeller'], tweet.text)

def get_tweets(yeller,handle):
    auth = tweepy.OAuthHandler(yeller['consumerkey'], yeller['consumersec'])
    auth.set_access_token(yeller['accesskey'], yeller['accesssec'])
    api = tweepy.API(auth)
    vict_20 = api.user_timeline(handle)
    return vict_20

def tweet_gap(vict_tweets, yell_last_tweet):
	ticker = 0
	for tweet in vict_tweets:
		if to_upper(tweet.text) == yell_last_tweet:
			return ticker
		else :
			ticker += 1

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

def slave():
	while True:
		for user_data in multiple_user_data:
			subsequent_tweets(user_data)
			time.sleep(30)

if __name__ == "__main__":
	Thread(target=slave).start()
	app.run()