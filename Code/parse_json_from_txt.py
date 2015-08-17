__author__ = '9310gaurav'
import json

def parse(filename):
    f = open('./sports/ausopen.txt', 'r')
    all = f.read().split("\n")
    i = 0
    outfile = open('tweets.json','w')
    out = []
    for tweet in all:
        try:
            d = json.loads(tweet)
            g = {}
            g['id'] = d['id']
            g['text'] = d['text']
            g['created_at'] = d['created_at']
            g['retweet_count'] = d['retweet_count']
            g['entities'] = {}
            g['entities']['hashtags'] = d['entities']['hashtags']
            g['user'] = {}
            g['user']['id'] = d['user']['id']
            out.append(g)
        except ValueError:
            d = {}
    json.dump(out,outfile)