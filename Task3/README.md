# Computer Vision Course - Group Task #3

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
| [#Part 1](#part-1) | Harris Operator|
| [#Part 2](#part-2) | SIFT |
| [#Part 3](#part-3) | Features Matching |


---

# Part 1




---


# Part 2 

## Scale Invarient Features Transform (SIFT)
We ued the SIFT algorithm to create descriptors of the key points generated from the Harris operator
The SIST algorithm consist of two parts:
1. Calculate Key Point Oriantation
2. Generate the key points Descriptors
### Key Point Oriantation
Calculate the main oriantation of the key point to used it in the next step to compute the relative oriantaion of each point in the kernal.

Steps:
* take kernal 16 * 16 around the point 
* compute the magnitude and oriantation of the gradient of this kernal 
* multiply the magnitude by guassian filter 
* claculate the histogram of this kernal where each bin is 10 degrees 
* take the biggest bin of the histogram and assign it to the point
![Main oriantation](ScreenShots/oraintation.jpg)

![Main oriantation 2](ScreenShots/oraintation2.jpg)

### Key Point Descriptors
Steps:
* take 16 * 16 kernal 
* split it to 4 * 4 regions
* for each region we compute the magnitude and oriantation of the gradient 
* multiply the magnitude by guassian filter
* compute the histogram for each region where each bin is 45 degrees 
* we have 4 * 4 * 8 = 128 length descriptor  
![Main oriantation 2](ScreenShots/descriptors.png)


---

# Part 3





