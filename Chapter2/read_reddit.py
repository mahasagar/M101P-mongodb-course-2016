import json
import urllib2
import pymongo
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit
stories = db.stories

stories.drop();

reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])



