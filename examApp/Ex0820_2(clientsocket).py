import socket

HOST = '192.168.0.12'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체생성
client_socket.connect((HOST, PORT)) # 서버에 접속

while True :
    msg = input('Enter message : ')
    if msg == 'quit' :
        break
    
    client_socket.send(msg.encode()) # 다국어 시스템에서 필요
    data = client_socket.recv(1024) # 버퍼 크기는 서버와 동일하게
    
    print('received from the server :', data.decode())

client_socket.close()