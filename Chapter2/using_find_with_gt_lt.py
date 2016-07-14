import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores

def find():
    print "in find"
    query = {type:'','score':{'$gt':50,'$lt':70}}

    try:
        cursor = scores.find(query)
    except Exception as e:
        print "unexpected error",type(e),e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity>10):
            break;
find()