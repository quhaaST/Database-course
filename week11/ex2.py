from pymongo import MongoClient


def first_query(query_db):
    res = query_db.restaurants.insert_one(
        {"address": {"building": "1480", "coord": [-73.9557413, 40.7720266], 
                     "street": "2 Avenue", "zipcode": "10075"},
         "borough": "Manhattan", "cuisine": "Italian",
         "grades": [{"date": {"$date": {"$numberLong": "1412121600000"}}, 
                     "grade": "A", "score": 11}], 
         "name": "Vella",
         "restaurant_id": "41704620"})
    print(res.inserted_id)


client = MongoClient("mongodb://localhost:5050")
db = client['test']

first_query(db)
