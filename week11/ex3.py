from pymongo import MongoClient


def query1(query_db):
    res = query_db.restaurants.delete_one({'borough': 'Manhattan'})
    print(res.deleted_count)


def query2(query_db):
    res = query_db.restaurants.delete_many({'cuisine': 'Thai'})
    print(res.deleted_count)


client = MongoClient("mongodb://localhost:27017")
db = client['test']
query1(db)
query2(db)
