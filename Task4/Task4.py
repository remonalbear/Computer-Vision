from UI import Ui_MainWindow
from UI import *
from PyQt5 import QtCore, QtGui,QtWidgets


class Task4 (Ui_MainWindow):
    def __init__(self,MainWindow):
        super(Task4,self).setupUi(MainWindow)
        self.segm_input.setPixmap(QtGui.QPixmap("screenshots/seg3.png")) #set segmentation input image

        self.select_segm_algo.currentTextChanged.connect(self.display_segm) #calling a function when user select an segmentation algorithm
    def display_segm(self,value):
        if (value == "Mean Shift"):
            self.segm_output.setPixmap(QtGui.QPixmap("screenshots/mean_shift_result.jpg"))  #set mean shift segmentation output image
        

if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Task4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())