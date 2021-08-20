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
        
        self.dbupdate()
        
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
        self.conn.close()
        
    def dbupdate(self) :
        self.df0 = [] #시간용
        self.df1 = [] #센서1
        
        sql = 'select * from tblsensor order by ts_date desc limit 20'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        
        row = 0
        for item in result:
            for col in range(11) :
                self.tbl.setItem(row,col,QTableWidgetItem(str(item[col])))
                strtime = item[0]
            self.df0.append(strtime[12:]) #시간 데이터
            self.df1.append(item[1]) #첫번째 센서테이터
            row += 1
        
        self.df0.reverse()
        self.df1.reverse()
        self.graph1()
    
        
    def graph1(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.clear()
        
        self.ax1.bar(self.df0, self.df1)
        
        self.canvas.draw()
        

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 