from pymongo import MongoClient
from faker import Faker

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb_faker']
collection = db['people']

fake = Faker('ko_KR')

for _ in range(20):
    person = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
    collection.insert_one(person)

print("Data Inserted Successfully!!!")