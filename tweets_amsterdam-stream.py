#Arend Ligtenberg
#Wageningen University
#Nov 2013
# update jan 2016
#even wat onzin tekst

#===============================

from twython import TwythonStreamer
import string, json, pprint
import urllib
from datetime import datetime
#from datetime import date
#from time import *
import string, os, sys, subprocess, time
import psycopg2

# get access to the twitter API
APP_KEY = 'J0x4IMB3vCfgOOsXvxIZeOuPH'
APP_SECRET = 'yHbnCVFLtJ0judgkxUlyvliUO6dl6MOzBjDvPfZCKHQilnnsx4'
OAUTH_TOKEN = '4492998268-4wETpb00W1xRci4VqDQGtY4vz6WpTJ4tq87PqY0'
OAUTH_TOKEN_SECRET = '5Jsqc0QVFWB7w31ROPKzOpoJaRpzMlk91qksytjW6NaP4'

output_file = 'result_'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.csv' 


#Class to process JSON data comming from the twitter stream API. Extract relevant fields
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
         tweet_lat = 0.0
         tweet_lon = 0.0
         tweet_name = ""
         retweet_count = 0

         if 'id' in data:
               tweet_id = data['id']
         if 'text' in data:
               tweet_text = data['text'].encode('utf-8').replace("'","''").replace(';','')
         if 'coordinates' in data:    
               geo = data['coordinates']
               if not geo is None:
                    latlon = geo['coordinates']
                    tweet_lon = latlon[0]
                    tweet_lat= latlon[1]
         if 'created_at' in data:
                    dt = data['created_at']
                    tweet_datetime = datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')

         if 'user' in data:
                    users = data['user']
                    tweet_name = users['screen_name']

         if 'retweet_count' in data:
                    retweet_count = data['retweet_count']
                    
         #if tweet_lat != 0:
         #some elementary output to console    
         string_to_write = str(tweet_datetime)+", "+str(tweet_lat)+", "+str(tweet_lon)+": "+str(tweet_text)
         print string_to_write
         #write_tweet(string_to_write)

                 
    def on_error(self, status_code, data):
         print "OOPS FOUTJE: " +str(status_code)
         #self.disconnect

    
def write_tweet(t):
    target = open(output_file, 'a')
    target.write(t)
    target.write('\n')
    target.close()
        
##main procedure
def main():
    try:
        stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        print 'Connecting to twitter: will take a minute'
    except ValueError:
        print 'OOPS! that hurts, something went wrong while making connection with Twitter: '+str(ValueError)
    #global target
    
    
    # Filter based on bounding box
    try:
        stream.statuses.filter(locations='4.47,52.19,4.58,52.25')
    except ValueError:
        print 'OOPS! that hurts, something went wrong while getting the stream from Twitter: '+str(ValueError)


                
if __name__ == '__main__':
    main()














# Send a query to twitter
#results = twitter.search(q='arend_l')

# Get the tweets out of the results
#tweets = results['statuses']
#pprint.pprint(tweets)

#iterate over the tweets
#for tweet in tweets:
     #print result
#     tweettext = tweet['text']
     #print tweettext
