#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:37:43 2021

@author: maxsun
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #function
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

root = '/Users/maxsun/EAT'

df = pd.read_csv(root + '/EquipmentOutput.csv')

plot = draw_plot(df)

# plt.show() # Show the plot