import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost");

db = connection.school
scores = db.scores

def find():
    print "find , reporting for duty"
    query = {'type': 'exam'}
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



def find_one():
    print "find one,"
    query = {'student_id':10}
    try:
       print scores.find_one({})
    except Exception as e:
        print "Unexpected error:",type(e),e


find_one()