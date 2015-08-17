__author__ = '9310gaurav'
import json
def parse():
	f = open('./sports/ausopen.txt', 'r')
	all = f.read().split("\n")
	i = 0
	tweets = []
	for tweet in all:
		try:
			d = json.loads(tweet)
		except ValueError:
			print d = {}
		tweets.append(d)
	return tweets

if __name__ == "__main__":
	ans = parse()
	print ans[0]
	
