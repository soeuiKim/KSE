import socket
import datetime
import pymysql

conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql' , charset = 'utf8')
cursor = conn.cursor()



HOST = '192.168.0.12'
PORT = 9999


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체생성
client_socket.connect((HOST, PORT)) # 서버에 접속


while True :
    
    data = client_socket.recv(1024)
    
    now = datetime.datetime.today() # 현재 시스템 날짜 및 시간
    nowstr = now.strftime('%Y-%m-%d  %H:%M:%S') # 형식을 만들어서 문자열로 저장
    print(nowstr)
    
    rs = data.decode().split(':') # 콜론을 구분자로 모든 데이터를 분리(리스트생성)
    print(rs)
    
    sql = "insert into tblsensor values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (nowstr, int(rs[0]),int(rs[1]),int(rs[2]),int(rs[3]),int(rs[4]),int(rs[5]),int(rs[6]),int(rs[7]),int(rs[8]),int(rs[9])))
    conn.commit()

client_socket.close()
cursor.close()
conn.close()