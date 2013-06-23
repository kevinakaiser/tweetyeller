from flask import Flask
from flask import request

import tweepy

app = Flask(__name__)

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

		accounts = [yeller, victim]
		print(accounts)
		return 'Success'
  	except:
  		return 'Credentials provided are insufficient'

if __name__ == "__main__":
    app.run()