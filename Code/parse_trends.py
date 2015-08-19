__author__ = 'arkanath'

def parse_trends(filename):
    f = open(filename, 'r')
    lines = f.read().split("\n")
    for l in lines:
        print l
        break

parse_trends("")