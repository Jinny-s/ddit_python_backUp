
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt05.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
    
    def pbClick(self):
        user = self.leUser.text()
        com = ""
        result = ""

        ran = random.random()
        if ran < 0.5:
            com = "홀"
        else:
            com = "짝"
        
        if user == com:
            result = "WIN!"
        else:
            result = "LOSE!"
            
        self.leCom.setText(com)
        self.leResult.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()    