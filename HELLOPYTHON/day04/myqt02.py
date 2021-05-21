import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt02.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
    
    def pbClick(self):
        a = int(self.lbl.text())
        a += 1
        self.lbl.setText(str(a))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()