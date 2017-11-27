#!/usr/bin/env python
"""
Imports a given user's LastFM library data into MongoDB.
"""
import json
import urllib.request
import pymongo

username = input("Enter Username: ")

# Establishes connection to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

# Establishes connection to MongoDB collection
database = connection.lastfm
artists = database.artists
# Clears it of precious data
artists.drop()

# Opens LastFM API to access user's library data
userLibrary = urllib.request.urlopen("http://ws.audioscrobbler.com"
    "/2.0/?method=library.getartists"
    "&api_key=66f0acb6a00de7fd814cd490db7e86cf&user={:s}&format=json"
    .format(username))

libraryDictionary = json.loads(userLibrary.read())

# Iterates though dictionary addidng each artist as a document
for item in libraryDictionary['artists']['artist']:
    artists.insert_one(item)