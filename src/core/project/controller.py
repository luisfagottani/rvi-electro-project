# -*- coding: utf-8 -*-
import _thread
from .ready_video import *


_KNN = ''
_general = {}
_cameras = []

def setKnnInstance(knn):
    global _KNN
    _KNN = knn

def firstLoad(camera):

  _general['namePark'] = camera.namePark
  _general['pathData'] = camera.path

  auxObj = {}
  auxObj['camType'] = camera.camType
  auxObj['typeFile'] = camera.typeFile
  auxObj['urlCam'] = camera.urlCam
  auxObj['nameCam'] = camera.nameCam
  auxObj['spots'] = camera.spots

  _cameras.append(auxObj)
  teste = readVideo(_cameras[0]['urlCam']);
  print(teste)

  return True

def addCamera(camera):
  auxObj = {}
  auxObj.camType = camera.camType
  auxObj.typeFile = camera.typeFile
  auxObj.urlCam = camera.urlCam
  auxObj.nameCam = camera.nameCam
  auxObj.spots = camera.spots

  _cameras.append(auxObj)

  # def main(self):
  #   img_gray = Lbp.processImageCv('./project/images/11.png')
  #   hist = Lbp.lbp(img_gray)
  #   teste = _KNN.predict(hist.reshape(1, -1))



