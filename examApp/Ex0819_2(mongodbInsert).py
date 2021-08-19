from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/')  # mongodb 접속


db = conn['test'] # db반환

collection = db['product'] # collection반환

# x = collection.insert_one({'name' : '콘','price' : '2000'})
# # 1개 입력 __ id부여받음

# print(x.inserted_id)

# insert , insert_one 둘다 입력가능 , id부여 여부를 확인하기 위해 one 사용

dicts = [{'name' : '배추','price' : 3000},
         {'name' : '감자','price' : 2000}]
x = collection.insert_many(dicts) # one,many는 _id 반환가능
print(x.inserted_ids)