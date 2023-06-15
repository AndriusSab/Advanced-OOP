from pymongo import MongoClient

def create_fishing_store_database():
    client = MongoClient('mongodb://localhost:27017')
    db = client['fishing_store']
    return db