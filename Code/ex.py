from os import listdir
from os.path import isfile, join
import gzip
import json
import os
month = "Sep"
print month
mypath = "../" + month
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
dicto = {'follow' :['follow','openfollow','tfb','followtrick','tfbjp','teamfollowback','follow2befollowed','followback','sougofollow','anotherfollowtrain','tcfollowtrain','tityfollowtrain','hitfollowsteam','followme'],
'weekly' :['ff','tbt','f4f','wcw'],
'adult' :['porn','sex','xxx','sexy','hot','pussy','ass','milf','boobs','adult','anal','tits'],
'tech' :['iphone','iphonegames','androidgames','ipad','ipadgames','gameinsight','android','itunes','nsfw','youtube'],
'general':['video','music','fashion','job','news','travel','movie','photography','business','love']}

c = 0
print "total files = ", len(onlyfiles)
for f in onlyfiles:
    print c
    with gzip.open(mypath+"/"+f, 'rb') as f:
        # file_content = f.read()
        # print file_content
        a = json.load(f)
        # print a.keys()
        for cat in dicto:
            for tag in dicto[cat]:
                # if tag == 'unprogramaparaadriana':
                #     print tag
                if tag in a:
                    # ret = a[tag]
                    for tweet in a[tag]:
                        if tweet[3]=='en':
                            filename = "../extract/" + month + "/" + cat +"/" + tag + ".dat"
                            if not os.path.exists(os.path.dirname(filename)):
                                os.makedirs(os.path.dirname(filename))
                            with open(filename,"a+") as extract:
                                json.dump({tag:tweet},extract)
                                extract.write('\n')


    c+=1
    # if c>5:
    #     break