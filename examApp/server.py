import socket
from _thread import *
import time
import numpy as np




def functhread(client_socket, addr) :
    print('client connected by :', addr[0],':',addr[1]) # 클라이언트의 접속정보출력
    
    # 클라이언트가 접속을 끊을 때 까지 반복
    while True :
        try: 
            data = ''
            for item in range(9):
                data = data + str(np.random.randint(20, 30)) + ':'
                                    # 20~29까지 랜덤생성 : 
            data = data + str(np.random.randint(20, 30)) # 끝에 : 삭제를 위해 for구문빠져나옴
            
            client_socket.send(data.encode()) # 온도(예제)데이터 10개 전송
            
            time.sleep(60) # 60초(1분) 지연
        
        except ConnectionResetError as e:
            break
    
    client_socket.close() 
    


HOST = '192.168.0.12' 
PORT = 9999 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_socket.bind((HOST, PORT)) 
server_socket.listen()


print('server start')

while True :
    print('wait')
    
    client_socket, addr = server_socket.accept()  
    start_new_thread(functhread, (client_socket, addr))
    
server_socket.close()
    