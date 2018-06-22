import cv2
import numpy as np
from skimage.feature import local_binary_pattern


class Lbp:

  def processImageCv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  def lbp(mapImgs):
    from .helper import ObjectCreator
    radius = 1
    no_points = 8
    hists = []

    for mapImg in mapImgs:
      lbp = local_binary_pattern(mapImg.image, no_points, radius, method='nri_uniform')
      hist,bins = np.histogram(lbp.ravel(),59,[0,59], density=True)

      object = ObjectCreator()
      object.id = mapImg.id
      object.hist = hist

      hists.append(object)

    return hists



