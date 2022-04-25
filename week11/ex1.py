from pymongo import MongoClient


def query_first(db):
	cursor = db.restaurants.find({'cuisine': 'Thai'})
	print(len(list(cursor)))

def query_second(db):
	cursor = db.restaurants.find({ '$or': [ { 'cuisine': "Thai" }, { 'cuisine': 'Indian' } ] })
	print(len(list(cursor)))


def query_third(db):
	cursor = db.restaurants.find({'address': {'street': 'Rogers Avenue', 'zipcode': '11226', 'building': '1115'}})
	print(list(cursor))

# initialize the database connection
client = MongoClient("mongodb://localhost:5050")
db = client['test']

# execute all queries
query_first(db)
query_second(db)
query_third(db)
