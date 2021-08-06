# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:47:07 2021

@author: user12
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        
        self.tbl = QTableWidget(10, 5, self)
        self.tbl.setGeometry(30, 30, 600, 400)
  
        # self.tbl.setItem(0, 0, QTableWidgetItem('data1'))
        # self.tbl.setItem(9, 4, QTableWidgetItem('data last'))
        #  1~50을 순서대로 테이블에 출력_ 반복구문이용
        
        cnt = 1
        for i in range(10) : # 0 ~ 9 까지 반복
            for j in range(5) : # 0 ~ 4 까지 반복
                fcnt =  '%02d - %d' %  (i+1, j+1) # %d에 i,j 대응 _ 두개이상이면 () 사용 : 포맷팅
                self.tbl.setItem(i, j, QTableWidgetItem(str(fcnt)))
                cnt += 1
        
        
        self.setWindowTitle('table exam')
        self.setGeometry(100, 100, 800, 500)
        self.show()
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())