from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("localhost")
MongoClient(host='127.0.0.1', port=27017)
# conn = MongoClient("mongodb://username:password@ip:port/database_name")
db = conn.database_name

def export():
    print(db.collection_names())

def insert():
    result = db.user.insert_one({"name": "夏利刚", "age": 18, "hobby": "学习"})
    print(result.inserted_id)
    result = db.user.find_one({"_id": result.inserted_id})
    print(result)

def find():
    result = db.user.find()
    for item in result:
        print(item)

def findById():
    result = db.user.find()
    print(result)
    result = db.user.find_one({"_id": ObjectId("5d2d6b376870b2db3622313e")})
    print(result)

def count():
    count = db.user.count_documents({})
    print(count)


if __name__ == '__main__':
    # export()
    # insert()
    find()
    count()