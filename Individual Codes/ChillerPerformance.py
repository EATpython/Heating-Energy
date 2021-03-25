# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:24:31 2020

@author: Taraneh
"""

## This code is a test for curve fitting


# =============================================================================
# Import all the needed Librari
import numpy as np 
import pandas as pd
# curve-fit() function imported from scipy 
from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 
import time
# =============================================================================



# =============================================================================
# Here we define the chiller tons and kw s

tons = np.array([200,180,160,140,120,100,80,60,48])
kws = np.array([236.10,191.70,157.20,131.20,105.70,80.02,59.81,47.39,41.89])
n = 6
# =============================================================================

# =============================================================================
# Method 1 : Calculate the polynomial 
#to do : find the R for the fitted curve 

start_time_1 = time.time()

def ChillerKW (Load, tons = tons, kws = kws): 
    curve_coef = np.polyfit(tons,kws,n)
    chillerkw = np.poly1d(curve_coef)
    
    return chillerkw(Load)

df = pd.DataFrame([60,70,66])






print("--- %s seconds for calculation---" % (time.time() - start_time_1))

# =============================================================================
