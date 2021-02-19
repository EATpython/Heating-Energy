#Practice collaboration file


# Step 1 - Lets list all the libraries that needs to be imported
import pandas as pd
import numpy as np 
import warnings
import time
import matplotlib.pyplot as plt

# Step 2 - Lets Define all the User Inputs Required

# Step 3 - Lets Define all the variables that we will use with description


#################################################################################################################
# Step 4 - Lets Create all the functions 
## Input 
## Outputs 
#################################################################################################################


#################################################################################################################
# 4.a : User Propmt Input, save to 
## Input 
## Outputs 
#################################################################################################################



#################################################################################################################
# 4.b : Data Cleaning
## Input 
## Outputs 
#################################################################################################################



#################################################################################################################
# 4.c : Load Profile Generation
## Input 
## Outputs 
#howdy
#################################################################################################################


#################################################################################################################
# 4.d : EquipmentDemand Function
## Libraries : Pandas as pd 
## Input : LoadProfile, data_path, Equipment
## Outputs : EquipmentOutput 

data_path =  xxxxxxxxxx
LoadProfile = pd.read_csv(data_path + '/Load Profile.CSV', index_col=0) 
# =============================================================================
# *** User defined inputs ***

Equipment= {'Quantity': 1, 'Size' : 200, 'Turndown' : 0.05 }
# =============================================================================
#Todo : Unmet hours count , so you can after 10 of unmet hours run at turn doen 1 time 
# *** Defining the calculation Function ***
def EquipmentDemand(row , Equipment ):
    
    EquipQuantity = Equipment['Quantity']
    EquipMax = Equipment['Size'] 
    EquipTD = Equipment['Turndown']
    if row['HWLoad'] > EquipMax * EquipTD  : 
        BoilerOut = min ( row['HWLoad'] , EquipMax * EquipQuantity )
    else:
        BoilerOut = 0 
        
    return BoilerOut

# =============================================================================
# ***How to call this function *** 
# ***defining the data frames ***
# temporary input data fram 
Load_Temp = abs(pd.DataFrame ( data = LoadProfile['HWLoad']))  #converting back to Data frame 
#output data fram 
EquipmentOutput = pd.DataFrame(columns=['EquipmentOutput'])
#Function Call 
EquipmentOutput['EquipmentOutput'] = Load_Temp.apply(EquipmentDemand, axis = 1 , Equipment = Equipment)
#saving to CSV, this can be eliminated 
EquipmentOutput.to_csv('EquipmentOutput.csv') 
#################################################################################################################


#################################################################################################################
# 4.e : Boiler Consumption Function 
## Libraries : Pandas as pd 
## Input DataPath, EquipmentOutput, Boiler 
## Outputs BoilerConsumption 
data_path = 'C:/Users/Taraneh/Desktop/Python/Sample Data'
 
EquipmentOutput = pd.read_csv(data_path + '/EquipmentOutput.csv', index_col=0) 
# =============================================================================
# *** User defined inputs ***

Boiler = {'Efficiency': 0.8, 'Type' : 'Gas' }
# =============================================================================
# *** Defining the calculation Function ***
 
def BoilerInput(row , Boiler ):
    
    BoilerEfficiency = Boiler['Efficiency']
    
    return  row['EquipmentOutput'] * BoilerEfficiency 
# =============================================================================
# ***How to call this function *** 

BoilerConsumption = pd.DataFrame(columns=['BoilerInput'])

BoilerConsumption['BoilerInput'] = EquipmentOutput.apply(BoilerInput, axis = 1 , Boiler = Boiler)

BoilerAnnualConsumption = BoilerConsumption.sum(axis=0)

BoilerAnnualTherms = BoilerAnnualConsumption/1000

##############################################################################


##############################################################################
# 4.f : Chiller Consumption Function 
## Libraries : Pandas as pd, numpy as np, from scipy.optimize import curve_fit 
## Input : ChillerPerformance
## Outputs R, ChillerKw


# =============================================================================
# Import all the needed Librari
import numpy as np 
import pandas as pd
from scipy.optimize import curve_fit 
from matplotlib import pyplot as plt 
# =============================================================================
# Here we define the chiller tons and kw s : we need to call this ChillerPerformance
tons = np.array([200,180,160,140,120,100,80,60,48])
kws = np.array([236.10,191.70,157.20,131.20,105.70,80.02,59.81,47.39,41.89])
n = 6 # we have to find R for numbers 1 through 6 and find the best fit, n anr R value 
# =============================================================================

# =============================================================================
#Calculate the polynomial 
#to do : find the R for the fitted curve 

def ChillerKW (Load, tons = tons, kws = kws): 
    curve_coef = np.polyfit(tons,kws,n)
    chillerkw = np.poly1d(curve_coef)
    
    return chillerkw(Load)

df = pd.DataFrame([60,70,66])
#need to work on how to call this 
##############################################################################


##############################################################################
# 4.g : Electric Cost Calculator Function - @aks
## Input 
## Outputs 
##############################################################################


##############################################################################
# 4.h: Gas Cost Calculator FUnction 
## Input 
## Outputs 
##############################################################################


##############################################################################
# 4.i : Carbon Calculator Function - @ate
## Input 
## Outputs 
##############################################################################


##############################################################################
# 4.j : Variable vs Time Plotter function - @max
## Inputs
#
#   df - a pandas DataFrame object with timestamps in the first column & some variable of interest in the second column.
#
## Outputs 
#
#   No outputs. This function just draws a plot. We could change it so it returns a matplotlib object (figure or axes) and then use that to plot later.
#
## TODO
#
#   -Make more flexible/robust
#   -If it's always going to be 8760 data, we can work on making the x-axis prettier with month names
#
def draw_plot(df):
    y_values = df.iloc[:,1] # Values in the 2nd column will be plotted on the y-axis
    x_values = range(len(y_values)) # x-axis is just a range of the same length as y_values
    
    y_label = df.columns[1] # Name of 2nd column is y-axis label
    x_label = df.columns[0] # Name of 1st column is x-axis label

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.set_title(y_label + ' vs. ' + x_label) # set the title 
    ax.set_xlabel(x_label) # label the x-axis
    ax.set_ylabel(y_label) #label the y-axis
    ax.plot(x_values, y_values,lw=0.1)  # Plot the data
    plt.show() #show the plot
    return

##############################################################################
# 4.k : Variable vs Variable Plotter Function - @max
## Input 
## Outputs 
##############################################################################


##############################################################################
# 4.l : DIsstribution Energy Consumption 
## Input 
## Outputs 
