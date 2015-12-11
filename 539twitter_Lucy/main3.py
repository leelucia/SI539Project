# Import the necessary methods from "twitter" library and flask
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

app.secret_key = 'WebDesign'

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '360747438-h0zsIc5F8GAJNTNwgatiyNVhVhMwm9p7KA1iKCaS'
ACCESS_SECRET = 'UfgpWYzwNjSnh6xZykYwxy18NWHUfkMkyJe4EezXLIgFQ'
CONSUMER_KEY = '1KOTCNYqNZrtc3dP2W4nniGF8'
CONSUMER_SECRET = 'fc2MjXDSONQQhBAQqOgySxs9ZubnTRF5bSGbpArtLC3bX8N2la'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

@app.route('/')
@app.route('/index')          						#This is the main URL
def index():
    return render_template("index.html", name = "index", title = "Home")

@app.route('/bladder')
def bladder():
# blcsm bladder cancer
    blcsmdict = twitter.search.tweets(q='#blcsm', count = 2)
    blcsmstatus = blcsmdict['statuses']
    blcsm_userList = []
    blcsm_tweetList = []
    blcsm_timeList = []
    blcsm_locationList = []

    blcsm_numbtweets = len(blcsmstatus)
    for i in range(blcsm_numbtweets):
        blcsm_userList = blcsmstatus[i]['user']['screen_name']
        blcsm_tweetList = blcsmstatus[i]['text']
        blcsm_locationList = blcsmstatus[i]['user']['location']
        blcsm_timeList = blcsmstatus[i]['created_at']
    return render_template("blcsm.html", name = "bladder cancer", title = "Bladder Cancer")

@app.route('/breast')
def breast():
    # bcsm breast cancer
    bcsmdict = twitter.search.tweets(q='#bcsm', count = 2)
    bcsmstatus = bcsmdict['statuses']
    bcsm_userList = []
    bcsm_tweetList = []
    bcsm_timeList = []
    bcsm_locationList = []

    bcsm_numbtweets = len(bcsmstatus)
    for i in range(bcsm_numbtweets):
        bcsm_userList = blcsmstatus[i]['user']['screen_name']
        bcsm_tweetList = blcsmstatus[i]['text']
        bcsm_locationList = blcsmstatus[i]['user']['location']
        bcsm_timeList = blcsmstatus[i]['created_at']
    return render_template("bcsm.html", name = "breast cancer", title = "Breast Cancer")

@app.route('/prostate')
def prostate():
    # pcsm prostate cancer
    pcsmdict = twitter.search.tweets(q='#pcsm', count = 2)
    pcsmstatus = pcsmdict['statuses']
    pcsm_userList = []
    pcsm_tweetList = []
    pcsm_timeList = []
    pcsm_locationList = []

    pcsm_numbtweets = len(pcsmstatus)
    for i in range(pcsm_numbtweets):
        pcsm_userList = pcsmstatus[i]['user']['screen_name']
        pcsm_tweetList = pcsmstatus[i]['text']
        pcsm_locationList = pcsmstatus[i]['user']['location']
        pcsm_timeList = pcsmstatus[i]['created_at']
    return render_template("pcsm.html", name = "prostate cancer", title = "Prostate Cancer")

@app.route('/lung')
def lung():
    # lcsm lung cancer
    lcsmdict = twitter.search.tweets(q='#lcsm', count = 2)
    lcsmstatus = pcsmdict['statuses']
    lcsm_userList = []
    lcsm_tweetList = []
    lcsm_timeList = []
    lcsm_locationList = []

    lcsm_numbtweets = len(lcsmstatus)
    for i in range(lcsm_numbtweets):
        lcsm_userList = lcsmstatus[i]['user']['screen_name']
        lcsm_tweetList = lcsmstatus[i]['text']
        lcsm_locationList = lcsmstatus[i]['user']['location']
        lcsm_timeList = lcsmstatus[i]['created_at']
    return render_template("lcsm.html", name = "lung cancer", title = "Lung Cancer")


if __name__ == '__main__':
    app.run(debug=True)
