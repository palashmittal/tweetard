__author__ = 'palashmittal'

import json

def get_user_tweets(filename, user_id, hashtag):
	tweet_text = []
	with open(filename) as data_file:
		data = json.load(data_file)
	for tweet in data:
		if tweet["user"]["id"] == user_id:
			if hashtag in set([l["text"] for l in tweet["entities"]["hashtags"]]):
				tweet_text.append(tweet["text"])

	return tweet_text