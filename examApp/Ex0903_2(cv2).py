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
import cv2



class App (QWidget) :
    
    def __init__(self) :
        super().__init__()
        
        self.initui()
        
    def initui(self):
        font_name = font_manager.FontProperties(fname='c:/windows/Fonts/batang.ttc').get_name()
        rc('font', family=font_name)   
        
        self.img1_ = cv2.imread('C:\KSE\examApp/image1.jpg') 
        self.img2_ = cv2.imread('C:\KSE\examApp/image2.jpg') 
        self.img3_ = cv2.imread('C:\KSE\examApp/image3.jpg') 
        
        self.lne = QLineEdit(self)
        self.but = QPushButton('조회',self)
        self.but.clicked.connect(self.buteve)
        
        layout1 = QHBoxLayout()
        layout1.addWidget(self.lne)
        layout1.addWidget(self.but)
        
        self.tbl = QTableWidget(10,4)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.tbl)
        
        self.rbu1 = QRadioButton('type1')
        self.rbu2 = QRadioButton('type2')
        self.rbu3 = QRadioButton('type3')
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
        
        
        self.setWindowTitle('cv2')
        self.setGeometry(200, 200, 700, 700)
        self.show()
        
    def rbueve(self) :
        if self.rbu1.isChecked() :
            self.graph1()
        elif self.rbu2.isChecked() :
            self.graph2()
        else : 
            self.graph3()
    
    def graph1(self) :
        self.fig.clear() 
        self.ax1 = self.fig.add_subplot(111) # 이미지영역설정
        self.ax1.axis('off')
       
        self.img1 = cv2.cvtColor(self.img1_, cv2.COLOR_BGR2RGB)
       
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.img1, 'Hello world', (50,80), font, 1, (255,255,255), 3)
        cv2.putText(self.img1, 'Hello my only Load', (self.img1.shape[1] - 350,self.img1.shape[0] - 50), font, 1, (255,255,255), 3)
        
        self.ax1.imshow(self.img1)    
        self.canvas.draw()
        
    def graph2(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(121)
        self.ax1.axis('off')
        self.img1 = cv2.cvtColor(self.img1_, cv2.COLOR_BGR2RGB)
        
        self.ax2 = self.fig.add_subplot(122)
        self.ax2.axis('off')
        self.img2 = cv2.cvtColor(self.img2_, cv2.COLOR_BGR2RGB)
       
        self.ax1.imshow(self.img1)        
        self.ax2.imshow(self.img2)        
        
        self.canvas.draw()
    
    def graph3(self) :
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(131)
        self.ax1.axis('off')
        img1__= cv2.resize(self.img1_, dsize= (320,240))
        self.img1 = cv2.cvtColor(img1__, cv2.COLOR_BGR2RGB)
        
        self.ax2 = self.fig.add_subplot(132)
        self.ax2.axis('off')
        img2__= cv2.resize(self.img2_, dsize= (320,240))
        self.img2 = cv2.cvtColor(img2__, cv2.COLOR_BGR2RGB)
       
        self.ax3 = self.fig.add_subplot(133)
        self.ax3.axis('off')
        img3__= cv2.resize(self.img3_, dsize= (320,240))
        self.img3 = cv2.cvtColor(img3__, cv2.COLOR_BGR2RGB)
        
        self.ax1.imshow(self.img1)        
        self.ax2.imshow(self.img2)        
        self.ax3.imshow(self.img3)        
        
        
        self.canvas.draw()
        
# =============================================================================
#         1) numstr = '%dx%d' % (self.img1_.shape[1],self.img1_.shape[2])
#             shape 대입형식으로 변수저장해서 사이즈 변화
#         
#         2) aa, bb, _ = self.img1_.shape
#                (↑버리는 값 )
#              각각 변수에 shape값을 저장해서 사용
# =============================================================================
        
        
    def buteve(self) :
        self.fig.clear() 
        self.ax1 = self.fig.add_subplot(111) # 이미지영역설정
        self.ax1.axis('off')
       
        self.img1 = cv2.cvtColor(self.img1_, cv2.COLOR_BGR2RGB)
       
        self.ax1.imshow(self.img1)        
       
        self.canvas.draw()
       
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 