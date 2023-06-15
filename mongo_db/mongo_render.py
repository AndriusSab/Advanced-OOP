import random
import string
from pymongo import MongoClient

# Function to generate a random string
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Get user input
database_name = input('Enter the database name: ')
collection_name = input('Enter the collection name: ')
num_documents = int(input('Enter the number of documents to populate: '))

# Connect to MongoDB
client = MongoClient()
db = client[database_name]
collection = db[collection_name]

# Generate and insert random documents
for _ in range(num_documents):
    document = {
        'name': generate_random_string(10),
        'age': random.randint(18, 60),
        'email': generate_random_string(8) + '@example.com'
    }
    collection.insert_one(document)