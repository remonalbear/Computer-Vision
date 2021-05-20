import numpy as np
import cv2 
import math

def spectral_threshold(image):
    blur = cv2.GaussianBlur(image,(5,5),0)
    hist = cv2.calcHist([image],[0],None,[256],[0,256]) 
    hist /= float(np.sum(hist)) 
    BetweenClassVarsList = []
    for bar, _ in enumerate(hist):
        Foregroundlevels = []
        BackgroundLevels = []
        ForegroundHist = []
        BackgroundHist = []
        for level, value in enumerate(hist):
            if level < bar:
                BackgroundLevels.append(level)
                BackgroundHist.append(value)
            else:
                Foregroundlevels.append(level)
                ForegroundHist.append(value)
        
        FWeights = np.sum(ForegroundHist) / float(np.sum(hist))
        BWeights = np.sum(BackgroundHist) / float(np.sum(hist))
        FMean = np.sum(np.multiply(ForegroundHist, Foregroundlevels)) / float(np.sum(ForegroundHist))
        BMean = np.sum(np.multiply(BackgroundHist, BackgroundLevels)) / float(np.sum(BackgroundHist))
        BetClsVar = FWeights * BWeights * np.square(BMean - FMean)
        BetweenClassVarsList.append(BetClsVar)
    thresh1 = np.nanmax(BetweenClassVarsList)
    idx2 = BetweenClassVarsList.index(thresh1)
    BetweenClassVarsList = np.nan_to_num(BetweenClassVarsList)
    idx = -1
    thresh2 = BetweenClassVarsList[0]
    for index, value in enumerate(BetweenClassVarsList):
        if value > thresh2:
            if value == thresh1:
                thresh2 = value
                idx = index
    return (idx, idx2)







