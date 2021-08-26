import socket
import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import pymysql
from matplotlib import font_manager, rc


class App (QWidget) :
    def __init__(self) :
        super().__init__()
        self.initui()
        
    def initui(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        self.conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql' , charset = 'utf8')
    
        self.cursor = self.conn.cursor()
        
        font_name = font_manager.FontProperties(fname='c:/windows/Fonts/batang.ttc').get_name()
        rc('font', family=font_name)   
        
        self.tbl = QTableWidget(20, 11)
        self.col_head = ['date','Temp1','Temp2','Temp3','Temp4','Temp5','Temp6','Temp7','Temp8','Temp9','Temp10']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        
        self.line = QLineEdit()
        self.combo = QComboBox()
        self.radi1 = QRadioButton()
        self.radi2 = QRadioButton()
        
        layouttbl = QVBoxLayout()
        layouttbl.addWidget(self.tbl)
        
        layoutsel = QHBoxLayout()
        layoutsel.addWidget(self.line)
        layoutsel.addWidget(self.radi1)
        layoutsel.addWidget(self.radi2)
        layoutsel.addWidget(self.combo)
        
        layoutcan = QVBoxLayout()
        layoutcan.addWidget(self.canvas)
        
        
        layoutAll = QVBoxLayout()
        layoutAll.addLayout(layouttbl)
        layoutAll.addLayout(layoutsel)
        layoutAll.addLayout(layoutcan)
        self.setLayout(layoutAll)
        

        self.setWindowTitle('Sensor Thread SQL Gui')
        self.setGeometry(400, 200, 1200, 700)
        self.show()
        
        
        HOST = '192.168.0.12'
        PORT = 9999
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        
        # 타이머 생성
        self.timer1 = QTimer(self) #Qtcore에 소속되어있음
        self.timer1.start(1000) # 1000 = 1초
        self.timer1.timeout.connect(self.graph1) # 이벤트 함수 연결
        
        
        
    def dbupdate(self) :
        sql = 'select * from tblsensor order by ts_date desc limit 20'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        self.graph1()
        
 
    def graph1(self) :
        data = self.client_socket.recv(1024)
    
        now = datetime.datetime.today() # 현재 시스템 날짜 및 시간
        nowstr = now.strftime('%Y-%m-%d  %H:%M:%S') # 형식을 만들어서 문자열로 저장
        print(nowstr)
        
        rs = data.decode().split(':') # 콜론을 구분자로 모든 데이터를 분리(리스트생성)
        print(rs)
        
        df0 = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
        
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.clear()
        self.ax1.bar(df0, rs)
        
        self.canvas.draw()
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 