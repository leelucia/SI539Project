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

#blcsm bladder cancer
blcsmdict = twitter.search.tweets(q='#blcsm', count = 100)
blcsmstatus = blcsmdict['statuses']
blcsmusername = blcsmstatus[0]['user']['screen_name']
blcsmtweet = blcsmstatus[0]['text']
blcsmlocation =  blcsmstatus[0]['user']['location']
blcsmtime = blcsmstatus[0]['created_at']


#bcsm breast cancer
bcsmdict = twitter.search.tweets(q='#bcsm', count = 100)
bcsmstatus = bcsmdict['statuses']
bcsmusername = bcsmstatus[0]['user']['screen_name']
bcsmtweet = bcsmstatus[0]['text']
bcsmlocation =  bcsmstatus[0]['user']['location']
bcsmtime = bcsmstatus[0]['created_at']

#pcsm prostate cancer
pcsmdict = twitter.search.tweets(q='#pcsm', count = 100)
pcsmstatus = pcsmdict['statuses']
pcsmusername = pcsmstatus[0]['user']['screen_name']
pcsmtweet = pcsmstatus[0]['text']
pcsmlocation =  pcsmstatus[0]['user']['location']
pcsmtime = pcsmstatus[0]['created_at']

#lcsm lung cancer
lcsmdict = twitter.search.tweets(q='#lcsm', count = 100)
lcsmstatus = lcsmdict['statuses']
lcsmusername = lcsmstatus[0]['user']['screen_name']
lcsmtweet = lcsmstatus[0]['text']
lcsmlocation =  lcsmstatus[0]['user']['location']
lcsmtime = lcsmstatus[0]['created_at']
