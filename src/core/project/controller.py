# -*- coding: utf-8 -*-

_KNN = ''
_cameras = []
_status_spots = []
_id_camera_active = 0;

def setKnnInstance(knn):
    global _KNN
    _KNN = knn


def addCamera(camera):
  global _id_camera_active, _cameras
  from .ready_video import readVideo
  import threading


  _cameras.append(camera)
  _id_camera_active = camera.camId

  # Cria Thread
  readVideoThread = threading.Thread(target=readVideo, name="ThreadCamera",args=(camera.urlCam,))
  try:
    print("Start Thread Read Video (NAME: ReadCamThread)")
    readVideoThread.start()
  except:
    return False

  if(readVideoThread.isAlive()):
    return True


def processImage(frame):
  from .lbp import Lbp
  from .helper import findCameraObject
  from .cutImg import getTheSpots
  global  _status_spots, _cameras, _id_camera_active

  print("ProcessImage with a frame from video.")

  img_gray = Lbp.processImageCv(frame)
  index, camera = findCameraObject(_cameras, _id_camera_active)
  images = getTheSpots(camera, img_gray)
  hists = Lbp.lbp(images)

  statusSpots = []

  for vaga in hists:
    value = _KNN.predict(vaga.hist.reshape(1, -1))
    statusSpots.append({"id": vaga.id, "statusSpot": value[0] })

  _status_spots = statusSpots

  print(_status_spots)


def valueRequest():
  global  _status_spots
  return _status_spots






