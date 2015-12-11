from flask import Flask, render_template, request  #NEW IMPORT -- request
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


app = Flask(__name__)    #This is creating a new Flask object


#@app.route('/contact')   
#def contact():
#    return render_template("contact.html", name = "contact", title = "Contact Me")

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '360747438-h0zsIc5F8GAJNTNwgatiyNVhVhMwm9p7KA1iKCaS'
ACCESS_SECRET = 'UfgpWYzwNjSnh6xZykYwxy18NWHUfkMkyJe4EezXLIgFQ'
CONSUMER_KEY = '1KOTCNYqNZrtc3dP2W4nniGF8'
CONSUMER_SECRET = 'fc2MjXDSONQQhBAQqOgySxs9ZubnTRF5bSGbpArtLC3bX8N2la'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)


###code lines 25-41 are my current attempt and putting the tweets, time, and location for each hashtag search in nested dictionaries. Not sure if it works properly.
##There may be a better way to do this. open to ideas and am going to ask Yu-Jen
# cancerlist = ['#adsm','#ancsm','#bcsm','#ayacsm','#blcsm','#btsm','#crcsm','#esocsm','#gyncsm','#hncsm','#hpbcsm','#kcsm','#lcsm','#leusm','#lymsm','#melsm','#mmsm','#pancsm','#pcsm','#pedcsm','#scmsm','#stcsm','#thmsm','#thycsm','#tscsm']
# cancerdict = {}
# cancerdictstatus = {}
# tweet = {}
# timetweeted = {}
# location = {}



# # Feed code
# pullapi = []
# status = []
# username = []
# tweet = []
# time = []



# pullapi = twitter.search.tweets(q='#pcsm', count=5)
# pullapi_count = len(pullapi)
# print pullapi_count

# for i in range(pullapi_count):
#     # status = pullapi[i]['statuses']
#     username = pullapi[i]['user']['screen_name']
#     tweet = pullapi[i]['text']
#     time = pullapi[i]['created_at']
# print pullapi_count
# statusencoded = []
# statusencoded = [x.encode('UTF-8') for x in pullapi['statuses']]

# for x in statusencoded:
#     print statusencoded

# for status in statuses:
#     print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])





# blcsm bladder cancer
blcsmdict = twitter.search.tweets(q='#blcsm', count = 50)
blcsmstatus = blcsmdict['statuses']
blcsm_userList = []
blcsm_tweetList = []
blcsm_timeList = []
blcsm_locationList = []
blcsm_hoursList = []
#Feed page vars
blcsm_tweetFeed = []
blcsm_userFeed = []
blcsm_hoursFeed = []

blcsm_numbtweets = len(blcsmstatus)
for i in range(blcsm_numbtweets):
    blcsm_userList = blcsmstatus[i]['user']['screen_name']
    blcsm_tweetList = blcsmstatus[i]['text']
    blcsm_locationList = blcsmstatus[i]['user']['location']
    blcsm_timeList = blcsmstatus[i]['created_at']
    blcsm_hoursList.append(blcsm_timeList[11:13])
    blcsm_hoursListSorted = sorted(blcsm_hoursList)
    #Feed page stuff
    blcsm_tweetFeed.append(blcsm_tweetList[:])
    blcsm_userFeed.append(blcsm_userList[:])
    blcsm_hoursFeed.append(blcsm_hoursList[:])


