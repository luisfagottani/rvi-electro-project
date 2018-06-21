from concurrent import futures
import time
import grpc
from .protos import api_pb2_grpc, api_pb2
from .controller import *

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class Service(api_pb2_grpc.ParkingServicer):

  def LoadCamera(self, request, context):
    try:
      response = firstLoad(request)
    except ValueError:
      print("Erro ao cadastrar a primeira camera no sdistema")
      response = False

    return api_pb2.LoadCameraReply(response=response)



def server():
  print("Step 06: Iniciando modulos (API) do sistema.....")
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  api_pb2_grpc.add_ParkingServicer_to_server(Service(), server)
  server.add_insecure_port('[::]:50050')
  server.start()
  print("Sistema pronto.")
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)
