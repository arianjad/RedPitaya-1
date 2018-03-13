#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def gaussian(x,a,b,n):
	return n*np.exp(-(x-b)**2/(2*a))