blcsm_hoursListSortedEncoded = [x.encode('UTF-8') for x in blcsm_hoursListSorted]
blcsm_hoursListFinal = map(int, blcsm_hoursListSortedEncoded)
# print blcsm_hoursListFinal
blcsm_hoursCount_0 = blcsm_hoursListFinal.count(0)
blcsm_hoursCount_1 = blcsm_hoursListFinal.count(1)
blcsm_hoursCount_2 = blcsm_hoursListFinal.count(2)
blcsm_hoursCount_3 = blcsm_hoursListFinal.count(3)
blcsm_hoursCount_4 = blcsm_hoursListFinal.count(4)
blcsm_hoursCount_5 = blcsm_hoursListFinal.count(5)
blcsm_hoursCount_6 = blcsm_hoursListFinal.count(6)
blcsm_hoursCount_7 = blcsm_hoursListFinal.count(7)
blcsm_hoursCount_8 = blcsm_hoursListFinal.count(8)
blcsm_hoursCount_9 = blcsm_hoursListFinal.count(9)
blcsm_hoursCount_10 = blcsm_hoursListFinal.count(10)
blcsm_hoursCount_11 = blcsm_hoursListFinal.count(11)
blcsm_hoursCount_12 = blcsm_hoursListFinal.count(12)
blcsm_hoursCount_13 = blcsm_hoursListFinal.count(13)
blcsm_hoursCount_14 = blcsm_hoursListFinal.count(14)
blcsm_hoursCount_15 = blcsm_hoursListFinal.count(15)
blcsm_hoursCount_16 = blcsm_hoursListFinal.count(16)
blcsm_hoursCount_17 = blcsm_hoursListFinal.count(17)
blcsm_hoursCount_18 = blcsm_hoursListFinal.count(18)
blcsm_hoursCount_19 = blcsm_hoursListFinal.count(19)
blcsm_hoursCount_20 = blcsm_hoursListFinal.count(20)
blcsm_hoursCount_21 = blcsm_hoursListFinal.count(21)
blcsm_hoursCount_22 = blcsm_hoursListFinal.count(22)
blcsm_hoursCount_23 = blcsm_hoursListFinal.count(23)
# print blcsm_hoursCount_14, blcsm_hoursCount_15



# bcsm breast cancer
bcsmdict = twitter.search.tweets(q='#bcsm', count = 50) # count = whateva
bcsmstatus = bcsmdict['statuses']
bcsm_userList = []
bcsm_tweetList = []
bcsm_timeList = []
bcsm_locationList = []
bcsm_hoursList = []
#Feed page vars
bcsm_tweetFeed = []
bcsm_userFeed = []
bcsm_hoursFeed = []

bcsm_numbtweets = len(bcsmstatus)
for i in range(bcsm_numbtweets):
    bcsm_userList = bcsmstatus[i]['user']['screen_name']
    bcsm_tweetList = bcsmstatus[i]['text']
    bcsm_locationList = bcsmstatus[i]['user']['location']
    bcsm_timeList = bcsmstatus[i]['created_at']
    bcsm_hoursList.append(bcsm_timeList[11:13])
    bcsm_hoursListSorted = sorted(bcsm_hoursList)
    #Feed page stuff
    bcsm_tweetFeed.append(bcsm_tweetList[:])
    bcsm_userFeed.append(bcsm_userList[:])
    bcsm_hoursFeed.append(bcsm_hoursList[:])


bcsm_hoursListSortedEncoded = [x.encode('UTF-8') for x in bcsm_hoursListSorted]
bcsm_hoursListFinal = map(int, bcsm_hoursListSortedEncoded)
# print bcsm_hoursListFinal
bcsm_hoursCount_0 = bcsm_hoursListFinal.count(0)
bcsm_hoursCount_1 = bcsm_hoursListFinal.count(1)
bcsm_hoursCount_2 = bcsm_hoursListFinal.count(2)
bcsm_hoursCount_3 = bcsm_hoursListFinal.count(3)
bcsm_hoursCount_4 = bcsm_hoursListFinal.count(4)
bcsm_hoursCount_5 = bcsm_hoursListFinal.count(5)
bcsm_hoursCount_6 = bcsm_hoursListFinal.count(6)
bcsm_hoursCount_7 = bcsm_hoursListFinal.count(7)
bcsm_hoursCount_8 = bcsm_hoursListFinal.count(8)
bcsm_hoursCount_9 = bcsm_hoursListFinal.count(9)
bcsm_hoursCount_10 = bcsm_hoursListFinal.count(10)
bcsm_hoursCount_11 = bcsm_hoursListFinal.count(11)
bcsm_hoursCount_12 = bcsm_hoursListFinal.count(12)
bcsm_hoursCount_13 = bcsm_hoursListFinal.count(13)
bcsm_hoursCount_14 = bcsm_hoursListFinal.count(14)
bcsm_hoursCount_15 = bcsm_hoursListFinal.count(15)
bcsm_hoursCount_16 = bcsm_hoursListFinal.count(16)
bcsm_hoursCount_17 = bcsm_hoursListFinal.count(17)
bcsm_hoursCount_18 = bcsm_hoursListFinal.count(18)
bcsm_hoursCount_19 = bcsm_hoursListFinal.count(19)
bcsm_hoursCount_20 = bcsm_hoursListFinal.count(20)
bcsm_hoursCount_21 = bcsm_hoursListFinal.count(21)
bcsm_hoursCount_22 = bcsm_hoursListFinal.count(22)
bcsm_hoursCount_23 = bcsm_hoursListFinal.count(23)
# print bcsm_hoursCount_14, bcsm_hoursCount_15





