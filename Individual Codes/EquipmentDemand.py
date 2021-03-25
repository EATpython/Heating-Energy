# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:38:59 2020

@author: Taraneh
"""

#=============================================================================

# Importing all the required libraries
import pandas as pd
import warnings
import time

warnings.simplefilter('ignore')

print('Importing Libraries and Packages is done!')

# =============================================================================

# *** Loading the Data ***

data_path = 'C:/Users/Taraneh/Desktop/Python/Sample Data'
 
LoadProfile = pd.read_csv(data_path + '/Boiler Demand Data.CSV', index_col=0) 
print('Loading data is done!')

start_time = time.time()

# =============================================================================
# *** User defined inputs ***

Equipment = {'Quantity': 1, 'Size' : 200, 'Turndown' : 0.05 }
#Todo : Unmet hours count , so you can after 10 of unmet hours run at turn doen 1 time 
# =============================================================================


# *** Defining the calculation Function ***
 
def EquipmentDemand(row , Equipment ):
#def BoilerDemand(row , BoilerQuantity = Boiler['Quantity'], BoilerMax = Boiler['Size'] , BoilerTD = Boiler['Turndown']):
    
    EquipQuantity = Equipment['Quantity']
    EquipMax = Equipment['Size'] 
    EquipTD = Equipment['Turndown']
    if row['HWLoad'] > EquipMax * EquipTD  : 
        BoilerOut = min ( row['HWLoad'] , EquipMax * EquipQuantity )
    else:
        BoilerOut = 0 
    
        #print(unmethr)
    #return pd.Series([BoilerOut, unmethr], index = ["boilerout" , "Unmet"])
    return BoilerOut

# =============================================================================
# =============================================================================
# ***How to call this function *** 

# =============================================================================
# ***defining the data frames ***

# temporary input data fram 
Load_Temp = abs(pd.DataFrame ( data = LoadProfile['HWLoad']))  #converting back to Data frame 

#output data fram 
EquipmentOutput = pd.DataFrame(columns=['BoilerOutput'])

# =============================================================================
#Function Call 

EquipmentOutput['EquipmentOutput'] = Load_Temp.apply(EquipmentDemand, axis = 1 , Equipment = Equipment)

# =============================================================================
# =============================================================================

#Confirmations 
print('Calculation data is done!')
       

print("--- %s seconds --" % (time.time() - start_time))
  
##############################################################################

