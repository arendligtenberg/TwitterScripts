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
#import psycopg2

# get access to the twitter API
APP_KEY = '3PXJFtAYtia7CXFYEcAQDjyMW'
APP_SECRET = 'QcB5bNMjmp6JcoBqImyglvFhKM9kwWT4Qn1jC6qB9Q5Mi0k2oC'
OAUTH_TOKEN = '200857272-LHP8s5RDMgGheSgzDLLpFdhjqUKjHPmJXhX4gGgN'
OAUTH_TOKEN_SECRET = 'U4Q7kx9apYH5628G5gpDpzTulYsx7SKy2shkO95wropCx'
#twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Connect to a database
#conn = psycopg2.connect("dbname=gis user=postgres password=Entrada001")

# Open a cursor to perform database operations
#cur = conn.cursor()

#Class to process JSON data comming from the twitter stream API. Extract relevant fields
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        tweet_lat = 0.0
        tweet_lon = 0.0
        tweet_name = ''
        retweet_count = 0
        place_lat = 0.0
        place_lon = 0.0
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

            # Added these parameters for network analysis Module 6.

        if 'places' in data:
            plaats = data['places']
            bb = plaats['bounding_box']
            if not plaats is None:
                latlon1 = bb[0]
                lat1 = latlon1[0]
                lon1 = latlon1[1]
                latlon2 = bb[1]
                lat2 = latlon2[0]
                lon2 = latlon2[1]
                latlon3 = bb[2]
                lat3 = latlon3[0]
                lon3 = latlon3[1]
                latlon4 = bb[3]
                lat4 = latlon4[0]
                lon4 = latlon4[1]
                place_lat = ((lat1 + lat2 + lat3 + lat4)/4)
                place_lon = ((lon1 + lon2 + lon3 + lon4)/4)
 
        if tweet_lat != 0:
            #some elementary output to console    
            print str(tweet_datetime)+", "+str(tweet_lat)+", "+str(tweet_lon)+": "+tweet_text
        else:
            if place_lat != 0:
                print str(tweet_datetime)+", "+str(place_lat)+", "+str(place_lon)+": "+tweet_text+"============================="
        
            #insert into POSTGRESGL database (perhaps replace it in the future with a stored procedure for performance reasons)
            #cur.execute('INSERT INTO gimatweets (tweet_id, tweet_datetime, tweet_text, latitude, longitude,tweet_name,retweet_count,place_lat,place_lon) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);', (tweet_id, tweet_datetime, tweet_text, tweet_lat,tweet_lon,tweet_name,retweet_count,place_lat,place_lon))
            #conn.commit()                                                                                                                                             
                    
    def on_error(self, status_code, data):
        print "OOPS FOUTJE: " +str(status_code)
        #self.disconnect()

# Start stream from twitter
try:
     stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
except ValueError:
     print 'OOPS! that hurts, something went wrong while making connection with Twitter: '+str(ValueError)

# Filter based on bounding box
try:
     #stream.statuses.filter(locations='3.00,50.00,7.35,53.65')
     #stream.statuses.filter(track=['terror','bomb','isis','terrorist','explosion','news','breaking'])
     stream.statuses.filter(follow=[759251,428333,807095,5402612,742143,36670025,1642135962,18424289,2673523800,4970411,6017542,23484039,15108702,18767649,87416722,384438102,38400130,620136960,19706851])
except ValueError:
     print 'OOPS! that hurts, something went wrong while getting the stream from Twitter: '+str(ValueError) 












