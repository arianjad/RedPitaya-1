#! /usr/bin/python

import sys
import time
import redpitaya_scpi as scpi
# redpitaya_scpi.py is used to connect to the SCPI server

ip = '169.254.174.98'
# Get IP by typing arp -a in cmd line and looking for RP MAC address 
# Can also include ip as an argument when calling this script, use sys.argv

rp_s = scpi.scpi(ip)
# Initialize connection

def SetDecimation(dec,rp):
	rp.tx_txt('ACQ:DEC '+str(dec))

def StartAcquisition(rp):
	rp.tx_txt('ACQ:START')


class FastAnalogOutput:
	def __init__(self,sourceNum):
		self.source = str(sourceNum)
		self.waveform = 'SINE'
		self.freq = 1000
		self.ampl = 1
		self.state = 'OFF'
		self.offset = 0
		self.phase = 0
		self.duty = 50
		self.custom
		self.burst = 'OFF'
		self.count = 1
		self.time = 1
		self.trig = None

	def Enable(self):
	
	def Disable(self):

	def SetFreq(self, freq):

	def SetWave(self,waveform):

	def SetAmpl(self,ampl):

	def SetOffset(self,offset):

	def SetPhase(self,phase):

	def SetDuty(self,duty):

	def SetArbWave(self,array):

	def SetBurst(self,burst):

	def EnableBurst(self):

	def DisableBurst(self):

	def SetTrigger(self,trig):

	def ResetDefaults(self):


		

class FastAnalogInput():
	def __init__(self,sourcNum,RedPitaya):
		self.source = sourceNum
		self.rp = RedPitaya
		self.dec = 1
		self.avg = 'ON'
		self.trigSource = 'DISABLED'
		self.trigStatus
		self.trigTime =
		self.trigCounter = 
		self.trigGain = 
		self.trigLevel =
		self.dataUnits = 
		self.dataFormat = 



	def StartAcq(self):

	def StopAcq(self):

	def ResetAcq(self):

	def SetDec(self):

	def SetAvg(self):

	def EnableAvg(self):

	def DisableAvg(self):

	def GetDec(self):

	def GetAvg(self):

	def SetTrig(self):

	def TrigNow(self):

	def TrigState(self):

	def SetTrigDelay(self):

	def GetTrigDelay(self):

	def SetGain(self):

	def SetTrigLevel(self):

	def GetTrigLevel(self):

	def SetDataUnits(self):

	def SetDataFormat(self):

	def ReadData(self):

	def GetBuffSize(self):



def LedOn(led):
    rp_s.tx_txt('DIG:PIN LED' + str(led) + ',' + str(1))
    return
    
def LedOff(led):
    rp_s.tx_txt('DIG:PIN LED' + str(led) + ',' + str(0))
    return
# Define LED control functions
# Room for improvement: turn on multiple LEDs

def ConfigWaveForm(sourceNum,waveform):
	rp_s.tx_txt('SOUR'+str(sourceNum)+':'+'FUNC '+waveform.upper())
	print('Output ' + str(sourceNum)+' has been set to ' + waveform)
	return

def EnableOut(sourceNum):
	rp_s.tx_txt('OUTPUT' +str(sourceNum)+':STATE ON')
	print('Output ' + str(sourceNum)+' has been enabled')
	return

def DisableOut():
	rp_s.tx_txt('OUTPUT' +str(sourceNum)+':STATE OFF')
	print('Output ' + str(sourceNum)+' has been disabled')
	return

def ConfigFreq(sourceNum,)


def ConfigGenerator(sourceNum,waveform,freq,ampl,burst):
	source='SOUR'+sourceNum
	rp_s.tx_txt('GEN:RST')
	rp_s.tx_txt(FormatMessage(source,''))
