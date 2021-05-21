import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt09.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.pbClick0)
        self.pb1.clicked.connect(self.pbClick1)
        self.pb2.clicked.connect(self.pbClick2)
        self.pb3.clicked.connect(self.pbClick3)
        self.pb4.clicked.connect(self.pbClick4)
        self.pb5.clicked.connect(self.pbClick5)
        self.pb6.clicked.connect(self.pbClick6)
        self.pb7.clicked.connect(self.pbClick7)
        self.pb8.clicked.connect(self.pbClick8)
        self.pb9.clicked.connect(self.pbClick9)
        self.pbCall.clicked.connect(self.pbClickCall)
            
    def pbClick0(self):
        str_new = self.pb0.text()
        self.phoneNum(str_new)
        
    def pbClick1(self):
        str_new = self.pb1.text()
        self.phoneNum(str_new)
        
    def pbClick2(self):
        str_new = self.pb2.text()
        self.phoneNum(str_new)
        
    def pbClick3(self):
        str_new = self.pb3.text()
        self.phoneNum(str_new)
        
    def pbClick4(self):
        str_new = self.pb4.text()
        self.phoneNum(str_new)
        
    def pbClick5(self):
        str_new = self.pb5.text()
        self.phoneNum(str_new)
        
    def pbClick6(self):
        str_new = self.pb6.text()
        self.phoneNum(str_new)
        
    def pbClick7(self):
        str_new = self.pb7.text()
        self.phoneNum(str_new)
        
    def pbClick8(self):
        str_new = self.pb8.text()
        self.phoneNum(str_new)
        
    def pbClick9(self):
        str_new = self.pb9.text()
        self.phoneNum(str_new)
        
    def pbClickCall(self):
        result = self.le.text()
        
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('Calling')
        self.msg.setText(result + "로 연결하시겠습니까?")
        
        retval = self.msg.exec_()
        self.le.setText('')
        
    def phoneNum(self, str_new):
        str_old = self.le.text()
        result = str_old + str_new
        self.le.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()