# pcsm prostate cancerr
pcsmdict = twitter.search.tweets(q='#pcsm', count = 50)
pcsmstatus = pcsmdict['statuses']
pcsm_userList = []
pcsm_tweetList = []
pcsm_timeList = []
pcsm_locationList = []
pcsm_hoursList = []
#Feed page vars
pcsm_tweetFeed = []
pcsm_userFeed = []
pcsm_hoursFeed = []

pcsm_numbtweets = len(pcsmstatus)
for i in range(pcsm_numbtweets):
    pcsm_userList = pcsmstatus[i]['user']['screen_name']
    pcsm_tweetList = pcsmstatus[i]['text']
    pcsm_locationList = pcsmstatus[i]['user']['location']
    pcsm_timeList = pcsmstatus[i]['created_at']
    pcsm_hoursList.append(pcsm_timeList[11:13])
    pcsm_hoursListSorted = sorted(pcsm_hoursList)
    #Feed page stuff
    pcsm_tweetFeed.append(pcsm_tweetList[:])
    pcsm_userFeed.append(pcsm_userList[:])
    pcsm_hoursFeed.append(pcsm_hoursList[:])

pcsm_hoursListSortedEncoded = [x.encode('UTF-8') for x in pcsm_hoursListSorted]
pcsm_hoursListFinal = map(int, pcsm_hoursListSortedEncoded)
# print pcsm_hoursListFinal
pcsm_hoursCount_0 = pcsm_hoursListFinal.count(0)
pcsm_hoursCount_1 = pcsm_hoursListFinal.count(1)
pcsm_hoursCount_2 = pcsm_hoursListFinal.count(2)
pcsm_hoursCount_3 = pcsm_hoursListFinal.count(3)
pcsm_hoursCount_4 = pcsm_hoursListFinal.count(4)
pcsm_hoursCount_5 = pcsm_hoursListFinal.count(5)
pcsm_hoursCount_6 = pcsm_hoursListFinal.count(6)
pcsm_hoursCount_7 = pcsm_hoursListFinal.count(7)
pcsm_hoursCount_8 = pcsm_hoursListFinal.count(8)
pcsm_hoursCount_9 = pcsm_hoursListFinal.count(9)
pcsm_hoursCount_10 = pcsm_hoursListFinal.count(10)
pcsm_hoursCount_11 = pcsm_hoursListFinal.count(11)
pcsm_hoursCount_12 = pcsm_hoursListFinal.count(12)
pcsm_hoursCount_13 = pcsm_hoursListFinal.count(13)
pcsm_hoursCount_14 = pcsm_hoursListFinal.count(14)
pcsm_hoursCount_15 = pcsm_hoursListFinal.count(15)
pcsm_hoursCount_16 = pcsm_hoursListFinal.count(16)
pcsm_hoursCount_17 = pcsm_hoursListFinal.count(17)
pcsm_hoursCount_18 = pcsm_hoursListFinal.count(18)
pcsm_hoursCount_19 = pcsm_hoursListFinal.count(19)
pcsm_hoursCount_20 = pcsm_hoursListFinal.count(20)
pcsm_hoursCount_21 = pcsm_hoursListFinal.count(21)
pcsm_hoursCount_22 = pcsm_hoursListFinal.count(22)
pcsm_hoursCount_23 = pcsm_hoursListFinal.count(23)
# print pcsm_hoursCount_14, pcsm_hoursCount_15



