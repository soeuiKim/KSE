import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class App (QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initui()
        
    def initui(self):
        
        self.le1 = QLineEdit()
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        ax1 = self.fig.add_subplot(221)
        data1 = [1,2,3,4]
        data2 = [1,4,9,16]
        ax1.plot(data1,data2) # x,y 값 리스트로 부여
        
        ax2 = self.fig.add_subplot(222)
        data1 = [1,2,3,4]
        data2 = [1,9,2,15]
        ax2.plot(data1,data2)
        
        ax3 = self.fig.add_subplot(223)
        data1 = [1,2,3,4]
        data2 = [3,5,7,9]
        ax3.plot(data1,data2)
        
        ax4 = self.fig.add_subplot(224)
        data1 = [1,2,3,4]
        data2 = [4,9,7,1]
        ax4.plot(data1,data2)
        
        self.canvas.draw()
        
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.le1)
        
        layout = QHBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        
        layout.setStretchFactor(layout1, 1)
        layout.setStretchFactor(layout2, 0)
        
        
        self.setLayout(layout)
        
        
        self.setWindowTitle('Graphic Exam')
        self.setGeometry(300, 200, 1200, 600)
        self.show()
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
