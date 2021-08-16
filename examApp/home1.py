import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse
from matplotlib import font_manager, rc


class soeui (QWidget) :
    def __init__(self) :
        super().__init__()
        self.initui()
    def initui(self) :
        font_name = font_manager.FontProperties(fname='c:/windows/Fonts/batang.ttc').get_name()
        rc('font', family=font_name)
        
        self.bu1 = QPushButton('colick', self)
        self.bu2 = QPushButton('colick2', self)
        self.bu1.clicked.connect(self.bu1cl)
        self.bu2.clicked.connect(self.bu2cl)
        
        layout1 = QVBoxLayout()
        layout1.addWidget(self.bu1)
        layout1.addWidget(self.bu2)
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.canvas)
        
        layoutAll = QHBoxLayout()
        layoutAll.addLayout(layout1)
        layoutAll.addLayout(layout2)
        
        self.setLayout(layoutAll)
        
        self.setWindowTitle('home test')
        self.setGeometry(200, 200, 500, 500)
        self.show()
        
    def bu1cl(self):
        
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ZsmPBe%2FeXla3HBKm7yEIeD5OLFpLY6jr0w6Qx5SXFhAuh33cjUei2weBHfE4%2FdiEAJaEQpENvyhvM4qK%2FQSzgw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
        
        res = ulib.urlopen(url)
        self.air = BeautifulSoup(res, 'html.parser')
        
        self.stn = []
        self.xpm10 = []
        self.xpm25 = []
        
        col = 0
        for item in self.air.findAll('item') :
            for stname in item.findAll('stationname'):
                self.stn.append(stname.string)
            for pm10 in item.findAll('pm10value'):
                if pm10 == '-' :
                    pm10.append('0')
                self.xpm10.append(int(pm10.string))
            for pm25 in item.findAll('pm25value'):
                if pm25 == '-' :
                    pm25.append('0')
                self.xpm25.append(int(pm25.string))
            col += 1
            
        ax = self.fig.add_subplot(111)
        ax.bar(self.stn , self.xpm10)
        self.canvas.draw()
        
        
        
        
        
        
        
        
        
        # X = np.arange(-5, 5, 0.25)
        # Y = np.arange(-5, 5, 0.25)
        # X, Y = np.meshgrid(X, Y)
        # Z = X**2 + Y**2
        
        # self.fig.clear()
        
        # ax = self.fig.gca(projection='3d')
        # ax.plot_wireframe(X, Y, Z, color='black')
        # self.canvas.draw() 
        
        
        
        
        
    def bu2cl(self) :
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        
        self.fig.clear()
        
        ax1 = self.fig.add_subplot(111)
        ax1.plot(X,Y)
        ax1.bar(X,X*2)
        
        self.canvas.draw()
    
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = soeui()
    sys.exit(app.exec_())