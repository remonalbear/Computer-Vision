from UI import *
from PyQt5 import QtCore, QtGui,QtWidgets
import numpy as np
from scipy import signal as sig
from scipy import ndimage as ndi
from skimage.io import imread
from skimage.color import rgb2gray
import cv2 as cv2

class GUI(Ui_MainWindow):
    def __init__(self,MainWindow):
        super(GUI,self).setupUi(MainWindow)
        
        filename = 'lena.jpg'
        srcImg1 = cv2.imread(filename, cv2.COLOR_BGR2RGB)
        grayImg1 = rgb2gray(srcImg1)
        features1 = self.harris(grayImg1)
        result_image = srcImg1

        srcImg2 = cv2.imread("lena_temp.jpg", cv2.COLOR_BGR2RGB)
        grayImg2 = rgb2gray(srcImg2)
        features2 = self.harris(grayImg2)
        result_image2 = srcImg2

        for match in features1:
            result_image = cv2.circle(result_image, (match[1], match[0]), radius=0, color=(0, 0, 255), thickness=-1)
        for match in features2:
            result_image2 = cv2.circle(result_image2, (match[1], match[0]), radius=0, color=(0, 0, 255), thickness=-1)
        imageName = 'result.jpg'   
        cv2.imwrite(imageName, result_image)
        cv2.imwrite('reult2.jpg', result_image2)
        self.label.setPixmap(QtGui.QPixmap(imageName))
        self.label_2.setPixmap(QtGui.QPixmap('reult2.jpg'))
    def gradient_x(self,grayImg):
        ##Sobel operator kernels.
        kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
        return sig.convolve2d(grayImg, kernel_x, mode='same')


    def gradient_y(self,grayImg):
        kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        return sig.convolve2d(grayImg, kernel_y, mode='same')


    def harris(self,grayImg):
        Ix = self.gradient_x(grayImg)
        Iy = self.gradient_y(grayImg)

        Ixx = ndi.gaussian_filter(Ix**2, sigma=1)
        Ixy = ndi.gaussian_filter(Iy*Ix, sigma=1)
        Iyy = ndi.gaussian_filter(Iy**2, sigma=1)

        k = 0.05

        # determinant
        detA = Ixx * Iyy - Ixy ** 2
        # trace
        traceA = Ixx + Iyy
            
        R = detA - k * traceA ** 2

        zeroArray = np.zeros((grayImg.shape[0],grayImg.shape[1]))
        zeroArray[R>0.001*R.max()] = True
        x = np.where(zeroArray == True)
        features =np.asarray(x).T.tolist()

        return features





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  