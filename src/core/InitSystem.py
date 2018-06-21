# -*- coding: utf-8 -*-
import json
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Global Vars
_CONFIG_VAR = ''

# Initate Project
def configs():
  print("STEP 01: Loading configs.....")
  global _CONFIG_VAR

  try:
    with open('static/config.json') as f:
      _CONFIG_VAR = json.load(f)
  except ValueError:
    print("Erro ao carregar as configurações!!")
    return False


def testDataSet():
  print("STEP 03: Carregando o dataset para treinamento.....")
  df = pd.read_csv('static/' + _CONFIG_VAR['CLASSIFIER']['TRAINING_DATA_SET'], delimiter=';', header=None, names=_CONFIG_VAR['CLASSIFIER']['PANDA_NAMES'])
  featureVector = np.array(df.ix[:, 0:59])
  classVector = np.array(df['class'])
  return featureVector, classVector

def knn():
  print("STEP 02: Iniciando o KNeighborsClassifier.....")
  knn = KNeighborsClassifier(n_neighbors=_CONFIG_VAR['CLASSIFIER']['KNN_NEIGHBORS'])
  feature, featureClass = testDataSet()
  print("STEP 04: Iniciando treinamento.....")
  knn.fit(feature, featureClass)
  print("STEP 05: KNeighborsClassifier treinado e pronto.")
  return knn


def initiateSystem():
  print("Initiating BackService.....")
  configs()

  try:
    return knn()
  except ValueError:
    print("Erro ao iniciar o KNN")
    return False
