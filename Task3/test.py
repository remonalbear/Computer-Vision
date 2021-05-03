import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
face = cv2.imread("lena.jpg")
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
# main_image = [1, 2, 3]
# result = np.correlate(main_image, main_image, mode='same')7
# result = signal.correlate2d(main_image, main_image, mode='same')

# print(result)

template = np.copy(face[150:250, 200:300])  # right eye
template = template - template.mean()
corr = signal.correlate2d(face, template, boundary='symm', mode='same')
(y, x) = np.unravel_index(np.argmax(corr), corr.shape)  # find the match

fig, (ax_orig, ax_template, ax_corr) = plt.subplots(3, 1,
                                                    figsize=(6, 15))
ax_orig.imshow(face)
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_template.imshow(template)
ax_template.set_title('Template')
ax_template.set_axis_off()
ax_corr.imshow(corr)
ax_corr.set_title('Cross-correlation')
ax_corr.set_axis_off()
ax_orig.plot(x, y, 'ro')
print("hello")
plt.show()