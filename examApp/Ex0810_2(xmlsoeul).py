import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
        
        res = ulib.urlopen(url) 
        
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.initUI()
        
    def initUI(self) :
        
        cnt = len(self.air.findAll('item')) # 행의 갯수
        
        self.tbl = QTableWidget(cnt, 4, self) # 공백형태의 테이블 표시
        self.tbl.setGeometry(50, 30, 500, 750)
        self.col_head = ['station','pm10','pm25','o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)

        row = 0 # 행번호
        for item in self.air.findAll('item') :
            for sname in item.findAll('stationname'):
                self.tbl.setItem(row,0,QTableWidgetItem(sname.string))
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(row,1,QTableWidgetItem(pm10.string))
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(row,2,QTableWidgetItem(pm25.string))
            for o3 in item.findAll('o3value'):
                self.tbl.setItem(row,3,QTableWidgetItem(o3.string))
            row += 1
            
        
        
        self.setWindowTitle('DB exam')
        self.setGeometry(200, 200, 600, 800)
        self.show()
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())