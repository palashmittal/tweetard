__author__ = 'arkanath'

import json
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
        if(i>=last_i+1000):
            last_i = i
            print last_i, " Done"
        for hashtag in set([l["text"] for l in tweet["entities"]["hashtags"]]):
            if hashtag in count:
                count[hashtag]+=1
            else:
                count[hashtag]=1
    count = sorted(count.items(), key=operator.itemgetter(1))
    count = [l for l in reversed(count)]
    return count[0:n]

def get_top_users(data, hashtag, n):
    user_count = {}
    for tweet in data:
        if hashtag in set([l["text"] for l in tweet["entities"]["hashtags"]]):
            user_id = tweet["user"]["id"]
            if(user_id in user_count):
                user_count[user_id]+=1
            else:
                user_count[user_id]=1
    user_count = sorted(user_count.items(), key=operator.itemgetter(1))
    user_count = [l for l in reversed(user_count)]
    return user_count[0:n]