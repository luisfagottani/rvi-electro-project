from concurrent import futures
import time
import grpc
from .protos import api_pb2_grpc, api_pb2


_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class Service(api_pb2_grpc.ParkingServicer):

  def addCamera(self, request, context):
    from .controller import addCamera
    response = addCamera(request)
    return api_pb2.addCameraReply(response=response)

  def ReturnSpots(self, request, context):
    from .controller import valueRequest
    try:
      response = valueRequest()
    except ValueError:
      print("Erro ao cadastrar a primeira camera no dasdsas")
      response = False

    return api_pb2.StatusSpotsResponse(spots=response)



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

