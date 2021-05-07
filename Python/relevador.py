#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 02:56:59 2021

@author: pi
"""

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

'''
while True:
   GPIO.output(7, True)
   print("encendido")
   time.sleep(1)
   GPIO.output(7, False)
   print("apagado")
   time.sleep(1)'''
   
   
class Relevador:
    
    pin = 7
    
    def SetPin(self, num):
        self.pin = num
        
    def GetPin(self):
        return self.pin
    
    def ConfigurarSensor(self):
        '''GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)'''
        
        GPIO.output(self.GetPin(), True)
        print("Encendido")
        time.sleep(1)
        GPIO.output(self.GetPin(), False)
        print("Apagado")
        time.sleep(1)
        
        
            
reley = Relevador()

reley.SetPin(7)
reley.ConfigurarSensor()