import socket
from _thread import *
# https://webnautes.tistory.com/1381 참고 사이트


def functhread(client_socket, addr) :
    print('client connected by :', addr[0],':',addr[1]) # 클라이언트의 접속정보출력
    
    # 클라이언트가 접속을 끊을 때 까지 반복
    while True :
        # 예외가 발생할 가능성이 있는 코드
        try: 
            # 클라이언트가 1024이하로 보낸다는 확신이 있을때 넣음
            # 스트림 수신 대기, 수신되지 않을 경우 아래로 내려가지 않음
            data = client_socket.recv(1024) 
            
            if not data :
                break
            print(addr[0], addr[1], data.decode()) # 수신데이터 출력
            client_socket.send(data) # 수신된 데이터 echo
        
        except ConnectionResetError as e:
            break
    
    client_socket.close() # 소킷 종료 : 메모리에 남아있을수 있기때문에 (서버에 부담)
    


HOST = '192.168.0.12'  #local loopback address, localhost와 동일 (내부통신연결)
PORT = 9999 # 0~65535 범위에서 사용가능 ( 0~1024는 사용하지 않도록함 : 일정데이터 지정되어 있음)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소킷 객체 생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 소킷 옵션 설정


server_socket.bind((HOST, PORT)) # 문자열과 정수
server_socket.listen() # 클라이어트로부터 수신준비, 서버시작

print('server start')

while True :
    print('wait')
    client_socket, addr = server_socket.accept()  
    # 대기상태, 아래 라인으로 내려가지 않음
    # 접속할 경우 클라이언트소킷과 IP주소를 반환
    start_new_thread(functhread, (client_socket, addr)) # 스레드함수 호출
    
server_socket.close()
    