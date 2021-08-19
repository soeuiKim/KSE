from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/')  # mongodb 접속

# https://velopert.com/category/dev-log/tech-log/mongodb 참고사이트
# $eq	==  (equals) 주어진 값과 일치하는 값
# $gt	>  (greater than) 주어진 값보다 큰 값
# $gte	>=  (greather than or equals) 주어진 값보다 크거나 같은 값
# $lt	<  (less than) 주어진 값보다 작은 값
# $lte	<=  (less than or equals) 주어진 값보다 작거나 같은 값
# $ne	!=  (not equal) 주어진 값과 일치하지 않는 값
# $in	주어진 배열 안에 속하는 값
# $nin	주어빈 배열 안에 속하지 않는 값

# print(conn.list_database_names())  # 설치된 db명칭 출력(show dbs와 동일한 처리)

db = conn['test'] # db반환

collection = db['product'] # collection반환

x = collection.find_one()
# print(x)

# query = {'name' : '냉장고'}
# query = {'price' : {$gte : 100000}}

# sort 정렬 : 기본 오름차순, -1 내림차순 : 원본데이터는 변화없이 정렬만 함
# result = collection.find().sort('name', -1)

result = collection.find({'price' : {'$gte' : 100000, '$lte' : 300000}})


for item in result : 
    print(item)
    # print(item['name'], item['price'])

# print(x['name'],x['price'])

