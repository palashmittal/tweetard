# from __future__ import print_function
import ast
import os   
import operator
dicto = {'follow' :['follow','openfollow','tfb','followtrick','tfbjp','teamfollowback','follow2befollowed','followback','sougofollow','anotherfollowtrain','tcfollowtrain','tityfollowtrain','hitfollowsteam','followme'],
'weekly' :['ff','tbt','f4f','wcw'],
'adult' :['porn','sex','xxx','sexy','hot','pussy','ass','milf','boobs','adult','anal','tits'],
'tech' :['iphone','iphonegames','androidgames','ipad','ipadgames','gameinsight','android','itunes','nsfw','youtube'],
'general':['video','music','fashion','job','news','travel','movie','photography','business','love']}

all_tags = []
for cat in dicto:
    all_tags += dicto[cat]


def proc(txt):
    ret = ''
    for word in txt.split():
        if word[0] == '#':
            continue
        if word[0] == '@':
            continue
        if word[:4] == 'http':
            continue
        ret += word+' '
    return ret

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

for month in months:
    print "for the month of ", month
    assoc = {}
    twit = {}
    for cat in dicto:
        # if cat != 'tech':
        #     continue
        for tag in dicto[cat]:
            txt = ""
            mentions = 0
            # if tag != 'iphone':
            #     continue
            filename = "../extract/" + month + "/" + cat +"/" + tag + ".dat"
            with open(filename) as f:
                content = f.readlines()
            for tweet in content:
                tweet = ast.literal_eval(tweet)[tag]
                # print tweet
                if tag not in assoc:
                    assoc[tag] = {}
                for cotag in tweet[4]:
                    if cotag not in assoc[tag]:
                        assoc[tag][cotag] = 0
                    assoc[tag][cotag] += 1
                mentions += len(tweet[5])
                txt +=  tweet[2] + " "
            st = sorted(assoc[tag].items(), key=operator.itemgetter(1))
            s = 0
            l = 0
            for par in st:
                s += par[1]
                l += len(par[0])*par[1]
            avg = float(s)/st[-1][1]
            avlen = float(l)/s
            outfile = "../extract/cotags/" +  cat +"/" + tag + "/" + month + ".dat"
            if not os.path.exists(os.path.dirname(outfile)):
                os.makedirs(os.path.dirname(outfile))
            # with open(outfile, "a+") as f2:
            f2 = open(outfile, "a+")
            print >> f2, "hello"
            print >>f2,  "tweets =", len(content)
            print >>f2,  "avg =", avg
            print >>f2,  "avlen =", avlen
            print >>f2,  "mentions =", mentions
            print >>f2,  "text =", proc(txt)
            # print >>f2,  st
            # i = 0
            # for par in reversed(st):
            for par in st[::-1][:100]:
                # i += 1
                print >>f2,  par
                # if i > 100:
                #     break



# print sorted(assoc['iphone'].items(), key=operator.itemgetter(1))
