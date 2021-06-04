from face_recog import face_recog
from gui import Ui_MainWindow
from gui import *
from PyQt5 import QtCore, QtGui,QtWidgets
import numpy as np
import cv2 
from face_detection import face_detection
from face_recog import face_recog
class Task5 (Ui_MainWindow):
    def __init__(self,MainWindow):
        super(Task5,self).setupUi(MainWindow)
    path1 = 'screenshots\\faces.jpeg'
    path2 = 'test.pgm'
    num, det_img = face_detection(path1)
    rec_img = face_recog(path2)

if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Task5(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())