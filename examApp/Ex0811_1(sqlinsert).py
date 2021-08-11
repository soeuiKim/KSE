import pymysql

conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql' , charset = 'utf8')
cursor = conn.cursor()

sql = "insert into 제품 values (%s,%s,%s,%s,%s)"
cursor.execute(sql,('p08','컴퓨터',500,5000,'아이비엠'))



cursor.close()
conn.commit() # insert, update 에 필요함
conn.close()
# ↑필수 구문


