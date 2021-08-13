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
        
        self.le1 = QLineEdit(self)
        
        self.bu1 = QPushButton('조회',self)
        self.bu1.clicked.connect(self.bu1ev)
        
        self.strArea = ['전국', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
        self.cbA = QComboBox()
        self.cbA.addItems(self.strArea)
        # self.cbA.addItem('종로구')
        # self.cbA.addItem('용암동')
        # self.cbA.addItem('용담동')
        # self.cbA.addItem('사천동')
        # self.cbA.addItem('오창읍') 
        # self.cbA.addItem('복대동') 
        self.cbA.activated.connect(self.cbAev)
        # 콤보박스에 항목을 변경해서 선택했을 경우
        
        
        layout1 = QHBoxLayout()
        layout1.addWidget(self.le1)
        layout1.addWidget(self.cbA)
        layout1.addWidget(self.bu1)
        
        self.tbl = QTableWidget(self)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.tbl)
        layout2.addWidget(self.canvas)
        
        self.canvas.draw()
               
        layoutA = QVBoxLayout()
        layoutA.addLayout(layout1)
        layoutA.addLayout(layout2)
        
        self.setLayout(layoutA)
        
        
        self.tbl.setRowCount(10)
        self.tbl.setColumnCount(4)
        self.col_head = ['date','pm10','pm25','o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        self.setWindowTitle('Graphic Exam')
        self.setGeometry(500, 200, 500, 700)
        self.show()
        
    def cbAev(self) :
        
        strArea = self.cbA.currentText() 
        encoderArea = parse.quote_plus(strArea)  
        #입력한 문자열을 인코딩을위한 코드로 변환
        
        url ="http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&sidoName="+ encoderArea +"&ver=1.0"
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.le1.setText(self.cbA.currentText())
        # currentText():현재보여지는 항목
        
        # QMessageBox.about(self,'title', str(self.cbA.currentIndex()))
        # 선택항목의 위치 표시
        
        dt = []
        xpm10 = []
        xpm25 = []
        xo3 = []
        
        row = 0 
        for item in self.air.findAll('item') :
            for time in item.findAll('datatime'):
                self.tbl.setItem(row, 0, QTableWidgetItem(time.string))
                strT = time.string
                dt.append(strT[11:])
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(row,1,QTableWidgetItem(pm10.string))
                xpm10.append(int(pm10.string))
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(row,2,QTableWidgetItem(pm25.string))
                xpm25.append(int(pm25.string))
            for o3 in item.findAll('o3value'):
                self.tbl.setItem(row,3,QTableWidgetItem(o3.string))
                xo3.append(float(o3.string))
            row += 1
            
        # 막대그래프 나타내 보기
        
        
        
        
    def bu1ev(self) :
        
        strArea = self.le1.text() 
        encoderArea = parse.quote_plus(strArea)  
        #입력한 문자열을 인코딩을위한 코드로 변환
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&stationName="+ encoderArea +"&dataTerm=DAILY&ver=1.0"
        
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        dt = []
        xpm10 = []
        xpm25 = []
        xo3 = []
        
        row = 0 
        for item in self.air.findAll('item') :
            for time in item.findAll('datatime'):
                self.tbl.setItem(row, 0, QTableWidgetItem(time.string))
                strT = time.string
                dt.append(strT[11:])
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(row,1,QTableWidgetItem(pm10.string))
                xpm10.append(int(pm10.string))
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(row,2,QTableWidgetItem(pm25.string))
                xpm25.append(int(pm25.string))
            for o3 in item.findAll('o3value'):
                self.tbl.setItem(row,3,QTableWidgetItem(o3.string))
                xo3.append(float(o3.string))
            row += 1
        
        dt.reverse() # 역순
        xpm10.reverse()
        xpm25.reverse()
        xo3.reverse()
            
        ax1 = self.fig.add_subplot(111)
        ax1.clear() # 그래프 영역 초기화 (sbuplot 각각필요)
        
        ax1.plot(dt, xpm10, 'r--', label = 'pm10')
        ax1.plot(dt, xpm25, 'b-.', label = 'pm25')
        ax1.plot(dt, xo3, 'g:', label = 'o3')
        ax1.legend()
        
        
        self.canvas.draw()
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
