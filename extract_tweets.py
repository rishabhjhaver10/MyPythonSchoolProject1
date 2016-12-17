from twython import TwythonStreamer
#!pip install Twython
#from time import sleep
import sys
import json
 
tweets = []
 
class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''
 
    # overriding
    def on_success(self, data):
        try:
            if data['lang'] == 'en':
                tweets.append(data)
                #sleep(1)
                print 'received tweet #', len(tweets), data['text'][:100]
        except:
            pass
            
 
        if len(tweets) >= 1000:
            self.store_json()
            self.disconnect()
            return False 
 
    # overriding
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
 
    def store_json(self):
        with open('tweet_stream_coordinates_{}_{}.json'.format(keyword, len(tweets)), 'w') as f:
            json.dump(tweets, f, indent=4)
 
 
if __name__ == '__main__':
 
   # with open('rishabh_twitter_credentials.json', 'r') as f:
       # credentials = json.load(f)
 
    # create your own app to get consumer key and secret
    CONSUMER_KEY = 'NZ1FizZQd5WFTmD80fMEjd0Dy'
    CONSUMER_SECRET = 'QcaeutLbfFnWGqej7KjxOTscNBXxoaAUrjEbuwJ0lJNENNIZiM'
    ACCESS_TOKEN = '706899266048888833-5GPUGduDjRDjHQqwoLcJLZlXRtDdfmo'
    ACCESS_TOKEN_SECRET = 'fYQbUvCYLvdCItt54B27TVoCvhMmchpHi7wJrkVqq7WFQ'
 
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'Washington DC'
 
    stream.statuses.filter(locations='-77.10, 38.46, -76.50, 38.59')

