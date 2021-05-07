import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt




face1 = cv2.imread("lena.jpg")
face2 = face1[150:250, 200:300]
# face2 = cv2.imread("lena_temp.jpg")
# face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
gray1 = cv2.cvtColor(face1, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(face2, cv2.COLOR_RGB2GRAY)

sift = cv2.SIFT_create()
orb = cv2.ORB_create()
kp1, des1 = sift.detectAndCompute(gray1,None)
kp2, des2 = sift.detectAndCompute(gray2, None)

matches1 = []
matches2 = []
# for idx, ele2  in enumerate(des2):
#     points_dis = []
#     for ele1 in des1:
#         diff = ele1-ele2
#         ssd = np.sum(np.square(diff))
#         points_dis.append(ssd)
#     # index = np.unravel_index(np.argmin(points_dis), len(points_dis))
#     index = points_dis.index(min(points_dis))
#     matches1.append(kp1[index])
#     matches2.append(kp2[idx])
    
for idx, ele2  in enumerate(des2):
    points_dis = []
    for ele1 in des1:
        nnc = np.mean(np.multiply((ele1-np.mean(ele1)),(ele2-np.mean(ele2))))/(np.std(ele1)*np.std(ele2))
        points_dis.append(nnc)
    # index = np.unravel_index(np.argmin(points_dis), len(points_dis))
    index = points_dis.index(max(points_dis))
    matches1.append(kp1[index])
    matches2.append(kp2[idx])



# print(type(des2))
# print(len(des2))
# print(len(des2[0]))

# print(kp)
img=cv2.drawKeypoints(gray1,matches1,face1)
cv2.imwrite('result11.jpg',img)
img2=cv2.drawKeypoints(gray2,matches2,face2)
cv2.imwrite('result22.jpg',img2)


# bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

# Match descriptors.
# matches = bf.match(des1, des2)
# print(type(matches[0]))
# matches = bf.knnMatch(des1,des2, k=2)
# Sort them in the order of their distance.

# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])

# print(good)
# matches = sorted(matches, key=lambda x: x.distance)
# print(good[0].distance)
# Draw first 10 matches.
# img3 = cv2.drawMatches(face1, kp1, face2, kp2, matches[:25],None, flags=2)
# cv2.imshow("result", img3)
# cv2.waitKey(0)