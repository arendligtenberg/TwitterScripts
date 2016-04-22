#!/usr/bin/python
#TBV Module 6 opdracht Social Media
# Arend Ligtenberg / Wageningen Universitey / Nov. 2013
# Gebruik nu twython, maar tweepy is een alternatief. Moet de code wat omgeschreven worden

from twython import TwythonStreamer
import string, json, pprint
import urllib
from datetime import datetime
#from datetime import date
#from time import *
import string, os, sys, subprocess, time
import psycopg2

# get access to the twitter API
APP_KEY = '3PXJFtAYtia7CXFYEcAQDjyMW'
APP_SECRET = 'QcB5bNMjmp6JcoBqImyglvFhKM9kwWT4Qn1jC6qB9Q5Mi0k2oC'
OAUTH_TOKEN = '200857272-LHP8s5RDMgGheSgzDLLpFdhjqUKjHPmJXhX4gGgN'
OAUTH_TOKEN_SECRET = 'U4Q7kx9apYH5628G5gpDpzTulYsx7SKy2shkO95wropCx'
#twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Connect to a database
conn = psycopg2.connect("dbname=twitter user=postgres password=Module5")

# Open a cursor to perform database operations
cur = conn.cursor()

#Class to process JSON data comming from the twitter stream API. Extract relevant fields
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
         tweet_lat = 0.0
         tweet_lon = 0.0
	 tweet_name = ''
	 retweet_count = 0
	 # Can we use this to filter out popular tweets?

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


         if tweet_lat != 0:
                    #some elementary output to console    
                    print str(tweet_datetime)+", "+str(tweet_lat)+", "+str(tweet_lon)+": "+tweet_text
                    #insert into POSTGRESGL database (perhaps replace it in the future with a stored procedure for performance reasons)
                    cur.execute('INSERT INTO geotweets (tweet_id, tweet_datetime, tweet_text, latitude, longitude,tweet_name,retweet_count) VALUES (%s,%s,%s,%s,%s,%s,%s);', (tweet_id, tweet_datetime, tweet_text, tweet_lat,tweet_lon,tweet_name,retweet_count))
                    conn.commit()
                    
       # Added these parameters for network analysis Module 6.
                    
         if 'current_user_retweet' in data:
                    user_retweet = data['current_user_retweet']  
                    
         if 'in_reply_to_screen_name' in data:
                    Reply_to = data['in_reply_to_screen_name']
                    
         if 'in_reply_to_status_id' in data:
                    Reply_ID = data['in_reply_to_status_id']  
                    
         if 'place' in data:
                    Country = data['country']
                    Placename = data['full_name']                                                                                                                        
                    

    def on_error(self, status_code, data):
         print "OOPS FOUTJE: " +str(status_code)
         #self.disconnect()

# Start stream from twitter
try:

     stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
except ValueError:
     print 'OOPS! that hurts, something went wrong while making connection with Twitter: '+str(ValueError)

# Filter based on text --> Not sure if we still need this
#try:
#     stream.statuses.filter()
#except ValueError:
#     print 'OOPS! that hurts, something went wrong while getting the stream from Twitter: '+str(ValueError) 
                    













