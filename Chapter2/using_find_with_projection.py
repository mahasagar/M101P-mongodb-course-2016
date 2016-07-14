import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
scores = db.scores

def find():
        print "find , reporting for duty"
        query = {}
        projection = {'student_id':1,'_id':0}

        try:
            cursor = scores.find(query,projection)
        except Exception as e:
            print "unexpected error",type(e),e
        sanity = 0
        for doc in cursor:
            print doc
            sanity += 1
            if (sanity>10):
                break;

find()