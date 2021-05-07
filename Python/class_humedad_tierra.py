#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:59:24 2021

@author: pi
"""

import serial

class Humedad_Tierra:
    
    pin = "/dev/ttyACM0"
    
    #print(type(pin) is str)
    
    #def SetPin(self, num):
     #   self.pin = num
    
    #def GetPin(self):
     #   return self.pin
    
    def ConfigurarSensor(self):

#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
        ser = serial.Serial(self.pin,115200)
        ser.flushInput()
        
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        valor_sensor = int(line)
        #print(valor_sensor)
        return valor_sensor
        '''
        while True:
        
            try:
        
                lineBytes = ser.readline()
                line = lineBytes.decode('utf-8').strip()
                valor_sensor = int(line)
                #print(valor_sensor)
                return valor_sensor
        
            except KeyboardInterrupt:
                break'''
            
            
            
    #SetPin(str(input("Digite el pin a utilizar: ")))
'''miHTierra = Humedad_Tierra()
seri = "/dev/ttyACM0"
miHTierra.SetPin(seri)
miHTierra.ConfigurarSensor()'''
#self.pin.port = "COM{}".format(num-1)