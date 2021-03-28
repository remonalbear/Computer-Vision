from UI import * 
import pyqtgraph
from PyQt5 import QtCore, QtGui,QtWidgets
import cv2 as cv
import numpy as np
import random


class GUI(Ui_MainWindow):
    def __init__(self,MainWindow):
        super(GUI,self).setupUi(MainWindow) 

        self.images=[self.filteredImage,self.noiseImage,self.edgeDetectionImage,
                    self.freqeuncyFilteredImage,self.equalizedImage,self.normalizedImage,
                    self.originalImage,self.redChannel,self.greenChannel,self.blueChannel,
                    self.imageOne,self.imageTwo,self.mixedImage,self.grayScaleImage]    
        #removing unwanted options from the image display widget
        for i in range(len(self.images)):
            self.images[i].ui.histogram.hide()
            self.images[i].ui.roiPlot.hide()
            self.images[i].ui.roiBtn.hide()
            self.images[i].ui.menuBtn.hide() 
        #noise slide configrations
        self.noiseSlider.setValue(20)
        self.noiseSlider.setMaximum(50)
        self.noiseSlider.setMinimum(0) 
        self.noiseSlider.valueChanged.connect(self.noiseSliderChange)
        self.noiseSliderValue=20
        #display the original image
        self.originalImageData=cv.imread('D:\CV\Task1\\test.jpg',0)
        self.originalImage.setImage(self.originalImageData.T)    
        self.originalImage.show()
        #link events with functions   
        self.noiseOptions.currentTextChanged.connect(self.applyNoise)
        self.applyNoise("Uniform")
    def noiseSliderChange(self):
        self.noiseSliderValue=self.noiseSlider.value()
        self.applyNoise(self.noiseOptions.currentText())
    def applyNoise(self,value):
        self.noiseImageData=np.array(self.originalImageData.copy())
        if (value == "Guassian"):
            self.noiseImageData=self.noiseImageData+np.random.normal(0,self.noiseSliderValue**.5,self.noiseImageData.shape)
        elif(value == "Salt & Pepper"):
            prop=self.noiseSliderValue/200.0
            thresh=1-prop
            for i in range(self.originalImageData.shape[0]):
                for j in range(self.originalImageData.shape[1]):
                    rand=random.random()
                    if rand<prop :
                        self.noiseImageData[i][j]=0
                    elif rand>thresh:
                        self.noiseImageData[i][j]=255
        elif(value == "Uniform"):
            print("yes in uniform ")
            print("before",self.noiseImageData)
            self.noiseImageData =self.noiseImageData+self.noiseSliderValue
            print("after",self.noiseImageData)
        self.noiseImage.setImage(self.noiseImageData.T)
        self.noiseImage.show()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  