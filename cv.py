import cv2
from scipy import ndimage

#BGR
low_orange = (140, 60, 0)
high_orange = (255, 150, 120)

def getXY(img):
  mask = cv2.inRange(img, low_orange, high_orange)
  # return the average x and y values of the baby
  return ndimage.measurements.center_of_mass(mask)[0], mask
