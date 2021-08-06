# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:07:49 2021

@author: user12
"""

''' 날짜 시간 텍스트박스 '''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDateEdit, QTimeEdit, QDateTimeEdit, QTextEdit
from PyQt5.QtCore import QDate, QTime, QDateTime

class App(QWidget) :
    
    def __init__(self) : 
        super().__init__()
        self.initA()
        
    def initA(self) :
        
        da = QDateEdit(self)
        da.move(30, 30)                 # PyQt5.QtCore 에서 QDate 임포트
        da.setDate(QDate.currentDate()) # 현재시스템 날짜를 컨트롤에 설정
        
        ti = QTimeEdit(self)
        ti.move(30,70)
        ti.setTime(QTime.currentTime())
        
        dati = QDateTimeEdit(self)
        dati.move(30,100)
        dati.setDateTime(QDateTime.currentDateTime())
        
        te = QTextEdit(self)
        te.setGeometry(30, 140, 300, 200)
        te.setText('soeui text!!!')
        
        self.setWindowTitle('A_')
        self.setGeometry(100, 100, 500, 500)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())