import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt07.ui")[0]

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
        if ran < 0.33:
            com = "가위"
        elif ran < 0.66:
            com = "바위"
        else:
            com = "보"
        
        if user == com:
            result = "DRAW!"
        elif (user == "가위" and com == "보") or (user=="바위" and com =="가위") or (user=="보" and com =="바위"):
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