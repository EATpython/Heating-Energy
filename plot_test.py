#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:37:43 2021

@author: maxsun
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # #function
# def draw_plot(df):
#     y_values = df.iloc[:,1] # Values in the 2nd column will be plotted on the y-axis
#     x_values = range(len(y_values)) # x-axis is just a range of the same length as y_values
#     y_label = df.columns[1] # Name of 2nd column is y-axis label
#     x_label = df.columns[0] # Name of 1st column is x-axis label
#
#     fig, ax = plt.subplots()  # Create a figure containing a single axes.
#     ax.set_title(y_label + ' vs. ' + x_label) # set the title
#     ax.set_xlabel(x_label) # label the x-axis
#     ax.set_ylabel(y_label) #label the y-axis
#     ax.plot(x_values, y_values,lw=0.1)  # Plot the data
#     plt.show() #show the plot
#     return
# #

#####################################################################################################################

# SANDBOX
#
# root = '/Users/maxsun/EAT'

# df = pd.read_csv(root + '/EquipmentOutput.csv')
# print(df.head())
# print(df.dtypes)
#
# x_values_time = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
# y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis
# x_values = np.random.randn(y_values.size)  # Values in the 1st column will be plotted on the x-axis
#
# x = x_values_time[1]
# print(type(x))
#
# x_label = df.columns[0]  # Name of 1st column is x-axis label
# y_label = df.columns[1]  # Name of 2nd column is y-axis label

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.set_title(y_label + ' vs. ' + x_label)  # set the title
# ax.set_xlabel(x_label)  # label the x-axis
# ax.set_ylabel(y_label)  # label the y-axis
# ax.plot(x_values, y_values, lw=0.1)  # Plot the data
# plt.show()  # show the plot

# FUNCTION
#
# def plot_x(df):
#     print("\nHere's a preview of the data you're trying to plot:\n") #show a preview of the data passed to the function
#     print(df.head())
#
#     x_values = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
#     y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis
#
#     x_label = df.columns[0]  # Name of 1st column is x-axis label
#     y_label = df.columns[1]  # Name of 2nd column is y-axis label
#
#     print("\nx-values are of type: ", type(x_values[1])) #print data types to the console
#     print("y-values are of type: ", type(y_values[1]))
#
#     #do a quick check that the data is plottable (i.e. not a string - this could be more robust)
#     if (type(x_values[1]) == str) or (type(y_values[1]) == str):
#         print("\nERROR: Please make sure you are plotting numerical data.\n")
#         return
#
#     #make the plot
#     print('\nData looks good. Ready to plot. Here we gooooooooo!!!!!\n')
#     fig, ax = plt.subplots()  # Create a figure containing a single axes.
#     ax.set_title(str(y_label) + ' vs. ' + str(x_label))  # set the title
#     ax.set_xlabel(x_label)  # label the x-axis
#     ax.set_ylabel(y_label)  # label the y-axis
#     ax.plot(x_values, y_values, lw=0.1)  # Plot the data
#     plt.show()  # show the plot
#     return

#SCRIPT
#


root = '/Users/maxsun/EAT'

# df = pd.read_csv(root + '/EquipmentOutput.csv')
df = pd.DataFrame(np.random.random(size=(1000,2)))
plot = plot_x(df)





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
def plot_time(df):
    y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis
    x_values = range(len(y_values))  # x-axis is just a range of the same length as y_values

    y_label = df.columns[1]  # Name of 2nd column is y-axis label
    x_label = df.columns[0]  # Name of 1st column is x-axis label

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.set_title(y_label + ' vs. ' + x_label)  # set the title
    ax.set_xlabel(x_label)  # label the x-axis
    ax.set_ylabel(y_label)  # label the y-axis
    ax.plot(x_values, y_values, lw=0.1)  # Plot the data
    plt.show()  # show the plot
    return

##############################################################################
# 4.k : Variable vs Variable Plotter Function - @max
## Inputs
#
#   df - 'nx2' pandas DataFrame object with x-values in the first column & y-values in the second column.
#
## Outputs
#
#   No outputs. This function just draws a plot. We could change it so it returns a matplotlib object (figure or axes) and then use that to plot later.
#
##############################################################################
def plot_x(df):
    print("\nHere's a preview of the data you're trying to plot:\n") #show a preview of the data passed to the function
    print(df.head())

    x_values = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
    y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis

    x_label = df.columns[0]  # Name of 1st column is x-axis label
    y_label = df.columns[1]  # Name of 2nd column is y-axis label

    print("\nx-values are of type: ", type(x_values[1])) #print data types to the console
    print("y-values are of type: ", type(y_values[1]))

    #do a quick check that the data is plottable (i.e. not a string - this could be more robust)
    if (type(x_values[1]) == str) or (type(y_values[1]) == str):
        print("\nERROR: Please make sure you are plotting numerical data.\n")
        return

    #make the plot
    print('\nData looks good. Ready to plot. Here we gooooooooo!!!!!\n')
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.set_title(str(y_label) + ' vs. ' + str(x_label))  # set the title
    ax.set_xlabel(x_label)  # label the x-axis
    ax.set_ylabel(y_label)  # label the y-axis
    ax.plot(x_values, y_values, lw=0.1)  # Plot the data
    plt.show()  # show the plot
    return
