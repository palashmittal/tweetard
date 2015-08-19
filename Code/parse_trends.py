__author__ = 'arkanath'
import ast
import time
import operator

def parse_trends(filename):
    f = open(filename, 'r')
    lines = [l for l in f.read().split("\n") if l]
    last_i = 0
    i = 0
    total_encountered = {}
    months = {}
    per_month_count = {}
    month_count = {}
    for l in lines:
        i+=1
        if(i>last_i+100):
            last_i = i
            # print i
            # break
        # print l
        split_lines = l.split("\t")
        timestamp = split_lines[0]
        hashtags = ast.literal_eval(split_lines[1])
        # print timestamp
        aa = time.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
        for hash in hashtags:
            if hash not in total_encountered:
                total_encountered[hash] = 0
                month_count[hash] = 0
                months[hash] = []
                per_month_count[hash] = {}
                for mon in range(1,12,1):
                    per_month_count[hash][mon] = 0
            if aa.tm_mon not in months[hash]:
                months[hash].append(aa.tm_mon)
                month_count[hash]+=1
            per_month_count[hash][aa.tm_mon]+=1
            total_encountered[hash] += 1
    month_count_total_count = month_count.items()
    for ii in range(len(month_count_total_count)):
        month_count_total_count[ii] = month_count_total_count[ii]+(total_encountered[month_count_total_count[ii][0]],)
    month_count_total_count = sorted(month_count_total_count, key=operator.itemgetter(1,2))
    month_count_total_count = [l for l in reversed(month_count_total_count)]
    return month_count_total_count,month_count,months,total_encountered,per_month_count