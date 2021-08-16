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
        
        self.le1 = QLineEdit(self)
        self.le1.setText('종로구')
        
        self.bu1 = QPushButton('조회',self)
        self.bu1.clicked.connect(self.bu1ev)
        
        self.strArea1 = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
        self.strArea2 = ['종로구', '태종대','수창동','신흥','서석동','읍내동','울산항','목감동','중앙로','용담동','서천읍','삼천동','용당동','청송읍','대산면','이도동','신흥동']
        self.cbA = QComboBox()
        self.cbA.addItems(self.strArea1)
        self.cbA.activated.connect(self.cbAev)
        # 콤보박스에 항목을 변경해서 선택했을 경우
        
        
        layout1 = QHBoxLayout()
        layout1.addWidget(self.le1)
        layout1.addWidget(self.cbA)
        layout1.addWidget(self.bu1)
        
        self.tbl = QTableWidget(self)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.tbl)
        
        self.rbu1 = QRadioButton('type1')
        self.rbu2 = QRadioButton('type2')
        self.rbu3 = QRadioButton('type3')
        self.rbu3.setChecked(True)
        self.rbu1.clicked.connect(self.rbuClick)
        self.rbu2.clicked.connect(self.rbuClick)
        self.rbu3.clicked.connect(self.rbuClick)
        layout3 = QHBoxLayout()
        layout3.addWidget(self.rbu1)
        layout3.addWidget(self.rbu2)
        layout3.addWidget(self.rbu3)
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        layout4 = QVBoxLayout()
        layout4.addWidget(self.canvas)
        
        self.canvas.draw()
               
        layoutA = QVBoxLayout()
        layoutA.addLayout(layout1)
        layoutA.addLayout(layout2)
        layoutA.addLayout(layout3)
        layoutA.addLayout(layout4)
        
        self.setLayout(layoutA)
        
        
        self.tbl.setRowCount(10)
        self.tbl.setColumnCount(4)
        self.col_head = ['date','pm10','pm25','o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        self.setWindowTitle('Graphic Exam')
        self.setGeometry(500, 200, 500, 700)
        self.show()
        
    def cbAev(self) :
        # self.le1.setText(self.cbA.currentText())
        
        self.le1.setText(self.strArea2[self.cbA.currentIndex()])
        
    def rbuClick(self) :
    # 버튼이 여러개일때 비슷한 이벤트가 발생한다면 비교구문을 넣어 한개의 이벤트만 생성
        if self.rbu1.isChecked() :
            self.graph1()
        elif self.rbu2.isChecked() :
            self.graph2()
        else : 
            self.graph3()
            
            
    def bu1ev(self) :
        
        strArea = self.le1.text() 
        encoderArea = parse.quote_plus(strArea)  
        #입력한 문자열을 인코딩을위한 코드로 변환
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&stationName="+ encoderArea +"&dataTerm=DAILY&ver=1.0"
        
        
        res = ulib.urlopen(url) 
        self.air = BeautifulSoup(res,'html.parser') 
        
        self.dt = []
        self.xpm10 = []
        self.xpm25 = []
        self.xo3 = []
        
        row = 0 
        for item in self.air.findAll('item') :
            for time in item.findAll('datatime'):
                self.tbl.setItem(row, 0, QTableWidgetItem(time.string))
                strT = time.string
                self.dt.append(strT[11:])
            for pm10 in item.findAll('pm10value'):
                self.tbl.setItem(row,1,QTableWidgetItem(pm10.string))
                
                if pm10 == '-' :
                    pm10.delete('-')
                    pm10.append(0)
                self.xpm10.append(int(pm10.string))
            for pm25 in item.findAll('pm25value'):
                self.tbl.setItem(row,2,QTableWidgetItem(pm25.string))
                
                if pm25 == '-' :
                    pm25.delete('-')
                    pm.append(0)
                self.xpm25.append(int(pm25.string))
            for o3 in item.findAll('o3value'):
                self.tbl.setItem(row,3,QTableWidgetItem(o3.string))
                
                if pm10 == '-' :
                    pm10.delete('-')
                    pm10.append(0)
                self.xo3.append(float(o3.string))
            row += 1
            
        self.dt.reverse() # 역순
        self.xpm10.reverse()
        self.xpm25.reverse()
        self.xo3.reverse()
        
        self.graph3()
        
        
    def graph1(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.clear()
        
        self.ax1.plot(self.dt, self.xpm10, 'r--', label = '미세먼지')
        self.ax1.legend()
        
        self.canvas.draw()
    
    def graph2(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        self.ax1.clear()
        self.ax2.clear()
        
        self.ax1.plot(self.dt, self.xpm10, 'r--', label = '미세먼지')
        self.ax2.plot(self.dt, self.xpm25, 'b-.', label = '초미세먼지')
        self.ax1.legend()
        self.ax2.legend()
        
        self.canvas.draw()
        
    def graph3(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(311)
        self.ax2 = self.fig.add_subplot(312)
        self.ax3 = self.fig.add_subplot(313)
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        
        self.ax1.plot(self.dt, self.xpm10, 'r--', label = '미세먼지')
        self.ax2.plot(self.dt, self.xpm25, 'b-.', label = '초미세먼지')
        self.ax3.plot(self.dt, self.xo3, 'g:', label = '오존')
        self.ax1.legend()
        self.ax2.legend()
        self.ax3.legend()
        
        self.canvas.draw()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
