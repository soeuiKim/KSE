# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:45:53 2021

@author: user12
"""

'''  콤보박스 텍스트박스(라인) 프로그래스바(로딩창ㅎ) '''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QLineEdit, 
                             QProgressBar, QPushButton)

class SoApp(QWidget) :
    
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initSo()
    
    def initSo(self) :
        cb = QComboBox(self) # 콤보박스 생성
        cb.addItem('Seoul')
        cb.addItem('Busan')
        cb.addItem('CheongJu')
        cb.move(20, 0)
        
        q1 = QLineEdit(self)  # text박스
        q1.move(20, 30)
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 60, 450, 30)
        
        self.step = 0
        
        self.bu1 = QPushButton('up', self)
        self.bu1.setGeometry(40, 100, 100, 30)
        
        self.bu1.clicked.connect(self.bu1ev)
        
        
        self.bu2 = QPushButton('down', self)
        self.bu2.setGeometry(200, 100, 100, 30)
        
        self.bu2.clicked.connect(self.bu2ev)
        
        
        self.setWindowTitle('combobox and textbox exam')
        self.setGeometry(800, 250, 500, 300)  # 위치와 가로,세로 크기
        self.show()  # 윈도우 보이기
        
    def bu1ev(self) :
        if self.step >= 100 :
            self.bu1.setValue(100)
            return
        
        self.step = self.step + 10
        self.pbar.setValue(self.step)
       
        
    def bu2ev(self) :
        if self.step >= 100 :
            self.bu1.setValue(0)
            return
        
        self.step = self.step - 10
        self.pbar.setValue(self.step)
        

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = SoApp()
    sys.exit(app.exec_())
