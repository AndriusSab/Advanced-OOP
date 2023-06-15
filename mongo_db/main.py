# Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data.
# The input should ask for :

# database name
# collection name
# field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
# number o documents to create.
from pymongo import MongoClient
from typing import List, Dict, Any, Optional
from random_word import RandomWords
import random

class MongoDbRandomGenerator:
    def create_random_db(self) -> None:
        host = input("Enter MongoDB host: ")
        port = int(input("Enter MongoDB port: "))
        db_name = input("Enter database name: ")
        collection_name = input("Enter collection name: ")
        num_documents = int(input("Enter number of documents to create: "))

        fields = []
        while True:
            field_name = input("Enter field name (or 'done' to finish): ")
            if field_name == 'done':
                break
            
            field_type = input("Enter field type ('string', 'number', 'date'): ")
            field_range = {}
            if field_type in ('number', 'date'):
                field_range['min'] = float(input("Enter minimum value: "))
                field_range['max'] = float(input("Enter maximum value: "))
            
            field = {'name': field_name, 'type': field_type, 'range': field_range}
            fields.append(field)
        
        self.populate_database(host, port, db_name, collection_name, fields, num_documents)
    
    def populate_database(self, host: str, port: int, db_name: str, collection_name: str, fields: List[Dict[str, Any]], num_documents: int) -> None:
        client = MongoClient(host, port)
        db = client[db_name]
        collection = db[collection_name]
        
        for _ in range(num_documents):
            document = {}
            for field in fields:
                field_name = field['name']
                field_type = field['type']
                field_range = field['range']
                
                if field_type == 'string':
                    document[field_name] = self.generate_random_string()
                elif field_type == 'number':
                    document[field_name] = self.generate_random_number(field_range['min'], field_range['max'])
                elif field_type == 'date':
                    document[field_name] = self.generate_random_date(field_range['min'], field_range['max'])
                # Add more field types as needed
                
            collection.insert_one(document)
            
        print(f"{num_documents} documents created in '{db_name}.{collection_name}'")
    
    def generate_random_string(self) -> str:
        r = RandomWords()
        return r.get_random_word()
    
    def generate_random_number(self, min_val: float, max_val: float) -> float:
        return random.uniform(min_val, max_val)
    
    def generate_random_date(self, start_date: str, end_date: str) -> str:
        start_timestamp = pd.to_datetime(start_date).timestamp()
        end_timestamp = pd.to_datetime(end_date).timestamp()
        random_timestamp = random.uniform(start_timestamp, end_timestamp)
        return pd.to_datetime(random_timestamp, unit='s').strftime('%Y-%m-%d')

# Example usage
generator = MongoDbRandomGenerator()
generator.create_random_db()