# from UI import * 
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui,QtWidgets
from cv2 import cv2 as cv
import numpy as np
from PIL import Image
import matplotlib as plt
import random
from UI import Ui_MainWindow
# from collections import Counter # Replaced


class GUI(Ui_MainWindow):
    def __init__(self,MainWindow):
        super(GUI,self).setupUi(MainWindow) 

        self.images=[self.filteredImage,self.noiseImage,self.edgeDetectionImage,
                    self.freqeuncyFilteredImage,self.equalizedImage,self.normalizedImage,
                    self.redChannel,self.greenChannel,self.blueChannel,
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
        #retrieve the original image data
        self.originalImageData=cv.imread('test.jpg')
        #display the grayscale image
        self.grayScaleImageData=cv.cvtColor(self.originalImageData, cv.COLOR_BGR2GRAY)
        self.grayScaleImage.setImage(self.grayScaleImageData.T)
        self.grayScaleImage.show()
        #link events with functions 
        self.noiseOptions.currentTextChanged.connect(self.applyNoise)
        self.applyNoise("Uniform")
    #add noise functions
    #rerender when the slider changed
    def noiseSliderChange(self):
        self.noiseSliderValue=self.noiseSlider.value()
        self.applyNoise(self.noiseOptions.currentText())
    #add the noise and display
    def applyNoise(self,value):
        self.noiseImageData=np.array(self.grayScaleImageData.copy())
        if (value == "Guassian"):
            self.noiseImageData=self.noiseImageData+np.random.normal(0,self.noiseSliderValue**.5,self.noiseImageData.shape)
        elif(value == "Salt & Pepper"):
            prop=self.noiseSliderValue/200.0
            thresh=1-prop
            for i in range(self.grayScaleImageData.shape[0]):
                for j in range(self.grayScaleImageData.shape[1]):
                    rand=random.random()
                    if rand<prop :
                        self.noiseImageData[i][j]=0
                    elif rand>thresh:
                        self.noiseImageData[i][j]=255
        elif(value == "Uniform"):
            # print("yes in uniform ")
            # print("before",self.noiseImageData)
            self.noiseImageData =self.noiseImageData+self.noiseSliderValue
            # print("after",self.noiseImageData)
        self.noiseImage.setImage(self.noiseImageData.T)
        self.noiseImage.show()

        
###################################################################################################

        def df(img):
            values = [0]*256
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    values[img[i,j]]+=1
            return values

        ## This part for Histogram Graph ###
        x = np.linspace(0, 255, num=256)
        y = df(self.grayScaleImageData)
        bg = pg.BarGraphItem(x=x, height=y, width=1, brush='r')
        self.originalHistogram.addItem(bg) # P.S. PlotItem type is: PlotWidget

###################################################################################################

        ## This part for Equalized Image ###
        def cdf(hist):
            cdf = [0] * len(hist)
            cdf[0] = hist[0]
            for i in range(1, len(hist)):
                cdf[i]= cdf[i-1]+hist[i]
            cdf = [ele*255/cdf[-1] for ele in cdf]
            return cdf
        def equalize_image(image):
            my_cdf = cdf(df(self.grayScaleImageData))
            image_equalized = np.interp(image, range(0,256), my_cdf)
            return image_equalized
        eq = equalize_image(self.grayScaleImageData)
        self.equalizedImage.ui.histogram.show()
        self.equalizedImage.setImage(eq.T) # P.S. PlotItem type is: ImageView

###################################################################################################

        ## This part for Normalized Image ###
        def normalize_image(img):
            minValue = 0
            maxValue = max(img.flatten())
            values = np.zeros(img.shape)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    values[i,j] = (img[i,j] - minValue)/(maxValue - minValue) * 255.0
            return values
        nr = normalize_image(self.grayScaleImageData)
        self.normalizedImage.ui.histogram.show()
        self.normalizedImage.setImage(nr.T) # P.S. PlotItem type is: ImageView
###################################################################################################

        ## This part for Global Thresholding ###
        def global_threshold(nor_image, threshold):
            image = np.array(nor_image)
            new_img = np.copy(image)
            try:
                for channel in range(image.shape[2]):
                    new_img[:, :, channel] = list(map(lambda row: list((255 if ele>threshold else 0) for ele in row) , image[:, :, channel]))
            except:
                new_img[:, :] = list(map(lambda row: list((255 if ele>threshold else 0) for ele in row) , image[:, :]))
            return Image.fromarray(new_img)
################################################################################################### 

        ## This part for Local Thresholding ###
        def local_threshold(nor_image, size, const):
            image = np.array(nor_image)
            new_img = np.copy(image)
            for channel in range(image.shape[2]):
                for row in range(0, image.shape[0], size):
                    for col in range(0, image.shape[1], size):
                        mask = image[row:row+size,col:col+size, channel]
                        threshold = np.mean(mask)-const
                        new_img[row:row+size,col:col+size, channel] = global_threshold(mask, threshold)
            return Image.fromarray(new_img)
################################################################################################### 

        ## This part for RGB 2 Gray_scale conversion ###
        def gry_conv(image):
            gry_img = np.dot(image[..., :3], [0.299, 0.587, 0.114])
            return gry_img
################################################################################################### 

        ## This part for Hybrid Images ###
        def hybrid_img(img1, img2):
            # convert image 1
            # convert image 2
            # hybrid = low_img1 + high_img2
            # return hybrid
######################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  