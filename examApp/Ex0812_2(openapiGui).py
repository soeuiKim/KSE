import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse


class App (QWidget) :
    
    def __init__(self) :
        super().__init__()
        
        self.initui()
        
    def initui(self):
        
        
        
        self.leAre = QLineEdit(self)
        self.leAre.setGeometry(30, 30, 150, 30)
        
        self.btnFind = QPushButton('Find', self)
        self.btnFind.setGeometry(200, 30, 100, 30)
        self.btnFind.clicked.connect(self.btnFindEv)
        
        self.tbl = QTableWidget(self)
        self.tbl.setColumnCount(4)
        self.tbl.setGeometry(10, 100, 450, 250)
        self.col_head = ['date','pm10','pm25','o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        self.setWindowTitle('Graphic Exam')
        self.setGeometry(550, 350, 600, 400)
        self.show()
        
    def btnFindEv(self) :
        
        strArea = self.leAre.text() # 한글일경우 인코딩 필요
        encoderArea = parse.quote_plus(strArea)
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=5&pageNo=1&stationName="+ encoderArea +"&dataTerm=DAILY&ver=1.0"
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.tbl.setRowCount(5)
        
        row = 0 
        for item in self.air.findAll('item') :
            for time in item.findAll('datatime'):
                self.tbl.setItem(row, 0, QTableWidgetItem(time.string))
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(row,1,QTableWidgetItem(pm10.string))
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(row,2,QTableWidgetItem(pm25.string))
            for o3 in item.findAll('o3value'):
                self.tbl.setItem(row,3,QTableWidgetItem(o3.string))
            row += 1

        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    