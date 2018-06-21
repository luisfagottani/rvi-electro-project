# -*- coding: utf-8 -*-
from InitSystem import initiateSystem
from project import api
from project import controller
_KNN = ''

class main(object):

  def start(self):
    global _KNN
    # Initiate KNN
    _KNN = initiateSystem()
    controller.setKnnInstance(_KNN)
    api.server()



if __name__ == "__main__":
  main().start()