#import modules
import sys
import tweepy
import json

#global variables
auth

consumer_key = 'z0QhzPiZ6WWLUPSFX7pew'
consumer_secret = 'rJsq1Pl9SzfV7kptmXfGWCYdQvmxFwSufLoFY4VdwU'
token_key = '8874842-8bzWBWxtZrt5JIcvNEWggKjQTwE8nmJ9FKb5TJFPP3'
token_secret = 'WdeBNQimiWyATR76ZIgdulA7usQUG47Rp6zqbpIEZVSw7'

#Main function
def main():
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(token_key, token_secret)
   api = tweepy.API(auth)


def twitterfeed():
   api = tweepy.API(auth)
   statuses = tweepy.Cursor(api.home_timeline).items(20)
   data = [s.text.encode('utf8') for s in statuses]
   print data

#Standard boilerplate to call main function if this file runs

if __name__ == '__main__':
    main()
    twitterfeed()
