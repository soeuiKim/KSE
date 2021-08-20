# 스레드 개념 이해

import threading

def functhread(number) :
    print(threading.currentThread().getName(), number)

if __name__ == '__main__' :
    for i in range(10) :
        mythread = threading.Thread(target=functhread, args=(i,))
        # 스레드 객체 생성
        
        mythread.start()

