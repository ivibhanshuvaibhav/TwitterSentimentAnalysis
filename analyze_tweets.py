from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import analyze_model as twitter
from credentials import *

MAX_NUM_TWEETS = 100

keyword = 'Modi'

class listener(StreamListener):

    def __init__(self):
        self.count = 0

    def on_data(self, data):
        try:

            self.count += 1
            tweet = data.split('","text":"')[1].split('","source":')[0].split('","display_text_range":')[0]
            print tweet
            twitter.analysis(tweet)

            if self.count >= MAX_NUM_TWEETS:
                return False
            return True

        except BaseException, e:
            print "Exception occured: " + str(e)
            time.sleep(5)

    def on_error(self, status):
        print "Error occured: " + status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])