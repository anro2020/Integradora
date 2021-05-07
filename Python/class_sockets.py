from class_conexion_api import Conexion_api
from websocket import create_connection
from datetime import datetime
import json

miApi = Conexion_api()
miDateTime = datetime.now()
eldatetime = str(miDateTime)

class Websockets:
    
    id_user = miApi.GetUsuario()
    
    def myconverter():
        if isinstance(datetime.now):
            return __str__()
    
    def send_message(self):
        ws = create_connection("ws://invernanderointeligente.herokuapp.com/adonis-ws")
        ws.send(json.dumps({
        "t":1,
        "d":{
        "topic":"chat",
        "event":"message",
        "data":"putoss"
        }
        }))
        result = ws.recv()
        result = json.loads(result)
        ws.send(json.dumps({
        "t":7,
        "d":{
        "topic":"chat",
        "event":"message",
        "data": self.id_user
        }
        }))
        
        print("id_user:", self.id_user)
        print(miDateTime)
        
        ws.send(json.dumps({
        "t":7,
        "d":{
        "topic":"chat",
        "event":"message",
        "data": ("NUEVO BARRIDO: ", eldatetime)
        }
        }))
        print("Received '%s'")
        
misocket = Websockets()
misocket.send_message()
