
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores

"""
def find():
    
    print("find, reporting for duty")
    
    query = {'type':'exam'}
    
    try:
"""

def find_one():
    
    print("find one, reporting for duty")
    
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
    
    except Exception as e:
        print("Unexpected error:", type(e), e)
    
    print(doc)

find_one()