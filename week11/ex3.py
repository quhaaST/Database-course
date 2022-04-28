from pymongo import MongoClient


def first_query(query_db):
    res = query_db.restaurants.delete_one({'borough': 'Manhattan'})
    print(res.deleted_count)


def second_query(query_db):
    res = query_db.restaurants.delete_many({'cuisine': 'Thai'})
    print(res.deleted_count)


client = MongoClient("mongodb://localhost:5050")
db = client['test']
first_query(db)
second_query(db)
