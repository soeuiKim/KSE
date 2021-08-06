# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:46:44 2021

@author: user12
"""

''' 레이아웃, 체크박스, 라디오버튼'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QRadioButton, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget) : 
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        label1 = QLabel('so Label YaSs',self) # 레이블 객체 생성
        label1.setAlignment(Qt.AlignCenter) # 가운데 정렬
        font1 = label1.font() # 해당 위젯의 폰트 변수 설정
        font1.setPointSize(20) # 폰트 크기
        font1.setBold(True)
        
        label2 = QLabel('SsoYaass',self)
        label2.setAlignment(Qt.AlignCenter)
        font2 = label2.font()
        font2.setPointSize(30)
        font2.setItalic(True)
        
        cb = QCheckBox('So CheckBox',self) # 체크박스생성
        
        rbtn1 = QRadioButton('So Radiobutton 1')
        rbtn2 = QRadioButton('So Radiobutton 2')
        rbtn3 = QRadioButton('So Radiobutton 3')
        
        rbtn1.setChecked(True)
        
        label1.setFont(font1) # 폰트 적용
        label2.setFont(font2)
                
        layout = QVBoxLayout() # 레이아웃 객체 생성
        
        layout.addWidget(label1) # 레이아웃에 추가
        layout.addWidget(label2)
        
        layout.addWidget(cb) # 체크박스 추가
        
        layout.addWidget(rbtn1)
        layout.addWidget(rbtn2)
        layout.addWidget(rbtn3)
        
        self.setLayout(layout) # 박스 레이아웃 설정
        self.setWindowTitle('So window')
        self.setGeometry(150, 150, 400, 300)
        self.show()
    
if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())