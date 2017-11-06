import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Joshua', 'lastname':'Rodriguez'}
print(doc)
print("about to insert the document")

try:
	users.insert_one(doc)
except Exception as e:
	print("insert failed", e)

print(doc)
print("inserting again")
doc = {'firstname':'Joshua', 'lastname':'Rodriguez'}

try:
	users.insert_one(doc)
except Exception as e:
	print("second insert failed", e)
