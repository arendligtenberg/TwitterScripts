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


##codes to access twitter API. 
APP_KEY = 'J0x4IMB3vCfgOOsXvxIZeOuPH'
APP_SECRET = 'yHbnCVFLtJ0judgkxUlyvliUO6dl6MOzBjDvPfZCKHQilnnsx4'
OAUTH_TOKEN = '4492998268-4wETpb00W1xRci4VqDQGtY4vz6WpTJ4tq87PqY0'
OAUTH_TOKEN_SECRET = '5Jsqc0QVFWB7w31ROPKzOpoJaRpzMlk91qksytjW6NaP4'

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
#ACCESS_TOKEN = twitter.obtain_access_token()

##exectuting query
##result: JSON with Tweets

search_results = twitter.search(q='#amsterdam', geocode='52.08174,6.45327,250km', count=100)
##parsing out 
for tweet in search_results["statuses"]:
    print tweet['user']['screen_name']
    print tweet['user']['followers_count']
    print tweet['text']
    if tweet['place'] != None:
        print tweet['place']['full_name']
        print tweet['place']['place_type']    
        coordinates = tweet['coordinates']
    if tweet['coordinates'] != None:
        coordinates = tweet['coordinates']
        print coordinates['coordinates'][0]
        print coordinates['coordinates'][1]
    print '==========================='
