# Coded by Michael Sawyer, V 1.0 6-24-17
# Released under GPL license, please include credit to original author.



#!/usr/bin/python

import os
import glob
import time


#Temp Probe Config, and process input.

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   
   while lines[0].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      temp_f = temp_c * 9.0 / 5.0 + 32.0
      return temp_c
rawtemp = read_temp()
temp = abs(rawtemp)

#PH Sensor Reading, and Calculations
phdata = os.popen('i2cget -y 1 0x48').read()
APH = float.fromhex(phdata)
PH1 = (abs(APH) * 0.15) - 8

#Temperature correction calculations

phDifference = PH1 - 7
tempDifferenceC = temp - 25
phAdjust = float((0.03*phDifference)*(tempDifferenceC/10))

if PH1 > 7 and temp < 25:
   phAdjust = phAdjust

if PH1 > 7 and temp > 25:
   phAdjust = phAdjust*-1

if PH1 < 7 and temp > 25:
   phAdjust = phAdjust

if PH1 < 7 and temp < 25:
   phAdjust = phAdjust* - 1

#output final calculations

tempAdjustedPH = float(PH1 + phAdjust)
print("Adjusted PH Meter output after temp correction: ", tempAdjustedPH)
print("Thermo Reading: ", temp)
#Resources and code grabbed from all over the internet, included are all the websites I can remember
#https://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi
