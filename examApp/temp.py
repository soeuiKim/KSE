# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt  #날짜생성



class MyApp(QMainWindow) : # QMainWindow 클래스를 상속받아 MyApp 클래스 정의
    def __init__(self) : # 생성자
        super().__init__() # 부모클래스의 생성자 호출(윈도우에 띄우기위해)
        self.date = QDate.currentDate() # 현재 시스템 날짜시간 가져오기
        self.initUI() # 메서드 호출


    def initUI(self) : # 일반적인 메서드 정의
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
                                            # 날짜 출력
        self.setWindowTitle('My App') # 타이틀 바
        self.resize(800, 600) # 윈도우크기
        self.show() #화면에 보이기

if __name__ == '__main__' : 
    app = QApplication(sys.argv) #프로그램 실행
    ex = MyApp() # 객체생성
    sys.exit(app.exec_())
    





