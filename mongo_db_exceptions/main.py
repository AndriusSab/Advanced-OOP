from pymongo import MongoClient
from pymongo.errors import PyMongoError

def conection_to_db():
    try:
        client = MongoClient('mongodb://localhost:27017')
        db = client['FishingEquipment']
        collection = db['Rods']

        
        client = collection.find_one({'name': 'John'})
        
        if client:
            print('Found document:', client)
        else:
            print('Document not found.')
        
        client.close()
        
    except PyMongoError as e:
        print('An error occurred:', str(e))
        
        
    except ConnectionError as e:
        print('ConnectionError:', str(e))
        
conection_to_db()





