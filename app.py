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

if __name__ == "__main__":
    app.run()