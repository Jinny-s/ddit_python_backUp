import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtGui

form_class = uic.loadUiType("myqt01.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.index = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.pbClick)
        
        
    def pbClick(self):
        self.index += 1
        loc_index = self.index % 3
        self.pb.setIcon(QtGui.QIcon(str(loc_index)+'.png'))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()