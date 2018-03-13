import sys
import time
import redpitaya_scpi as scpi
# redpitaya_scpi.py is used to connect to the SCPI server

ip = '169.254.174.98'
# Get IP by typing arp -a in cmd line and looking for RP MAC address 
# Can also include ip as an argument when calling this script, use sys.argv

rp = scpi.scpi(ip)
# Initialize connection

decimation = 1 #{1,8,64,1024,8192,65536}
rp.tx_txt('ACQ:DEC '+str(decimation))
rp.tx_txt('ACQ:DEC?')
print('Decimation factor is '+rp.rx_txt())
avg = 'ON'
rp.tx_txt('ACQ:AVG '+ str(avg))
rp.tx_txt('ACQ:AVG?')
print('Averaging is '+rp.rx_txt())
rp.tx_txt('ACQ:TRIG CH1_PE')
rp.tx_txt('ACQ:TRIG:DLY 0')
rp.tx_txt('ACQ:TRIG:DLY?')
print('Trig delay is '+ rp.rx_txt() + ' samples')
rp.tx_txt('ACQ:SOUR1:GAIN LV')
print('Gain setting is LV')
rp.tx_txt('ACQ:TRIG:LEV 50') #mV
rp.tx_txt('ACQ:TRIG:LEV?')
print('Trig level is '+rp.rx_txt() +' mV')
