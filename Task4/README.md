# Computer Vision Course - Group Task #4

---

# Team Work:

| Name | Section | Bench |
| ----------- | ----------- | ----------- |
| Ahmed Adel | 1 | 6 |
| Remon Albear | 1 | 33 |
| Abdulla Zahran | 2 | 4 |
| Mohammed Almotasem | 2 | 19 |

---

# Table of Content

| Requiered Part | Title |
| ----------- | ----------- |
| [#Part 1](#part-1) | Image Thresholding |
| [#Part 2](#part-2) | Image Segmentation |


---

# Part 1



## Image Segmentation

Image thresholding is mainly used to detect the edges found in a given picture, through choosing a suitable threshold; then applyingthis threshold and dividing the picture into two clusters: pixels with values than the the threshold which are set to 255 and others less than it which are set to 0.
Apllying the theshold can be done using mainly two methods: Global or Local thresholding.
But choosing the value of the threshold is the real trick and can be done by different techniques that will be displayed as follows on our "lena" image sample.
![Lena](screenshots/lena.PNG)
### 1. Optimal threshold
The optimal thresholding is done using by suing the means of the image and calculating the threshold using iteration to set pur two main reigons.
#### Global threshold
![Optmial_Global](screenshots/optimal_global.PNG)
#### Local threshold
![Optimal_Local](screenshots/optimal_local.PNG)
### 2. Otsu threshold
The Otsu algorithm is mainly based on select the threshold by calculating the between class variance for every value in the histogram and selecting the threshold based on the value that acheived the higher between class variance.
#### Global threshold
![Otsu_Global](screenshots/otsu_global.PNG)
#### Local threshold
![Otsu_Localal](screenshots/otsu_local.PNG)
### 3. Spectral threshold
The spectral algorithm is acheieved by applying on e of the previous algorithm but using the three or more modes ie. Generalizing mode and calculating two or more thresholds and applying the thresholds to the selected image.
#### Global threshold
![Spectral_Global](screenshots/spectral_global.PNG)
#### Local threshold
![Spectral_Local](screenshots/spectral_local.PNG)


---


# Part 2 

## Image Thresholding
### Mean shift segementation


* 
![mean shift result 1](screenshots/mean_seg_res1.JPG)

* 
![mean shift result 2](screenshots/mean_seg_res3.JPG)

* 
![mean shift result 2](screenshots/mean_seg_res2.JPG)


## Main Program working
![Program 1](screenshots/P1.PNG)