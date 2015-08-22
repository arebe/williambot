import tweepy, time, datetime, sys
import random

class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

twitter = TwitterAPI()


filename=open('truthtweets.txt','r')
f=filename.readlines()
filename.close()
replyText = random.choice(f)
replyText = replyText.replace('\n', '')
print replyText


tweets = twitter.api.search('"meaning of truth"')

print tweets[0].created_at
print tweets[0].text
print tweets[0].user.id
print tweets[0].id
print tweets[0].user.screen_name

replyUser = tweets[0].user.screen_name
replyTweet = tweets[0].id

#API.update_status(status[, in_reply_to_status_id][, lat][, long][, source][, place_id])
statusUpdate = replyText + " LOL @" + replyUser + " #truth"
print statusUpdate


#check if tweet happened within last few hours
sDate = tweets[0].created_at
age = time.time() - (sDate - datetime.datetime(1970,1,1)).total_seconds()
print age
if age < 86400:
    print statusUpdate
    twitter.api.update_status(status=statusUpdate, in_reply_to_status_id = replyTweet)