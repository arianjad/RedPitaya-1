#! /usr/bin/python

import sys
import time
import redpitaya_scpi as scpi
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
# redpitaya_scpi.py is used to connect to the SCPI server

def gaussian(x,a,b,n):
	return n*np.exp(-(x-b)**2/(2*a))
# intialize fit function

ip = '169.254.174.98'
# Get IP by typing arp -a in cmd line and looking for RP MAC address 
# Can also include ip as an argument when calling this script, use sys.argv

rp = scpi.scpi(ip)
# Initialize connection

rp.tx_txt('ACQ:RST')
# Reset acquisition parameters

decimation = 8
buff_time_ms = decimation * 131.072 * 10**-3
rp.tx_txt('ACQ:DEC '+str(decimation))
rp.tx_txt('ACQ:DEC?')
print('Decimation factor is '+rp.rx_txt())
print('Buffer length is ' +str(buff_time_ms) + ' ms')
# Set decimation, {1,8,64,1024,8192,65536}

avg = 'ON'
rp.tx_txt('ACQ:AVG '+ str(avg))
rp.tx_txt('ACQ:AVG?')
print('Averaging is '+rp.rx_txt())
# Set averaging

rp.tx_txt('ACQ:TRIG:DLY 0')
rp.tx_txt('ACQ:TRIG:DLY?')
print('Trig delay is '+ rp.rx_txt() + ' samples')
# Set trigger delay in samples (ie where does trigger occur in 16k sample buffer)

rp.tx_txt('ACQ:TRIG:LEV 50')
rp.tx_txt('ACQ:TRIG:LEV?')
print('Trig level is '+rp.rx_txt() +' mV')
# Set trigger level in mV

rp.tx_txt('ACQ:SOUR1:GAIN LV')
print('Gain setting is LV')
# Set gain mode (HV = 20V, LV = 1V)

rp.tx_txt('ACQ:DATA:UNITS VOLTS')
rp.tx_txt('ACQ:DATA:FORMAT FLOAT')
rp.tx_txt('ACQ:BUF:SIZE?')
buff_size = int(rp.rx_txt())
xdata = np.linspace(0,buff_time_ms,buff_size)
# Set data settings, prepare xdata for plotting/fitting

rp.tx_txt('ACQ:START')
time.sleep(0.5)
# Need to wait for buffer to fill up first

rp.tx_txt('ACQ:TRIG CH1_PE')
# Set trigger source. Must be set after ACQ:START

timeout = 10
# set timeout for trigger

trials = 10

for i in range(0,trials):
	start_acq = time.time()
	while 1:
		rp.tx_txt('ACQ:TRIG:STAT?')
		trig_time = time.time()
		elapsed = trig_time - start_acq
		if rp.rx_txt() == 'TD':
			status = 'Triggered'
			print(status)
			break
		elif elapsed > timeout:
			print('Trigger timed out')
			break

	if status == "Triggered":
		start_data = time.time()
		rp.tx_txt('ACQ:SOUR1:DATA?')
		buff_string = rp.rx_txt()
		buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
		buff = np.fromiter(buff_string,float, buff_size)
		# alternative: np.array(list(map(float,buff_string)))
		# or can try np.fromiter(map(float,buff_string))
		
		popt, pcov = curve_fit(gaussian, xdata, buff)
		end_data = time.time()
		print('Mean is '+str(popt[2]))
		print('Variance is '+str(popt[1]))
		print('Fit took ' + str(end_data - start_data) + ' sec')
		print('Acquisition and fit took ' + str(end_data - start_acq) + ' sec')



