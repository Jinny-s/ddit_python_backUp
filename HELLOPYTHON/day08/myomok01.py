import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QSize, QRect

form_class = uic.loadUiType("myomok01.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.pb_reset.clicked.connect(self.pbReset)
        self.arr2D = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
            ]
        self.pb2D = []
        
        for i in range(10):
            pb_line = []
            for j in range(10):
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
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:    
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                else:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                    
    def btnClick(self):
        tg = self.sender().toolTip()
        i = int(tg.split(',')[0])
        j = int(tg.split(',')[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        if self.flag_wb:
            self.arr2D[i][j] = 1
        else:
            self.arr2D[i][j] = 2
        
        self.flag_wb = not self.flag_wb
        self.myrender()
        
    def pbReset(self):
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
        self.flag_wb = True
        self.myrender()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()