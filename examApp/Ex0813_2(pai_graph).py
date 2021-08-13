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
from matplotlib import font_manager, rc



class App (QWidget) :
    
    def __init__(self) :
        super().__init__()
        
        self.initui()
        
    def initui(self):
        font_name = font_manager.FontProperties(fname='c:/windows/Fonts/batang.ttc').get_name()
        rc('font', family=font_name)   
        
        self.lne = QLineEdit(self)
        self.cob = QComboBox(self)
        self.but = QPushButton('조회',self)
        self.but.clicked.connect(self.buteve)
        
        layout1 = QHBoxLayout()
        layout1.addStretch(1)
        layout1.addWidget(self.lne)
        layout1.addWidget(self.cob)
        layout1.addWidget(self.but)
        layout1.addStretch(1)
        
        self.tbl = QTableWidget(self)
        self.tbl.setRowCount(5)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.tbl)
        
        layout3 = QVBoxLayout()
        
        layoutAll = QVBoxLayout()
        layoutAll.addLayout(layout1)
        layoutAll.addLayout(layout2)
        layoutAll.addLayout(layout3)
        self.setLayout(layoutAll)
        
        
        
        
        
        
        
        
        
        
        
        
        self.setWindowTitle('API Graphic')
        self.setGeometry(400, 200, 1100, 700)
        self.show()
        
    def buteve(self) :
        
        # strArea = self.le1.text() 
        # encoderArea = parse.quote_plus(strArea)  
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.stn = []
        self.xpm10 = []
        self.xpm25 = []
        
        self.tbl.setHorizontalHeaderLabels(self.stn)
        
        cnt = len(self.air.findAll('item'))
        self.tbl.setColumnCount(cnt)
        
        # col = 0 
        # for item in self.air.findAll('item') :
        #     for stname in item.findAll('stationname'):
        #         self.tbl.setItem(0, col, QTableWidgetItem(stname.string))
        #         self.stn.append(stname.string)
        #     for pm10 in item.findAll('pm10value'):
        #         self.tbl.setItem(1, col, QTableWidgetItem(pm10.string))
        #         self.xpm10.append(int(pm10.string))
        #     for pm25 in item.findAll('pm25value'):
        #         self.tbl.setItem(2, col, QTableWidgetItem(pm25.string))
        #         self.xpm25.append(int(pm25.string))
        #     col += 1
        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 