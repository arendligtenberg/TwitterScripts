#import modules
import sys
import tweepy
import json

#global variables

consumer_key = 'z0QhzPiZ6WWLUPSFX7pew'
consumer_secret = 'rJsq1Pl9SzfV7kptmXfGWCYdQvmxFwSufLoFY4VdwU'
token_key = '8874842-8bzWBWxtZrt5JIcvNEWggKjQTwE8nmJ9FKb5TJFPP3'
token_secret = 'WdeBNQimiWyATR76ZIgdulA7usQUG47Rp6zqbpIEZVSw7'

#Main function
def main():
    print sys.argv[0],'starts'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    print 'Connected to Twitter'
    api = tweepy.API(auth)


    print 'Experiment with cursor'
    print 'Get search method returns json objects'

    json_search = api.search(q="football")
    #json.loads(json_search())
    print  json_search


#Standard boilerplate to call main function if this file runs

if __name__ == '__main__':
    main()# imports

from pprint import pprint
