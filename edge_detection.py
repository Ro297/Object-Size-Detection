import numpy as np
import cv2
import math
from matplotlib import pyplot as plt
from cv2 import threshold, drawContours


img = cv2.imread('./Images/test_image.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray,40,60)

plt.imshow(edges)
plt.show()