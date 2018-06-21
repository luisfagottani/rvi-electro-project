import cv2
import numpy as np
from skimage.feature import local_binary_pattern


class Lbp:

  def processImageCv(imgPath):
    image = cv2.imread(imgPath)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  def lbp(im_gray):
      radius = 1
      no_points = 8

      # Uniform LBP is used
      lbp = local_binary_pattern(im_gray, no_points, radius, method='nri_uniform')
      hist,bins = np.histogram(lbp.ravel(),59,[0,59], density=True)
      return hist



