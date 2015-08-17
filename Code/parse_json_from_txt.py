__author__ = '9310gaurav'
import json

def parse(filename):
    f = open(filename, 'r')
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