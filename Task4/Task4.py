from UI import Ui_MainWindow
from UI import *
from PyQt5 import QtCore, QtGui,QtWidgets


class Task4 (Ui_MainWindow):
    def __init__(self,MainWindow):
        super(Task4,self).setupUi(MainWindow)


if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Task4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())