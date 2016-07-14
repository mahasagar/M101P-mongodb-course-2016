#first sort - skip - limit
import sys
import pymongo

db = connection.school
scores = db.scores

def find():
    print "find , reporting for duty"
    query = {}
    try:
       cursor = scores.find(query).sort('student_id',pymongo.ASCENDING).skip(4)
