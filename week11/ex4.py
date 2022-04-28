from pymongo import MongoClient
import datetime


def query1(query_db):
    res = query_db.restaurants.find()
    arr = list(res)
    n = len(arr)
    grades = []
    for i in range(n):
        temp = []
        i_grades = arr[i]['grades']
        for elem in i_grades:
            temp.append(elem['grade'])
            print(elem['grade'])
        if 'C' in temp:
            deleted = query_db.restaurants.delete_one({'_id': arr[i]['_id']})
            print(1123)
        else:
            with_c = query_db.restaurants['grades'].insert_one(
                {'date': datetime.datetime(2014, 12, 30, 0, 0), 'grade': 'C', 'score': 0})


client = MongoClient("mongodb://localhost:27017")
db = client['test']

query1(db)
