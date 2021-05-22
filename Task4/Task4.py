from UI import Ui_MainWindow
from UI import *
from PyQt5 import QtCore, QtGui,QtWidgets
import cv2
from threshold import *

class Task4 (Ui_MainWindow):
    def __init__(self,MainWindow):
        super(Task4,self).setupUi(MainWindow)
        self.segm_input.setPixmap(QtGui.QPixmap("screenshots/seg3.png")) #set segmentation input image

        self.select_segm_algo.currentTextChanged.connect(self.display_segm) #calling a function when user select an segmentation algorithm
        self.select_thresh_algo.currentTextChanged.connect(self.display_thresh)
    def display_segm(self,value):
        if (value == "Mean Shift"):
            self.segm_output.setPixmap(QtGui.QPixmap("screenshots/mean_shift_result.jpg"))  #set mean shift segmentation output image
        
    def display_thresh(self, value):
        input = cv2.imread("screenshots/temp.jpg")
        if(value == "Optimal(G)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/optimal_global.png"))
        elif(value == "Otsu(G)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/otsu_global.png"))
        elif(value == "Spectral(G)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/spectral_global.png"))
        elif(value == "Optimal(L)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/optimal_local.png"))
        elif(value == "Otsu(L)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/otsu_local.png"))
        elif(value == "Spectral(L)"):
            self.thesh_output.setPixmap(QtGui.QPixmap("screenshots/spectral_local.png"))
if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Task4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())