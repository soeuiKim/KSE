
import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class App (QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initui()
        
    
    def initui(self) :
        
        conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql' , charset = 'utf8')
        
        cursor = conn.cursor()
        
        sql = 'select * from 제품'
        cursor.execute(sql)
        result = cursor.fetchall()
        cnt = len(result)
        
        self.tbl = QTableWidget(cnt, 5, self)
        self.tbl.setGeometry(30, 30, 700, 300)
        self.col_head = ['제품번호','제품명','재고량','단가','제조업체']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        
        row = 0
        for item in result : # 레코드 갯수만큼 반복
            for col in range(5) : # 열구성
                self.tbl.setItem(row,col,QTableWidgetItem(str(item[col])))
            row += 1
        
        self.setWindowTitle('my sql')
        self.setGeometry(400, 300, 800, 500)
        self.show()
        
        
    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    
    