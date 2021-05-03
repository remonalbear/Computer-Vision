import numpy as np
from scipy import signal as sig
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.feature import corner_peaks
from skimage.io import imread
from skimage.color import rgb2gray

filename = 'box.jpg'

srcImg = imread(filename)

grayImg = rgb2gray(srcImg)

def gradient_x(grayImg):
    ##Sobel operator kernels.
    kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    return sig.convolve2d(grayImg, kernel_x, mode='same')
def gradient_y(grayImg):
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    return sig.convolve2d(grayImg, kernel_y, mode='same')

Ix = gradient_x(grayImg)
Iy = gradient_y(grayImg)

Ixx = ndi.gaussian_filter(Ix**2, sigma=1)
Ixy = ndi.gaussian_filter(Iy*Ix, sigma=1)
Iyy = ndi.gaussian_filter(Iy**2, sigma=1)


k = 0.05

# determinant
detA = Ixx * Iyy - Ixy ** 2
# trace
traceA = Ixx + Iyy
    
R = detA - k * traceA ** 2


# corners = corner_peaks(R,threshold_abs=3)
srcImg[R>0.01*R.max()]=[255,0,0]
fig, ax = plt.subplots()
ax.imshow(srcImg, interpolation='nearest', cmap=plt.cm.gray)
plt.show()