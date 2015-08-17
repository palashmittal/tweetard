__author__ = 'arkanath'

import json
from pprint import pprint
import operator

def get_data(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

def get_top_n_hashtags(data, n):
    count = {}
    last_i = 0
    i = 0
    for tweet in data:
        i = i+1
        if(i>=last_i+1):
            last_i = i
            print last_i, " Done"
        for hashtag in set([l["text"] for l in tweet["entities"]["hashtags"]]):
            if hashtag in count:
                count[hashtag]+=1
            else:
                count[hashtag]=1
    count = sorted(count.items(), key=operator.itemgetter(1))
    count = [l for l in reversed(count)]
    print count[0:n]

def get_top_users(data, hashtag):
    return ""

data = get_data("/Users/arkanath/Temp/Social Computing Project/tweetard/Data/sampletweets.json")
get_top_n_hashtags(data,5)