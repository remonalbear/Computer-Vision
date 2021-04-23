# from UI import * 
from numpy.core.fromnumeric import shape
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui,QtWidgets
from cv2 import cv2 as cv
from math import sqrt
import numpy as np
from PIL import Image
import matplotlib as plt
import random
from UI import Ui_MainWindow
from lines_hough import hough_lines

# from collections import Counter # Replaced


class GUI(Ui_MainWindow):
    def __init__(self,MainWindow):
        super(GUI,self).setupUi(MainWindow) 

        self.images=[self.cannyInputImage,self.cannyOutputImage,
                    self.activeContoursInputImage,self.activeContoursOutputImage]   

        #removing unwanted options from the image display widget
        for i in range(len(self.images)):
            self.images[i].ui.histogram.hide()
            self.images[i].ui.roiPlot.hide()
            self.images[i].ui.roiBtn.hide()
            self.images[i].ui.menuBtn.hide()
            self.images[i].view.setContentsMargins(0,0,0,0)
            self.images[i].view.setAspectLocked(False)
            self.images[i].view.setRange(xRange=[0,100],yRange=[0,100], padding=0)

        #retrieve the original image data
        hough_lines("linesInput.jpg")
        
        
    
    
        
######################################################################################################



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  