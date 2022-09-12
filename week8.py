from typing import Collection
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://gilang:cQxUZhoHw7SmyBfa@cluster0.lco38k5.mongodb.net/?retryWrites=true&w=majority")
db = client.database
collection = db.Cluster0

def locationn(kecepatan,latitude,longitude,timestamp):
    data = {
        "ID transaksi": str(uuid.uuid4()),
        "kecepatan": 90,
        "latitude": 6.2088,
        "longitude": 106.8456
        "timestamp": timestamp
    }
    records = collection.insert_one(data)
    print("data tersimpan",records)
