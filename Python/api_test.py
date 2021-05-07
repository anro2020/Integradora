from class_conexion_api import Conexion_api
import json

#Objeto
miApi = Conexion_api()

data = miApi.GetUsuario()

miApi.Post(input("Sensor temperatura: "), input("Sensor Humedad: "), input("Frio: "), input("Calor: "))
print("Post enviado")


