from flask import Flask
from flask import request
from flask import render_template, url_for

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
		yeller = { "yeller username": request.form['yeller'],
            	   "password": request.form['password'],
                   "consumer key": request.form['consumerkey'],
                   "consumer secret": request.form['consumersec'],
                   "access key": request.form['accesskey'],
                   "access secret": request.form['accesssec']
		}

		victim = {
				"victim username": request.form['victim']
		}

		user_data = {"yeller": yeller, "victim": victim}
		multiple_user_data.append(user_data)
		print(accounts)
		return 'Success'
  	except:
  		return 'Credentials provided are insufficient'

def first_tweet(user_data):
	victim_last_tweet = get_tweets(user_data.victim.handle)[0]
	send_tweet(user_data.yeller, str.upper(victim_last_tweet))

def subsequent_tweets(user_data):
	vict_tweets = get_tweets(user_data.victim.handle)
	yell_last_tweet = get_tweets(user_data.yeller.handle)[0]
	gap = tweet_gap(vict_tweets, yell_last_tweet)
	to_tweet = vict_tweets[0:gap].reverse()
	for tweet in to_tweet:
		send_tweet(user_data.yeller, tweet)

def tweet_gap(vict_tweets, yell_last_tweet):
	ticker = 0
	for tweet in vict_tweets:
		if str.toupper(tweet) == yell_last_tweet:
			return ticker
		else :
			ticker += 1

if __name__ == "__main__":
    app.run()