import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QSize, QRect

form_class = uic.loadUiType("myomok20.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_bw = True
        self.flag_ing = True
        self.pb_reset.clicked.connect(self.pbReset)
        self.arr2D = [[0 for col in range(20)] for row in range(20)]
        
        # 컴퓨터 임시 좌표
        self.arr_seq = [
            {'i':0, 'j':0},
            {'i':0, 'j':1},
            {'i':0, 'j':2},
            {'i':0, 'j':3},
            {'i':0, 'j':4}
        ]
        self.arr_idx = 0
        
        self.pb2D = []
        
        for i in range(20):
            pb_line = []
            for j in range(20):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(40*j,40*i, 40, 40))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        self.myrender()
    
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:    
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                else:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                    
    def btnClick(self):
        if not self.flag_ing:
            return
        
        tg = self.sender().toolTip()
        i = int(tg.split(',')[0])
        j = int(tg.split(',')[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 1
        self.arr2D[i][j] = 1
        
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        le = self.getLE(i,j,stone)
        ri = self.getRI(i,j,stone)
        lu = self.getLU(i,j,stone)
        rd = self.getRD(i,j,stone)
        ru = self.getRU(i,j,stone)
        ld = self.getLD(i,j,stone)
        
        D1 = up + 1 + dw
        D2 = le + 1 + ri
        D3 = lu + 1 + rd
        D4 = ru + 1 + ld
        
        self.myrender()
        
        if D1 == 5 or D2 == 5 or D3 == 5 or D4 == 5:
            QMessageBox.about(self, "오목 경기 결과", "흑돌 승리!")
            self.flag_ing = False
            return
        
        self.flag_bw = not self.flag_bw
        
        
        # 컴퓨터
        com_i = self.arr_seq[self.arr_idx]['i']
        com_j = self.arr_seq[self.arr_idx]['j']
        
        stone = 2
        self.arr2D[com_i][com_j] = 2
        self.arr_idx = self.arr_idx + 1  
        
        up = self.getUP(com_i,com_j,stone)
        dw = self.getDW(com_i,com_j,stone)
        le = self.getLE(com_i,com_j,stone)
        ri = self.getRI(com_i,com_j,stone)
        lu = self.getLU(com_i,com_j,stone)
        rd = self.getRD(com_i,com_j,stone)
        ru = self.getRU(com_i,com_j,stone)
        
        D1 = up + 1 + dw
        D2 = le + 1 + ri
        D3 = lu + 1 + rd
        D4 = ru + 1 + ld
        
        self.myrender()
        
        if D1 == 5 or D2 == 5 or D3 == 5 or D4 == 5:
            QMessageBox.about(self, "오목 경기 결과", "백돌 승리!")
            self.flag_ing = False
        
        self.flag_bw = not self.flag_bw
        
    def getUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt    
        
    def getRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt    
        
    def getLU(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt   
         
    def getRD(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt    
        
    def getRU(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt    
        
    def getLD(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt    
        
    def pbReset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        self.flag_bw = True
        self.flag_ing = True
        
        # 컴터임시
        self.arr_idx = 0
        
        self.myrender()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()