import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json


# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

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

# def cancersearch():
#     for i in cancerlist:
#         cancerdict[i] = twitter.search.tweets(q=i)
#         cancerdictstatus[i] = cancerdict[i]['statuses']
#         for x in cancerdictstatus[i]:
#             tweet[i] = x['text']
#             timetweeted[i] = x['created_at']
#             location[i] = x['geo']

# cancersearch()

adsmdict = twitter.search.tweets(q='#pcsm', count=1)
status = adsmdict['statuses']
username = status[0]['user']['screen_name']
tweet = status[0]['text']
time = status[0]['created_at']

###code below is what I used to make sure I was getting the tweet
# def adcsm():
#     adsmdict = {}
#     adsmdict = twitter.search.tweets(q='#adcsm', count=1)
#     adcsmstatus = bcsmdict['statuses']
#
#     for i in status:
#         adcsmtweet = i['text']
#         adcsmtimetweeted = i['created_at']
#         adcsmlocation = i['geo']
        #add code to write tweet to mysql database


#print status[0]['text']
