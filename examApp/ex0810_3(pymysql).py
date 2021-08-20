
import pymysql 

# db접속
conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql' , charset = 'utf8')

cursor = conn.cursor() # 커서 설정

sql = 'select * from 제품'

cursor.execute(sql) # sql실행

result = cursor.fetchall() # 모든 레코드를 반환해서 result 변수에 저장

# print(result)

for item in result:
    print(item[0], item[1],item[2],item[3],item[4])
    
# print ('---------------------------')
    
# # 고객정보 출력

# sql2 = 'select * from 고객'
# cursor.execute(sql2)
# res = cursor.fetchall()

# for cus in res:
#     print(cus[0],cus[1],cus[2],cus[3],cus[4],cus[5])




# conn.close() # 접속 종료