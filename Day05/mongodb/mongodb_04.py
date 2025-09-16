from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['school_db']
collection = db['students']

# 단일 문서 삭제
result = collection.delete_one(
    {"name": "Soyeon Kim"})
print(f"수정된 문서 수: {result.deleted_count}")