#import modules
import sys
import tweepy
import json
#from tweepy.parsers import JSONParser

#global variables


#consumer_key = 'z0QhzPiZ6WWLUPSFX7pew'
#consumer_secret = 'rJsq1Pl9SzfV7kptmXfGWCYdQvmxFwSufLoFY4VdwU'
#token_key = '8874842-8bzWBWxtZrt5JIcvNEWggKjQTwE8nmJ9FKb5TJFPP3'
#token_secret = 'WdeBNQimiWyATR76ZIgdulA7usQUG47Rp6zqbpIEZVSw7'

consumer_key = 'J0x4IMB3vCfgOOsXvxIZeOuPH'
consumer_secret = 'yHbnCVFLtJ0judgkxUlyvliUO6dl6MOzBjDvPfZCKHQilnnsx4'
token_key = '4492998268-4wETpb00W1xRci4VqDQGtY4vz6WpTJ4tq87PqY0'
token_secret = '5Jsqc0QVFWB7w31ROPKzOpoJaRpzMlk91qksytjW6NaP4'

#Main function
def main():
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(token_key, token_secret)
   api = tweepy.API(auth)
   query = '#grsscripting'
   #results = tweepy.Cursor(api.home_timeline).items(20)
   #results = [pages for pages in tweepy.Cursor(api.search, q=query).items(1)]
   #results = tweepy.Cursor(api.search(q=query,rpp=100,count=1000))
   #data = [s.text.encode('utf8') for s in results]
   results = tweepy.Cursor(api.search, q=query).items(1)
   print 'collecting tweets...'
   for tweet in results:
      #print dir(tweet)
      if tweet.user.geo_enabled:
         print "oke: "
         print tweet.coordinates
 
            


      #print tweet.text.encode('utf8')
      #print tweet
      #print tweet.author.has_extended_profile
      #u = pages.author
      #print u.profile_image_url
      #print u.location
      #print pages.source.encode('utf8')
      #if item.geo != None:
         #print item.geo['coordinates']
      #else: 
         #print  'no coordinate'
      print '-------------------------------------------'
   print 'done'



#Standard boilerplate to call main function if this file runs
if __name__ == '__main__':
    main()
    #search_tweets()

