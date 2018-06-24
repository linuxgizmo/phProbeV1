# Coded by Michael Sawyer, V 1.0 6-24-17
# Released under GPL license, please include credit to original author.



#!/usr/bin/python

import os
import time


#Temp Probe Config, and process input.

os.system('modprobe w1-gpio')
os.system('modprobe w1-them')

ph_temp_sensor='sys/bus/w1/devices/28-000005e2fdc3/w1_slave'

def temp_raw():
   f = open(ph_temp_sensor, 'r')
   lines = f.readlines()
   f.close()
   return lines
   
def read_temp():
   lines = temp_raw()
   while lines[0].strip()[-3]!='YES':
      time.sleep(0.2)
	  lines = (temp_raw)
   temp_output = lines[1].find('t=')
   if temp_output != -1:
      temp_string = lines[1].strip()[temp_output+2:]
	  temp_c = float(temp_string) / 1000.0
	  return temp_c


#PH Sensor Reading, and Calculations
PH1=os.popen('i2cget -y 1 0x48').read()
temp=os.pope)
PH2= float(PH1) * 5.0 / 1024
phfinal= 3.5 * PH2 
print("In PH thats:", phfinal)

#Temperature correction calculations

float phDifference = abs(PH1-7)
float tempDifferenceC = abs(temp-25)
float phAdjust = (0.03*phDifference)*(tempDifferenceC/10)

if (PH1>7 && temp<25)
   phAdjust=phAdjust
   
if (PH1>7 && temp>25)
   phAdjust=phAdjust*-1
   
if (PH1<7 && temp>25)
   phadjust=phadjust
   
if (PH1<7 && temp<25)
   phadjust=phadjust*-1
   
#output final calculations   
   
float tempAdjustedPH = PH + phAdjust
print(tempAdjustedPH)
   
   
#Resources and code grabbed from all over the internet, included are all the websites I can remember
#https://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi