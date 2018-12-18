#!/usr/bin/env python
#
# Python Library for using the Grove - I2C Motor Driver
#
# Modifications December 2018 SwitchDoc Labs
#
# original file from DexterIndustries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GrovePi/blob/master/LICENSE

import time,sys
import RPi.GPIO as GPIO
import smbus


bus = smbus.SMBus(1)

class motor_driver:

	MotorSpeedSet             = 0x82
	PWMFrequenceSet           = 0x84
	DirectionSet              = 0xaa
	MotorSetA                 = 0xa1
	MotorSetB                 = 0xa5
	Nothing                   = 0x01
	EnableStepper             = 0x1a
	UnenableStepper           = 0x1b
	Stepernu                  = 0x1c
	I2CMotorDriverAdd         = 0x0f  #Set the address of the I2CMotorDriver

	def __init__(self,address=0x0f):
		self.I2CMotorDriverAdd=address

	#Maps speed from 0-100 to 0-255
	def map_vals(self,value, leftMin, leftMax, rightMin, rightMax):
		#http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
		# Figure out how 'wide' each range is
		leftSpan = leftMax - leftMin
		rightSpan = rightMax - rightMin

		# Convert the left range into a 0-1 range (float)
		valueScaled = float(value - leftMin) / float(leftSpan)

		# Convert the 0-1 range into a value in the right range.
		return int(rightMin + (valueScaled * rightSpan))

	#Set motor speed
	def MotorSpeedSetAB(self,MotorSpeedA,MotorSpeedB):
		MotorSpeedA=self.map_vals(MotorSpeedA,0,100,0,255)
		MotorSpeedB=self.map_vals(MotorSpeedB,0,100,0,255)
		bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.MotorSpeedSet, [MotorSpeedA,MotorSpeedB])
		time.sleep(.02)

	#Set motor direction
	def MotorDirectionSet(self,Direction):
		bus.write_i2c_block_data(self.I2CMotorDriverAdd, self.DirectionSet, [Direction,0])
		time.sleep(.02)
        
