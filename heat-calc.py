#Practice collaboration file

# Step 1 - Lets list all the libraries that needs to be imported
import pandas as pd
import warnings
import time
import matplotlib.pyplot as plt

# Step 2 - Lets Define all the User Inputs Required

# Step 3 - Lets Define all the variables that we will use with description



# Step 4 - Lets Create all the functions 
## Input 
## Outputs 

# 4.a : User Propmt Input, save to 
## Input 
## Outputs 

# 4.b : Data Cleaning
## Input 
## Outputs 

# 4.c : Load Profile Generation
## Input 
## Outputs 
#howdy

# 4.d : Equipment Demand Function
## Input 
## Outputs 

# 4.e : Boiler Consumption Function 
## Input 
## Outputs 

# 4.f : Chiller Consumption Function 
## Input 
## Outputs 

# 4.g : Electric Cost Calculator Function - @aks
## Input 
## Outputs 

# 4.h: Gas Cost Calculator FUnction 
## Input 
## Outputs 

# 4.i : Carbon Calculator Function - @ate
## Input 
## Outputs 

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

# 4.k : Variable vs Variable Plotter Function - @max
## Input 
## Outputs 

# 4.l : DIsstribution Energy Consumption 
## Input 
## Outputs 
