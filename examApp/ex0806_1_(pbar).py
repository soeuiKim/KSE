# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:45:22 2021

@author: user12
"""

''' pbar 교수님 답_ 
    키보드 이벤트 핸들러'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QLineEdit, 
                             QProgressBar, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

class SoApp(QWidget) :
    
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.pbarvalue = 50
        self.initSo()
    
    def initSo(self) :
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 60, 450, 30)
        self.pbar.setValue(self.pbarvalue)

        self.bu1 = QPushButton('up', self)
        self.bu1.setGeometry(40, 100, 100, 30)
        
        self.bu1.clicked.connect(self.btn1Handler)
        
        
        self.bu2 = QPushButton('down', self)
        self.bu2.setGeometry(200, 100, 100, 30)
        
        self.bu2.clicked.connect(self.btn2Handler)
        
        
        self.setWindowTitle('pbar button')
        self.setGeometry(800, 250, 500, 300) 
        self.show()  
        
    def btn1Handler(self) :
        if self.pbarvalue >= 10 :
            self.pbarvalue += 10
        self.pbar.setValue(self.pbarvalue)

    # 다른방법    
    # def btn1Handler(self) :
    #         self.pbarvalue -= 10
    #     if self.pbarvalue < 0 :
    #         self.pbarvalue = 0
    #     self.pbar.setValue(self.pbarvalue)
    #
    # def btn2Handler(self) :
    #         self.pbarvalue += 10
    #     if self.pbarvalue > 100 :
    #         self.pbarvalue = 100
    #     self.pbar.setValue(self.pbarvalue)

    def btn2Handler(self) :
        if self.pbarvalue >= 10 :
            self.pbarvalue -= 10
        self.pbar.setValue(self.pbarvalue)

    def keyPressEvent(self, e) : # 키보드 이벤트 핸들러, 반드시 지정된 이름을 써야함
        if e.key() == Qt.Key_1 : # 왼쪽방향키 눌렀을때
            self.pbarvalue -= 10
            if self.pbarvalue < 0 :
                self.pbarvalue = 0
            self.pbar.setValue(self.pbarvalue)
        
        elif e.key() == Qt.Key_3 :
            self.pbarvalue += 10
            if self.pbarvalue > 100 :
                self.pbarvalue = 100
            self.pbar.setValue(self.pbarvalue)
        
        # esc키가 눌렸을때 창닫기
        elif e.key() == Qt.Key_Escape :
            self.close() # 창종료
            
        elif e.key() == Qt.Key_0 :
            QMessageBox.about(self, 'caption', 'message')





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = SoApp()
    sys.exit(app.exec_())
