#! /usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit
from redpitaya.overlay.mercury import as overlay
fpga = overlay() 

osc = [fpga.osc(0,1.0), fpga.osc(1,1.0)]	# Initialize scope inputs (0=IN1, 1=IN2) (1 = low voltage, 20 = high voltage)
gen = [fpga.gen(0), fpga.gen(1)]			# Initialize generator outputs (0=OUT1, 1=OUT2)

# Set oscilloscope settings. Decimation rate is 2^integer
def setScope(ch, sample_size,trig_post,trig)
	#ch: channel number, 0 or 1
	#sample_size: must be in miliseconds
	#trig_post: what fraction of buffer will be after trigger
	#sync: which channel is used for control
	#trig: which channel is used for trigger
	N = osc[ch].buffer_size
	osc[ch].decimation = 2^(math.ceil(math.log(sample_size/(16384*8**10^-6),2)))	#convert sample size to decimation parameter, always rounds up
	print('sample length is '+ str(osc[ch].decimation*16384*8**10^-6)+' ms')
	osc[ch].trig_pre = round(N * (1-trig_post))
	osc[ch].trig_post = round(N * trig_post)
	osc[ch].trig_src = fpga.trig_src['osc'+str(ch)]
	return




