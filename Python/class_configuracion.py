from class_humedad_temperatura_aire import Humedad_Temperatura
from class_humedad_tierra import Humedad_Tierra
from class_conexion_api import Conexion_api

import RPi.GPIO as GPIO
import time
import pymongo
import random
import json

#Objetos
miSensorTemperatura = Humedad_Temperatura()
miSensorTemperaturaTierra = Humedad_Tierra()

class Configuracion(object):
    
    def __init__(self):
        self.tempEstablecida = 20 #hablando de grados centigrados
        self.humEstablecida = 70 #hablando de porcentaje de humedad
        self.tempActual = 0
        self.estadoClima = "" #SI = refrigero, NO calentó
        self.estadoBomba = "" #SI = bombeo, No nada
        self.humedadActual = 0
        self.GPIOTemperatura = 4
        self.diccionario={}
    
    def ActivarRegado(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)#pin, no gpio
        
        GPIO.output(11, True)
        print("Iniciando regado...")
        time.sleep(6)
        GPIO.output(11, False)
        time.sleep(0)
        
    def ActivarAire(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.OUT)#pin, no gpio
        
        GPIO.output(22, False)
        print("Activando aire...")
        time.sleep(5)
        GPIO.output(22, True)
        time.sleep(0)

    def IniciarSensores(self):
        miSensorTemperatura.SetPin(self.GPIOTemperatura)

    def SetTemperaturaActual(self):
        self.tempActual = miSensorTemperatura.ConfigurarSensor()
        
        try:
            self.tempActual = int(self.tempActual)
            return self.tempActual
        
        
        except:
            print("")


    def GetTemperaturaActual(self):
        return self.tempActual

    def SetHumedadActual(self):
        self.humedadActual = miSensorTemperaturaTierra.ConfigurarSensor()
        
        try:
            self.humedadActual = int(self.humedadActual)
            return self.humedadActual()
        except:
            print("")
          

    def GetHumedadActual(self):
        return self.humedadActual

    def ControlTemperaturaActual(self):
        print("Temp. Establecida: ",self.tempEstablecida)
        print("Temp. Actual: ",self.tempActual)
        
        if self.GetTemperaturaActual() > self.tempEstablecida:
            self.estadoClima = "SI"
            self.ActivarAire()
            print("Aire frio 40 segundos")
        elif self.GetTemperaturaActual() < self.tempEstablecida:
            self.estadoClima = "NO"
            print("Sin aire")
        
    def GetEstadoClima(self):
      return self.estadoClima


    def ControlHumedadActual(self):
        if self.GetHumedadActual() > self.humEstablecida:
            self.estadoBomba = "NO"
        elif self.GetHumedadActual() < self.humEstablecida:
            self.estadoBomba = "SI"
            print("Hum. Establecida: ",self.humEstablecida)
            print("Hum. Actual: ",self.humedadActual)
            self.ActivarRegado()

    def GetEstadoBomba(self):
      return self.estadoBomba
                
    def GenerarDiccionario(self):
        self.diccionario = {"User_ID":random.randrange(50),"Temperatura":self.GetTemperaturaActual(),"Humedad":self.GetHumedadActual(), "Clima":self.GetEstadoClima(), "Bomba de agua":self.GetEstadoBomba()}
        print(self.diccionario)
        
        
    def GetDiccionario(self):
        return self.diccionario
    
    
    def ConexionMongoLocal(self, x):
        miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
        midb = miCliente["invernadero"]
        col = midb["sensores"]
        x = col.insert_one(x)
        
        print("Datos agregados")
        
    
    def ConexionMongoCluster(self, x):
        client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.tvjyg.mongodb.net/invernadero?retryWrites=true&w=majority")
        db = client.invernadero
        sensores = db.sensores
        sensores.insert_one(x)

        print("Datos agregados")
            
    def AccionarMySQL(self):
        miApi = Conexion_api()

        data = miApi.GetUsuario()

        miApi.Post(self.GetTemperaturaActual(), self.GetHumedadActual(), self.GetEstadoClima(), self.GetEstadoBomba())
        print("Post enviado")