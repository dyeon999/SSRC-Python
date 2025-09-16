from pymongo import MongoClient


# mongodb(no sql) - DB > Collection > Data(Object)
# Elasticsearch(no sql) - 문서(document) > data ...

client = MongoClient('mongodb://localhost:27017')
db = client['school_db']
collection = db['students']

student = {
    "name": "Soyeon Kim",
    "age" : 20,
    "grade" : "B",
    "subjects" : ["수학", "영어"]
}
#result = 
collection.insert_one(student) # insert는 추가 / update는 수정 / delete는 삭제
print("Success!!")

#print(f"New Document : {result.inserted_id}")

#print("MongoDB Success!!")
