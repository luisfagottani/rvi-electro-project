# -*- coding: utf-8 -*-
from InitSystem import initiateSystem
from project.api import server
from project.controller import setKnnInstance
_KNN = ''

class main(object):

  def start(self):
    global _KNN
    # Initiate KNN
    _KNN = initiateSystem()
    setKnnInstance(_KNN)
    server()


if __name__ == "__main__":
  main().start()