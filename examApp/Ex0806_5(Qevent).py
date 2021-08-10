
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QDial, QLCDNumber)

# 이벤트 객체생성, 함수생성, 연결

class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        
        self.lcd = QLCDNumber(self)
        self.lcd.setAutoFillBackground(True)
        self.lcd.move(50, 30)
        
        
        self.dial = QDial(self)
        self.dial.move(30, 80)   
        
        self.dial.valueChanged.connect(self.lcd.display) # 이벤트 연결
        
        self.btn1 = QPushButton('button1', self) #버튼생성
        self.btn1.setGeometry(30, 250, 150, 50) 
        
        self.btn1.clicked.connect(self.btn1Event) # 이벤트 연결
        
        self.btn2 = QPushButton('button2', self)
        self.btn2.setGeometry(200, 250, 150, 50)
        
        self.btn2.clicked.connect(self.btn2Event)
        
        
        self.setWindowTitle('event exam')
        self.setGeometry(800, 250, 500, 500)
        self.show()
        
    def btn1Event(self) : # 이벤트 핸들러 함수
        self.resize(700, 700)
        
    def btn2Event(self) :
        self.resize(500, 500)
        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())