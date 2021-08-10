# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:15:01 2021

@author: user12
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget) : # QWidget 클래스를 상속
    def __init__(self) : # 생성자
        super().__init__() # 부모클래스 생성자 호출(최초라인에 작성)
        self.initUI()
    
    
        # java의 this 와 비슷
        # self 원래 존재하는 단어 : 나를 지칭 : 매개변수처럼 사용가능(클래스쓸때)
    def initUI(self) :
        btn1 = QPushButton('button1', self) # 버튼생성
        btn2 = QPushButton('button2', self) 
        btn3 = QPushButton('button3', self) 
        
        vbox = QVBoxLayout() #박스 레이아웃 객체생성
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        
        self.setLayout(vbox) #레이아웃 관리자 선언
        
        self.setWindowTitle('So window')
        self.setGeometry(150, 150, 400, 300)
        self.show()
        
if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())