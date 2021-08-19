import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from pymongo import MongoClient





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
        
        self.btnAll = QPushButton('All', self)
        self.btnAll.setGeometry(300, 30, 100, 30)
        self.btnAll.clicked.connect(self.btnAllEv)
        
        
        self.tbl = QTableWidget(self)
        self.tbl.setColumnCount(2)
        self.tbl.setGeometry(10, 100, 450, 250)
        self.col_head = ['name','price']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        self.setWindowTitle('Graphic Exam')
        self.setGeometry(550, 350, 500, 400)
        self.show()
    
    def btnFindEv(self) :
        conn = MongoClient('mongodb://localhost:27017/')
        db = conn['test'] 
        collection = db['product'] 
        
        
        findstr = self.leAre.text()
        
        cnt = 0
        if len(findstr) > 0 :
            query = {'name' : findstr}
            cnt = collection.find(query).count()
        else :
            query = {}
            cnt = collection.find().count()
            
        result = collection.find(query)
        
        if cnt > 0 :
            self.tbl.setRowCount(cnt)
            row = 0
            for item in result :
                self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
                self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
                row += 1
        else :
            self.tbl.setRowCount(cnt)
                
            
        '''
        if findstr == "" :
            QMessageBox.about(self, 'oops', 'name을 입력하세요')
            result = collection.find()
            
            row = 0
            for item in result :
                self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
                self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
                row += 1
                
        else :       
            query = {'name' : findstr}
            result = collection.find(query) # 조건검색
        
            cnt = result.count() # 조회결과 행수
        
            self.tbl.setRowCount(cnt)
        
            row = 0
            for item in result :
                self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
                self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
                row += 1
        '''
        
    def btnAllEv(self) :
        conn = MongoClient('mongodb://localhost:27017/')
        db = conn['test'] 
        collection = db['product'] 
        
        result = db.product.find() # 전체검색
        
        cnt = collection.find().count() # 조회결과 행수
        
        self.tbl.setRowCount(cnt)
        
        row = 0
        for item in result :
            self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
            self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
            row += 1
            

    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    