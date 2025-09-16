from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['school_db']
collection = db['students']

# 단일 문서 업데이트 (소연의 학점을 B로 변경)
result = collection.update_one(
    {"name": "Soyeon Kim"},
    {"$set": {"grade": "B+"}}
)
print(f"수정된 문서 수: {result.modified_count}")