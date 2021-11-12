import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

#BGR
low_orange = (0, 90, 0)
high_orange = (50, 150, 255)

img = cv2.imread("/Users/michaelbryant/Desktop/pumpkin.jpeg")
width = img.shape[1]

mask = cv2.inRange(img, low_orange, high_orange)
masked_image = cv2.bitwise_and(img, img, mask=mask)

center = ndimage.measurements.center_of_mass(mask)[0]

plt.subplot(2, 2, 1)
plt.imshow(np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
plt.subplot(2, 2, 2)
plt.imshow(np.array(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)))
plt.subplot(2, 2, 3)
plt.imshow(np.array(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB)))

plt.subplot(2, 2, 4)
plt.plot((0, width), (center, center), color="red", linewidth=1)
plt.imshow(np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))

plt.show()
