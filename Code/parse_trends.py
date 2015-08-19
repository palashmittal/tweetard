__author__ = 'arkanath'

def parse_trends(filename):
    f = open('./sports/ausopen.txt', 'r')
    all = f.read().split("\n")
    i = 0