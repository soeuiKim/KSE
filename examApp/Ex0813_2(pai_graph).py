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
        self.lne.setText('전국')
        self.cob = QComboBox(self)
        self.cob.activated.connect(self.cobeve)
        self.but = QPushButton('조회',self)
        self.but.clicked.connect(self.buteve)
        
        self.strArea = ['전국', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
        self.cob.addItems(self.strArea)
        
        layout1 = QHBoxLayout()
        layout1.addStretch(1)
        layout1.addWidget(self.lne)
        layout1.addWidget(self.cob)
        layout1.addWidget(self.but)
        layout1.addStretch(1)
        
        self.tbl = QTableWidget(self)
        self.tbl.setRowCount(2)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.tbl)
        
        self.rbu1 = QRadioButton('type1')
        self.rbu2 = QRadioButton('type2')
        self.rbu3 = QRadioButton('type3')
        self.rbu1.setChecked(True)
        self.rbu1.clicked.connect(self.rbueve)
        self.rbu2.clicked.connect(self.rbueve)
        self.rbu3.clicked.connect(self.rbueve)
        
        layout3 = QHBoxLayout()
        layout3.addWidget(self.rbu1)
        layout3.addWidget(self.rbu2)
        layout3.addWidget(self.rbu3)
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.show()
        
        layout4 = QHBoxLayout()
        layout4.addWidget(self.canvas)
        
        layoutAll = QVBoxLayout()
        layoutAll.addLayout(layout1)
        layoutAll.addLayout(layout2)
        layoutAll.addLayout(layout3)
        layoutAll.addLayout(layout4)
        self.setLayout(layoutAll)
        
        
        self.setWindowTitle('API Graphic')
        self.setGeometry(400, 200, 1100, 700)
        self.show()
        
    def rbueve(self) :
        if self.rbu1.isChecked() :
            self.bar1()
        elif self.rbu2.isChecked() :
            self.bar1()
        else : 
            self.bar1()
    def bar1(self) :
        self.bar_ = self.fig.add_subplot(111)
        self.bar_.bar(self.stn, self.xpm10)
        
        
        self.canvas.draw()
        
    def buteve(self) :
        
        strArea = self.lne.text() 
        encoderArea = parse.quote_plus(strArea)  
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=" + encoderArea + "&ver=1.0"
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.stn = []
        self.xpm10 = []
        self.xpm25 = []
        
        col = 0
        for item in self.air.findAll('item') :
            for stname in item.findAll('stationname'):
                self.stn.append(stname.string)
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(0,col,QTableWidgetItem(pm10.string))
                
                # if pm10 == '-' :
                    # pm10.delete('-')
                    # pm10.append(0)
                self.xpm10.append(pm10.string)
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(1,col,QTableWidgetItem(pm25.string))
                
                # if pm10 == '-' :
                    # pm10.delete('-')
                    # pm10.append(0)
                self.xpm25.append(pm25.string)
            col += 1
        
        
        cnt = len(self.air.findAll('item'))
        self.tbl.setColumnCount(cnt)
        self.tbl.setHorizontalHeaderLabels(self.stn)
        
    def cobeve(self) :
        self.lne.setText(self.cob.currentText())
        
        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 