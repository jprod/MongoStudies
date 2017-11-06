import bottle
import pymongo

#this is the header to a default path to a webserver

@bottle.route('/')
def index():

	# connect to mongDB
	connection = pymongo.MongoClient('localhost', 27017)

	# attach to test database
	db = connection.test

	# get the name for the names collection
	name = db.names

	# find a single document
	item = name.find_one()

	return '<b> Hello {:s}!</b>'.format(item['name'])

bottle.run(host='localhost', port=8082)