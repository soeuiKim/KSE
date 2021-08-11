import pymysql
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QPushButton, QMessageBox)

class App (QWidget) :
    
    def __init__(self) :
       
        super().__init__()
       
        self.DBconn()
        
        self.initui()
    
    def initui(self) :
        
        self.lbltitle = ['제품번호','제품명','재고량','단가','제조업체']
        
        self.lbl1 = QLabel('제품번호',self)
        self.lbl1.setGeometry(20, 30, 100, 30)
        self.lbl1.setStyleSheet("color : #ffffff;" 
                                "background-color : #787878;"
                                "border-width : 1px;" 
                                "border-style: solid;")
        self.le1 = QLineEdit(self)
        self.le1.setGeometry(140, 30, 100, 30)
        
        
        self.lbl2 = QLabel('제품명',self)
        self.lbl2.setGeometry(20, 60, 100, 30)
        self.lbl2.setStyleSheet("color : #ffffff;" 
                                "background-color : #787878;"
                                "border-width : 1px;" 
                                "border-style: solid;")
        self.le2 = QLineEdit(self)
        self.le2.setGeometry(140, 60, 100, 30)
        
        
        self.lbl3 = QLabel('재고량',self)
        self.lbl3.setGeometry(20, 90, 100, 30)
        self.lbl3.setStyleSheet("color : #ffffff;" 
                                "background-color : #787878;"
                                "border-width : 1px;" 
                                "border-style: solid;")
        self.le3 = QLineEdit(self)
        self.le3.setGeometry(140, 90, 100, 30)
                
        
        self.lbl4 = QLabel('단가',self)
        self.lbl4.setGeometry(20, 120, 100, 30)
        self.lbl4.setStyleSheet("color : #ffffff;" 
                                "background-color : #787878;"
                                "border-width : 1px;" 
                                "border-style: solid;")
        self.le4 = QLineEdit(self)
        self.le4.setGeometry(140, 120, 100, 30)
        
        
        self.lbl5 = QLabel('제조업체',self)
        self.lbl5.setGeometry(20, 150, 100, 30)
        self.lbl5.setStyleSheet("color : #ffffff;" 
                                "background-color : #787878;"
                                "border-width : 1px;" 
                                "border-style: solid;")
        self.le5 = QLineEdit(self)
        self.le5.setGeometry(140, 150, 100, 30)
        
        
        
        self.btn1 = QPushButton('insert', self)
        self.btn1.setGeometry(10, 200, 50, 30)
        self.btn1.clicked.connect(self.btn1Handler)
        
        
        
        self.btn2 = QPushButton('Load', self)
        self.btn2.setGeometry(60, 200, 50, 30)
        self.btn2.clicked.connect(self.btn2Handler)   
        
        
        
        self.btn3 = QPushButton('previous', self)
        self.btn3.setGeometry(110, 200, 70, 30)
        self.btn3.clicked.connect(self.btn3Handler)   
        
        
        
        self.btn4 = QPushButton('next', self)
        self.btn4.setGeometry(180, 200, 50, 30)
        self.btn4.clicked.connect(self.btn4Handler)  
        
        
        self.lbl6 = QLabel('number',self)
        self.lbl6.setGeometry(250, 200, 100, 30)
        self.lbl6.setStyleSheet("color : white;"
                                "background-color : black;")
        
        
        self.lef = QLineEdit(self)
        self.lef.setGeometry(30, 250, 150, 30)
        
        self.bntf = QPushButton('조회',self)
        self.bntf.setGeometry(200, 250, 50, 30)
        self.bntf.clicked.connect(self.btnf)
        
        self.tbl = QTableWidget(self)
        # self.tbl.setRowCount(1)  로드할때 몇개의 행이 구성될지 모르니까
        self.tbl.setColumnCount(5) 
        self.tbl.setGeometry(20, 300, 550, 350)
        self.col_head = ['제품번호','제품명','재고량','단가','제조업체']
        # row 나 column이 없으면 head는 나타나지 않음
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        # 테이블의 셀 클릭 이벤트
        self.tbl.cellClicked.connect(self.tblcellh)
        
        

        self.setWindowTitle('DB Exam _my sql insert')
        self.setGeometry(400, 130, 800, 800)
        self.show()
        
        
    def tblcellh(self, row, col) :
        # cellinfo = " %d : %d" % (row,col)
        # QMessageBox.about(self, '정보',cellinfo)
        
        sql = "select * from 제품"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        
        self.cnt = len(self.result) 
        
        self.currec = 0 
        
        item = self.result[0] 
        self.le1.setText(item[0]) 
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4])
        
        strrec = "%d / %d" % (self.currec+1, self.cnt)
        self.lbl6.setText(strrec)
        

    def btnf(self) :
        
        sql = "select * from 제품 where 제품명 = %s"
        self.cursor.execute(sql, (self.lef.text()))
        self.result = self.cursor.fetchall()
        to = len(self.result)
        if to > 0 :
            item = self.result[0]  
            self.le1.setText(item[0]) 
            self.le2.setText(item[1])
            self.le3.setText(str(item[2]))
            self.le4.setText(str(item[3]))
            self.le5.setText(item[4]) 
        else : # 조회실패시
            QMessageBox.about(self, '정보', '검색결과가 없습니다')
            
    def btn1Handler(self) :
        sql = "insert into 제품 values (%s,%s,%s,%s,%s)"
        val1 = self.le1.text()
        val2 = self.le2.text()
        val3 = self.le3.text()
        val4 = self.le4.text()
        val5 = self.le5.text()
        self.cursor.execute(sql,(val1,val2,val3,val4,val5))
        self.conn.commit()
        # 메세지박스 출력
        QMessageBox.about (self,'정보','입력되었습니다.')
        # 기존 상자 내용 지우기
        self.le1.setText('')
        self.le2.setText('')
        self.le3.setText('')
        self.le4.setText('')
        self.le5.setText('')
    
    def btn2Handler(self) :
        sql = "select * from 제품"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        # result 변수에 모든 레코드가 반환됨
        
        self.cnt = len(self.result) # 전체 레코드 갯수
        
        self.tbl.setRowCount(self.cnt)
        
        self.currec = 0  # 레코드 번호
        item = self.result[0]  # item 에 첫번째 레코드 반환
        self.le1.setText(item[0]) 
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4])
        
        strrec = "%d / %d" % (self.currec+1, self.cnt)
        self.lbl6.setText(strrec)
        
        row = 0
        for item in self.result : # 레코드 갯수만큼 반복
            for col in range(5) : # 열구성
                self.tbl.setItem(row,col,QTableWidgetItem(str(item[col])))
            row += 1
            
    
        QMessageBox.about (self,'정보','제품테이블이 로드되었습니다.')
        
    def btn3Handler(self) :
        self.currec -= 1
        if self.currec < 0 :
            self.currec = 0
            QMessageBox.about (self,'정보','첫번째 자료입니다')
        
        item = self.result[self.currec]  
        self.le1.setText(item[0]) 
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4]) 
    
        strrec = "%d / %d" % (self.currec+1, self.cnt)
        
        
    def btn4Handler(self) :
        self.currec += 1 
        if self.currec >= self.cnt :
            self.currec = self.cnt-1
            QMessageBox.about (self,'정보','마지막 자료입니다.')
        
        item = self.result[self.currec]  
        self.le1.setText(item[0]) 
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4]) 
        
        strrec = "%d / %d" % (self.currec+1, self.cnt)
        self.lbl6.setText(strrec)
        
        
        
    def DBconn(self) :
        self.conn = pymysql.connect(host='127.0.0.1', user = 'bigdata', password   = '12345678', db = 'mysql' , charset = 'utf8')
        self.cursor = self.conn.cursor()


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
