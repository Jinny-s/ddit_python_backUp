import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt08.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
    
    def pbClick(self):
        a = int(self.le.text())
        b = 0
        result = ""
        
        for i in range(1, 10):
            b = a * i
            result += str(a) + "*" + str(i) + "=" + str(b) + "\n"
        
        self.te.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()