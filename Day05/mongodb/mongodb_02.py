from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['school_db']
collection = db['students']

for student in collection.find(): # find: 그 안에서 찾는것
    print(student)

print("========================================")
result = collection.find_one({"name":"Doyeon Kim"})
print(result)

print("========================================")
# 조건에 맞는 문서 조회 (나이가 20 이상인 학생)
print("\n나이가 20 이상인 학생:")
for student in collection.find({"age": {"$gte": 20}}):
    print(student)