# lcsm lung cancer
lcsmdict = twitter.search.tweets(q='#lcsm', count = 50)
lcsmstatus = lcsmdict['statuses']
lcsm_userList = []
lcsm_tweetList = []
lcsm_timeList = []
lcsm_locationList = []
lcsm_hoursList = []
#Feed page vars
lcsm_tweetFeed = []
lcsm_userFeed = []
lcsm_hoursFeed = []

lcsm_numbtweets = len(lcsmstatus)
for i in range(lcsm_numbtweets):
    lcsm_userList = lcsmstatus[i]['user']['screen_name']
    lcsm_tweetList = lcsmstatus[i]['text']
    lcsm_locationList = lcsmstatus[i]['user']['location']
    lcsm_timeList = lcsmstatus[i]['created_at']
    lcsm_hoursList.append(lcsm_timeList[11:13])
    lcsm_hoursListSorted = sorted(lcsm_hoursList)
    #Feed page stuff
    lcsm_tweetFeed.append(lcsm_tweetList[:])
    lcsm_userFeed.append(lcsm_userList[:])
    lcsm_hoursFeed.append(lcsm_hoursList[:])


lcsm_hoursListSortedEncoded = [x.encode('UTF-8') for x in lcsm_hoursListSorted]
lcsm_hoursListFinal = map(int, lcsm_hoursListSortedEncoded)
# print lcsm_hoursListFinal
lcsm_hoursCount_0 = lcsm_hoursListFinal.count(0)
lcsm_hoursCount_1 = lcsm_hoursListFinal.count(1)
lcsm_hoursCount_2 = lcsm_hoursListFinal.count(2)
lcsm_hoursCount_3 = lcsm_hoursListFinal.count(3)
lcsm_hoursCount_4 = lcsm_hoursListFinal.count(4)
lcsm_hoursCount_5 = lcsm_hoursListFinal.count(5)
lcsm_hoursCount_6 = lcsm_hoursListFinal.count(6)
lcsm_hoursCount_7 = lcsm_hoursListFinal.count(7)
lcsm_hoursCount_8 = lcsm_hoursListFinal.count(8)
lcsm_hoursCount_9 = lcsm_hoursListFinal.count(9)
lcsm_hoursCount_10 = lcsm_hoursListFinal.count(10)
lcsm_hoursCount_11 = lcsm_hoursListFinal.count(11)
lcsm_hoursCount_12 = lcsm_hoursListFinal.count(12)
lcsm_hoursCount_13 = lcsm_hoursListFinal.count(13)
lcsm_hoursCount_14 = lcsm_hoursListFinal.count(14)
lcsm_hoursCount_15 = lcsm_hoursListFinal.count(15)
lcsm_hoursCount_16 = lcsm_hoursListFinal.count(16)
lcsm_hoursCount_17 = lcsm_hoursListFinal.count(17)
lcsm_hoursCount_18 = lcsm_hoursListFinal.count(18)
lcsm_hoursCount_19 = lcsm_hoursListFinal.count(19)
lcsm_hoursCount_20 = lcsm_hoursListFinal.count(20)
lcsm_hoursCount_21 = lcsm_hoursListFinal.count(21)
lcsm_hoursCount_22 = lcsm_hoursListFinal.count(22)
lcsm_hoursCount_23 = lcsm_hoursListFinal.count(23)
# print lcsm_hoursCount_14, lcsm_hoursCount_15


	



@app.route('/')                     #This is the main URL
@app.route('/index')
def index():
    return render_template("index.html", name = "index", title = "Twitter Cancer Hashtags")

@app.route('/resources')
def resources():
    return render_template("resources.html", name = "resources", title = "Resources Utilized")

@app.route('/donut')   
def donut():
    return render_template("donut.html", 
    	name = "donut", 
    	title = "Hashtag Counts", 
    	blcsm_numbtweets=blcsm_numbtweets,
    	blcsm_userList=blcsm_userList,
    	blcsm_tweetList=blcsm_tweetList,
    	blcsm_locationList=blcsm_locationList,
    	blcsm_timeList=blcsm_timeList,
    	bcsm_numbtweets=bcsm_numbtweets,
    	pcsm_numbtweets=pcsm_numbtweets,
    	lcsm_numbtweets=lcsm_numbtweets,)

