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
 
EquipmentDemand = pd.read_csv(data_path + '/EquipmentOutput.csv', index_col=0) 
print('Loading data is done!')

start_time = time.time()

# =============================================================================
# *** User defined inputs ***

Boiler = {'Efficiency': 0.8, 'Type' : 'Gas' }
# =============================================================================


# *** Defining the calculation Function ***
 
def BoilerInput(row , Boiler ):
    
    BoilerEfficiency = Boiler['Efficiency']
    
    return  row['EquipmentOutput'] * BoilerEfficiency
      
# =============================================================================
# =============================================================================
# ***How to call this function *** 


BoilerConsumption = pd.DataFrame(columns=['BoilerInput'])

BoilerConsumption['BoilerInput'] = EquipmentDemand.apply(BoilerInput, axis = 1 , Boiler = Boiler)

BoilerAnnualConsumption = BoilerConsumption.sum(axis=0)

BoilerAnnualThemrs = BoilerAnnualConsumption/1000

# =============================================================================
# =============================================================================

#Confirmations 
print('Calculation data is done!')
       

print("--- %s seconds --" % (time.time() - start_time))
  
##############################################################################

