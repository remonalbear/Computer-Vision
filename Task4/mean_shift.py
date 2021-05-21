import cv2
from MEANSHIFT import meanShiftSeg

imagePath = "screenshots/seg3.png"

imageRGB = cv2.imread( imagePath )
cv2.imshow("input",imageRGB)
imageLUV = cv2.cvtColor( imageRGB, cv2.COLOR_RGB2LUV )

imageLUV2RGB = cv2.cvtColor( imageLUV, cv2.COLOR_LUV2RGB )


meanShift = meanShiftSeg( imageLUV, 7 )
segImage = meanShift.applyMeanShift()


cv2.imshow( 'image', segImage )



cv2.waitKey(0)
cv2.destroyAllWindows()