##Example script harvesting tweet using REST api
##Arend Ligtenberg, GIRS, jan 2016stt
##Just simple Python scripting mode, so no classes etc.


from twython import Twython
import json
import datetime


##some date time stuff, may be handy for generating unique filename
#now = datetime.datetime.now()
#day=int(now.day)
#month=int(now.month)
#year=int(now.year)


# get access to the twitter API
APP_KEY = '3PXJFtAYtia7CXFYEcAQDjyMW'
APP_SECRET = 'QcB5bNMjmp6JcoBqImyglvFhKM9kwWT4Qn1jC6qB9Q5Mi0k2oC'
OAUTH_TOKEN = '200857272-LHP8s5RDMgGheSgzDLLpFdhjqUKjHPmJXhX4gGgN'
OAUTH_TOKEN_SECRET = 'U4Q7kx9apYH5628G5gpDpzTulYsx7SKy2shkO95wropCx'
#twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
#ACCESS_TOKEN = twitter.obtain_access_token()

##exectuting query
##result: JSON with Tweets

search_results = twitter.search(q='Ruppert', count=500)
##parsing out 
for tweet in search_results["statuses"]:
    if tweet['place'] != None:
        print tweet['place']['full_name']
        print tweet['place']['place_type']    
        coordinates = tweet['coordinates']
        print tweet['user']['screen_name']
        print tweet['user']['followers_count']
        print tweet['text']
        print tweet['retweet_count']
        print tweet['place']
        print tweet['created_at'] 
        if tweet['coordinates'] != None:
            coordinates = tweet['coordinates']
            print coordinates['coordinates'][0]
            print coordinates['coordinates'][1]
        print '==========================='
