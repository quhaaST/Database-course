from pymongo import MongoClient
import datetime

def first_query(query_db):
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
        else:
            with_c = query_db.restaurants['grades'].insert_one(
                {'date': datetime.datetime(2014, 12, 30, 0, 0), 'grade': 'C', 'score': 0})


client = MongoClient("mongodb://localhost:5050")
db = client['test']

first_query(db)
