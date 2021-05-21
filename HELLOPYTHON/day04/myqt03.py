import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt03.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
    
    def pbClick(self):
        a = int(self.le1.text()) + int(self.le2.text())
        self.le3.setText(str(a))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
    