@app.route('/line')   
def line():
    return render_template("line.html", 
    	name="line", 
    	title = "Hashtags Over Time",
        blcsm_hoursCount_0 = blcsm_hoursCount_0,
        blcsm_hoursCount_1 = blcsm_hoursCount_1,
        blcsm_hoursCount_2 = blcsm_hoursCount_2,
        blcsm_hoursCount_3 = blcsm_hoursCount_3,
        blcsm_hoursCount_4 = blcsm_hoursCount_4,
        blcsm_hoursCount_5 = blcsm_hoursCount_5,
        blcsm_hoursCount_6 = blcsm_hoursCount_6,
        blcsm_hoursCount_7 = blcsm_hoursCount_7,
        blcsm_hoursCount_8 = blcsm_hoursCount_8,
        blcsm_hoursCount_9 = blcsm_hoursCount_9,
        blcsm_hoursCount_10 = blcsm_hoursCount_10,
        blcsm_hoursCount_11 = blcsm_hoursCount_11,
        blcsm_hoursCount_12 = blcsm_hoursCount_12,
        blcsm_hoursCount_13 = blcsm_hoursCount_13,
        blcsm_hoursCount_14 = blcsm_hoursCount_14,
        blcsm_hoursCount_15 = blcsm_hoursCount_15,
        blcsm_hoursCount_16 = blcsm_hoursCount_16,
        blcsm_hoursCount_17 = blcsm_hoursCount_17,
        blcsm_hoursCount_18 = blcsm_hoursCount_18,
        blcsm_hoursCount_19 = blcsm_hoursCount_19,
        blcsm_hoursCount_20 = blcsm_hoursCount_20,
        blcsm_hoursCount_21 = blcsm_hoursCount_21,
        blcsm_hoursCount_22 = blcsm_hoursCount_22,
        blcsm_hoursCount_23 = blcsm_hoursCount_23,
        bcsm_hoursCount_0 = bcsm_hoursCount_0,
        bcsm_hoursCount_1 = bcsm_hoursCount_1,
        bcsm_hoursCount_2 = bcsm_hoursCount_2,
        bcsm_hoursCount_3 = bcsm_hoursCount_3,
        bcsm_hoursCount_4 = bcsm_hoursCount_4,
        bcsm_hoursCount_5 = bcsm_hoursCount_5,
        bcsm_hoursCount_6 = bcsm_hoursCount_6,
        bcsm_hoursCount_7 = bcsm_hoursCount_7,
        bcsm_hoursCount_8 = bcsm_hoursCount_8,
        bcsm_hoursCount_9 = bcsm_hoursCount_9,
        bcsm_hoursCount_10 = bcsm_hoursCount_10,
        bcsm_hoursCount_11 = bcsm_hoursCount_11,
        bcsm_hoursCount_12 = bcsm_hoursCount_12,
        bcsm_hoursCount_13 = bcsm_hoursCount_13,
        bcsm_hoursCount_14 = bcsm_hoursCount_14,
        bcsm_hoursCount_15 = bcsm_hoursCount_15,
        bcsm_hoursCount_16 = bcsm_hoursCount_16,
        bcsm_hoursCount_17 = bcsm_hoursCount_17,
        bcsm_hoursCount_18 = bcsm_hoursCount_18,
        bcsm_hoursCount_19 = bcsm_hoursCount_19,
        bcsm_hoursCount_20 = bcsm_hoursCount_20,
        bcsm_hoursCount_21 = bcsm_hoursCount_21,
        bcsm_hoursCount_22 = bcsm_hoursCount_22,
        bcsm_hoursCount_23 = bcsm_hoursCount_23,
        pcsm_hoursCount_0 = pcsm_hoursCount_0,
        pcsm_hoursCount_1 = pcsm_hoursCount_1,
        pcsm_hoursCount_2 = pcsm_hoursCount_2,
        pcsm_hoursCount_3 = pcsm_hoursCount_3,
        pcsm_hoursCount_4 = pcsm_hoursCount_4,
        pcsm_hoursCount_5 = pcsm_hoursCount_5,
        pcsm_hoursCount_6 = pcsm_hoursCount_6,
        pcsm_hoursCount_7 = pcsm_hoursCount_7,
        pcsm_hoursCount_8 = pcsm_hoursCount_8,
        pcsm_hoursCount_9 = pcsm_hoursCount_9,
        pcsm_hoursCount_10 = pcsm_hoursCount_10,
        pcsm_hoursCount_11 = pcsm_hoursCount_11,
        pcsm_hoursCount_12 = pcsm_hoursCount_12,
        pcsm_hoursCount_13 = pcsm_hoursCount_13,
        pcsm_hoursCount_14 = pcsm_hoursCount_14,
        pcsm_hoursCount_15 = pcsm_hoursCount_15,
        pcsm_hoursCount_16 = pcsm_hoursCount_16,
        pcsm_hoursCount_17 = pcsm_hoursCount_17,
        pcsm_hoursCount_18 = pcsm_hoursCount_18,
        pcsm_hoursCount_19 = pcsm_hoursCount_19,
        pcsm_hoursCount_20 = pcsm_hoursCount_20,
        pcsm_hoursCount_21 = pcsm_hoursCount_21,
        pcsm_hoursCount_22 = pcsm_hoursCount_22,
        pcsm_hoursCount_23 = pcsm_hoursCount_23,
        lcsm_hoursCount_0 = lcsm_hoursCount_0,
        lcsm_hoursCount_1 = lcsm_hoursCount_1,
        lcsm_hoursCount_2 = lcsm_hoursCount_2,
        lcsm_hoursCount_3 = lcsm_hoursCount_3,
        lcsm_hoursCount_4 = lcsm_hoursCount_4,
        lcsm_hoursCount_5 = lcsm_hoursCount_5,
        lcsm_hoursCount_6 = lcsm_hoursCount_6,
        lcsm_hoursCount_7 = lcsm_hoursCount_7,
        lcsm_hoursCount_8 = lcsm_hoursCount_8,
        lcsm_hoursCount_9 = lcsm_hoursCount_9,
        lcsm_hoursCount_10 = lcsm_hoursCount_10,
        lcsm_hoursCount_11 = lcsm_hoursCount_11,
        lcsm_hoursCount_12 = lcsm_hoursCount_12,
        lcsm_hoursCount_13 = lcsm_hoursCount_13,
        lcsm_hoursCount_14 = lcsm_hoursCount_14,
        lcsm_hoursCount_15 = lcsm_hoursCount_15,
        lcsm_hoursCount_16 = lcsm_hoursCount_16,
        lcsm_hoursCount_17 = lcsm_hoursCount_17,
        lcsm_hoursCount_18 = lcsm_hoursCount_18,
        lcsm_hoursCount_19 = lcsm_hoursCount_19,
        lcsm_hoursCount_20 = lcsm_hoursCount_20,
        lcsm_hoursCount_21 = lcsm_hoursCount_21,
        lcsm_hoursCount_22 = lcsm_hoursCount_22,
        lcsm_hoursCount_23 = lcsm_hoursCount_23
    	)


@app.route('/feed')   
def feed():
    return render_template("feed.html",
        name="feed", 
        title = "Most Recent Tweets",
        blcsm_tweetFeed=blcsm_tweetFeed,
        blcsm_userFeed=blcsm_userFeed,
        blcsm_hoursFeed=blcsm_hoursFeed,
        bcsm_tweetFeed=bcsm_tweetFeed,
        bcsm_userFeed=bcsm_userFeed,
        bcsm_hoursFeed=bcsm_hoursFeed,
        pcsm_tweetFeed=pcsm_tweetFeed,
        pcsm_userFeed=pcsm_userFeed,
        pcsm_hoursFeed=pcsm_hoursFeed,
        lcsm_tweetFeed=lcsm_tweetFeed,
        lcsm_userFeed=lcsm_userFeed,
        lcsm_hoursFeed=lcsm_hoursFeed) 

@app.route('/about')   
def about():
    return render_template("about.html",
        name="feed", 
        title = "About") 

if __name__ == '__main__':
    app.run(debug=True)   #debug=True is optional 



