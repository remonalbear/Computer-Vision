from numpy.lib.type_check import imag
from spectral import spectral_threshold
import numpy as np
import cv2 
from otsu import otsu_threshold
from optimal import optimal_threshold
from spectral import spectral_threshold


def Global_threshold(image , thresh_typ = "Optimal"):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    if thresh_typ == "Otsu":
        threshold = otsu_threshold(image)
    elif thresh_typ == "Spectral":
        threshold = spectral_threshold(image)
    else:
        threshold = optimal_threshold(image)
    print(threshold)
    thresh_img = np.uint8(np.where(image > threshold, 255, 0))
    return thresh_img

def Local_threshold(image, block_size , thresh_typ = "Optimal"):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh_img = np.copy(image)
    for row in range(0, image.shape[0], block_size):
        for col in range(0, image.shape[1], block_size):
            mask = image[row:(row+block_size,image.shape[0]),col:min(col+block_size,image.shape[1])]
            thresh_img[row:(row+block_size,image.shape[0]),col:min(col+block_size,image.shape[1])] = Global_threshold(mask, thresh_typ)
    return thresh_img




source_image = cv2.imread("lena.jpg", 0)
optimal = Global_threshold(source_image, "Optimal")
otsu = Global_threshold(source_image, "Otsu")
spectral = Global_threshold(source_image, "Spectral")
# print(otsu)
cv2.imshow('Original image', source_image)
cv2.imshow('optimal thresholding', optimal)
cv2.imshow('otsu thresholding', otsu)
cv2.imshow('spectral thresholding', spectral)
cv2.waitKey(0)
cv2.destroyAllWindows()