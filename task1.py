# from UI import * 
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui,QtWidgets
from cv2 import cv2 as cv
from math import sqrt
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
        self.smoothingFilters = [np.array([(1,1,1),(1,1,1),(1,1,1)]) * (1/9),
                        np.array([(1,2,1),(2,4,2),(1,2,1)]) * (1/16),
                        np.array([(0,0,0),(0,0,0),(0,0,0)]) ]
        self.edgeDetectionFilters = [np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]),
                                    np.array([[1, 0],[ 0, -1]]),
                                    np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]) ]
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

        # filters
        self.filtersOptions.currentIndexChanged.connect(self.avgFilter)
        self.edgeDetectionOptions.currentIndexChanged.connect(self.edgFilters)
        self.frequancyFiltersOptions.currentIndexChanged.connect(self.freqFilters)
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
    # avg filters
    def avgFilter(self,value):
        '''
        get the filter index choosen from the Filtered Image ComboBox and apply
        that filter on the noiseImageData 
        '''
        avgPic = self.noiseImageData.copy()
        picShape = self.noiseImageData.shape
        filterShape = self.smoothingFilters[value].shape

        inputPicRow = picShape[0] + filterShape[0] - 1
        inputPicColumn = picShape[1] + filterShape[1] - 1
        zeros = np.zeros((inputPicRow,inputPicColumn))

        for i in range(picShape[0]):
            for j in range(picShape[1]):
                zeros[i+np.int((filterShape[0]-1)/2),j+np.int((filterShape[1]-1)/2)] = avgPic[i,j]
        if(value == 2):
            for i in range(picShape[0]):
                for j in range(picShape[1]):
                    targetWindow = zeros[i:i+filterShape[0],j:j+filterShape[1]]
                    result = np.median(targetWindow)
                    avgPic[i,j] = result
        else:
            for i in range(picShape[0]):
                for j in range(picShape[1]):
                    targetWindow = zeros[i:i+filterShape[0],j:j+filterShape[1]]
                    result = np.sum(targetWindow*self.smoothingFilters[value])
                    avgPic[i,j] = result
        self.filteredImage.setImage(avgPic.T)
    

    def edgFilters(self,value):
        '''
        get the filter index choosen from the Image Edges ComboBox and apply
        that filter on the noiseImageData 
        '''
        pic = self.noiseImageData.copy()
        maskVertical =  self.edgeDetectionFilters[value]
        maskHorizontal = maskVertical.T
        picShape = self.noiseImageData.shape
        filterShape = maskVertical.shape


        inputPicRow = picShape[0] + filterShape[0] - 1
        inputPicColumn = picShape[1] + filterShape[1] - 1
        zeros = np.zeros((inputPicRow,inputPicColumn))

        for i in range(picShape[0]):
            for j in range(picShape[1]):
                zeros[i+np.int((filterShape[0]-1)/2),j+np.int((filterShape[1]-1)/2)] = pic[i,j]

        for i in range(picShape[0]):
            for j in range(picShape[1]):
                targetWindow = zeros[i:i+filterShape[0],j:j+filterShape[1]]

                verticalResult = (targetWindow*maskVertical)
                verticalScore = verticalResult.sum() / 4

                horizontalResult = (targetWindow*maskHorizontal)
                horizontalScore = horizontalResult.sum() / 4

                result = (verticalScore**2 + horizontalScore**2)**.5
                pic[i,j] = result*3
        self.edgeDetectionImage.setImage(pic.T)
    def freqFilters(self,value):
        '''
        get the filter index choosen from the Frequency Filters ComboBox and apply
        that filter on the noiseImageData 
        '''
        original = np.fft.fft2(self.noiseImageData)
        center = np.fft.fftshift(original)
        if(value == 0):
            resault = center * self.idealFilterLP(50,self.noiseImageData.shape)
        else:
            resault = center * self.idealFilterHP(50,self.noiseImageData.shape)
        LowPass = np.fft.ifftshift(resault)
        inverse_LowPass = np.fft.ifft2(LowPass)
        self.freqeuncyFilteredImage.setImage(np.abs(inverse_LowPass).T)

    def distance(self,point1,point2):
        return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

    def idealFilterHP(self,D0,imgShape):
        base = np.ones(imgShape[:2])
        rows, cols = imgShape[:2]
        center = (rows/2,cols/2)
        for x in range(cols):
            for y in range(rows):
                if self.distance((y,x),center) < D0:
                    base[y,x] = 0
        return base
    def idealFilterLP(self,D0,imgShape):
        base = np.zeros(imgShape[:2])
        rows, cols = imgShape[:2]
        center = (rows/2,cols/2)
        for x in range(cols):
            for y in range(rows):
                if self.distance((y,x),center) < D0:
                    base[y,x] = 1
        return base
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
        # def hybrid_img(img1, img2):
        #     # convert image 1
        #     # convert image 2
        #     # hybrid = low_img1 + high_img2
        #     # return hybrid
######################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  