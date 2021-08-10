# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:40:12 2021

@author: user12
"""

''' 슬라이더 다이얼 캘린더'''

# 윈도우 500 400 크기로 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QCalendarWidget
from PyQt5.QtCore import Qt

class S (QWidget) :
    
    def __init__(self) : 
        super().__init__()
        self.initS()
        
    def initS(self) :
        
        self.slider = QSlider(Qt.Horizontal,self) # 슬라이더설정
        self.slider.move(30, 30) # 슬라이더 위치
        self.slider.setRange(0, 50) # 슬라이더 영역설정
        self.slider.setSingleStep(2) # 슬라이더 눈금설정
        
        self.dial = QDial(self)
        self.dial.move(30,70)
        self.dial.setRange(0, 50)
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(30, 200)
        
        
        self.setWindowTitle('S_initS')
        self.setGeometry(100, 100, 500, 500)
        self.show()
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = S()
    sys.exit(app.exec_())