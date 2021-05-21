import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt06.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
    
    def pbClick(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        c = 0
        
        for i in range(a, b+1):
            if i % 2 == 0:
                c += i
        
        self.le3.setText(str(c))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()