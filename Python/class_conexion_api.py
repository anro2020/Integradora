import requests
import json

class Conexion_api:

    data_registro = {}

    def GetUsuario(self):
        #Get
        response = requests.get("https://invernaderoeq5.herokuapp.com/user")
        return response.json()

    def Post(self, a, b, c, d):

        x = {
            'User_id':self.GetUsuario(),
            'Sensor_temperatura':a,
            'Sensor_humedad':b,
            'Enfrio':c,
            'Rego':d
            }

        print("POST: ",x)

        response = requests.post('https://invernaderoeq5.herokuapp.com/reporte', x)
