# Computer Vision Course - Group Task #2

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
| [GUI](#part-0) | Graphical User Interface - GUI |
| [#Part 1](#part-1) | Active contour |
| [#Part 2](#part-2) | Filter the noisy image |
| [#Part 3](#part-3) | Detect edges in the image |
| [#Part 4](#part-4) | Draw histogram and distribution curve |
| [#Part 5](#part-5) | Equalize the image |
| [#Part 6](#part-6) | Normalize the image |
| [#Part 7](#part-7) | Local and global thresholding |
| [#Part 8](#part-8) | Transformation from color image to gray scale |
| [#Part 9](#part-9) | Frequency domain filters |
| [#Part 10](#part-10) | Hybrid images |

---

# Part 1

## Active contour

this is the original image that we want to detect the boundaries of it.

![GUI](ScreenShots/snakeImageInput.png)

Starting with initial guess for the boundary points, then shift the points around until they reach to the local minimum of the energy function.

![GUI](ScreenShots/snakeImageOutput.png)