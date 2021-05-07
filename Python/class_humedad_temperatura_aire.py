import RPi.GPIO as GPIO
from Librerias import dht11
import time
#from tiempo import tiempo as t

class Humedad_Temperatura:
    
    pin = 0 #Le ingreso el gpio 4 pin 7
    
    def SetPin(self, num):
        self.pin = num
        
    def GetPin(self):
        return self.pin
    
    def ConfigurarSensor(self):
        # initialize GPIO
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        

        # read data using pin 14
        #GPIO
        instance = dht11.DHT11(self.GetPin())
        #hora = t.capturar()
        try:
            result = instance.read()
            if result.is_valid():
                #print("Temperature: %-3.1f C" % result.temperature)
                #print("Humidity: %-3.1f %%" % result.humidity)
                
                return int(result.temperature)
            time.sleep(0.5)
            '''        
            while True:
                result = instance.read()
                if result.is_valid():
                    print("Temperature: %-3.1f C" % result.temperature)
                    print("Humidity: %-3.1f %%" % result.humidity)
                    
                    #result.temperature = temperatura
                    #result.humidity = humedad
                    #print(temperatura, humedad)
                    #return result.temperature, result.humidity,hora
                time.sleep(2)'''
            
        except KeyboardInterrupt:
            pass
        finally:
            #print("Cleanup")
            GPIO.cleanup()
            
#SensorTemperatura.capturar()
