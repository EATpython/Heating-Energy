####################################################################################################################
#
# eatlib - Energy Automation Team (EAT) Library
#
# this is a library of functions to be used in EAT scripts



####################################################################################################################
# IMPORTS

import pandas as pd
import plotly.express as px
import datetime
# import numpy as np
# import warnings
# import time
# import matplotlib.pyplot as plt
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from scipy.optimize import curve_fit
# from matplotlib import pyplot as plt



####################################################################################################################
# FUNCTIONS:

# PLOTTING FUNCTIONS:

#####################################################
# plot_time(df) - variable vs. time plotting function
#
#   Imports:
#
#   pandas ad pd
#   from matplotlib import pyplot as plt
#
#   Inputs:
#
#   df - a pandas DataFrame object with timestamps in the first column & some variable of interest in the second column.
#
#
#   Outputs:
#
#   No outputs. This function just draws a plot. We could change it so it returns a matplotlib object (figure or axes) and then use that to plot later.
#
#
#   TODO:
#
#   -Make more flexible/robust
#   -If it's always going to be 8760 data, we can work on making the x-axis prettier with month names
#
# PLOTLY VERSION - STABLE
def plot_time(df):
    pd.options.plotting.backend = "plotly"  # activate Plotly backend
    print('PLOTLY BACKEND ACTIVATED')

    y_values = df.iloc[:,1]  # Values in the 2nd column will be plotted on the y-axis
    x_values = range(len(y_values))  # x-axis is just a range of the same length as y_values

    y_label = df.columns[1] # name of 2nd column is y-axis label
    x_label = df.columns[0] # name of 1st column is x-axis label
    xy_labels = {'x': x_label, 'y': y_label}    # create a dictionary of the labels to pass to px.line

    fig = px.line(x=x_values, y=y_values, labels=xy_labels, title=y_label + ' vs. ' + x_label)  # plot using plotly
    fig.show()
    return

# MATPLOTLIB VERSION - STABLE
# def plot_time(df):
#     y_values = df.iloc[:,1]  # Values in the 2nd column will be plotted on the y-axis
#     x_values = range(len(y_values))  # x-axis is just a range of the same length as y_values
#
#     x_ticks = [x*796.364 for x in range(12)]    # create x ticks corresponding to months
#     months = ['J','F','M','A','M','J','J','A','S','O','N','D']  # list of months
#
#     y_label = df.columns[1]  # Name of 2nd column is y-axis label
#     x_label = df.columns[0]  # Name of 1st column is x-axis label
#
#     fig, ax = plt.subplots()  # Create a figure containing a single axes.
#     ax.set_title(y_label + ' vs. ' + x_label)  # set the title
#     ax.set_xlabel(x_label)  # label the x-axis
#     ax.set_ylabel(y_label)  # label the y-axis
#     ax.set_xticks(x_ticks)  # set and label x-ticks
#     ax.set_xticklabels(months)
#     ax.plot(x_values, y_values, lw=0.1)  # plot using matplotlib
#     plt.show()  # show the plot
#     return
#####################################################



# plot_x(df) - variable vs. variable plotting function
#
#   Inputs:
#
#   df - 'nx2' pandas DataFrame object with x-values in the first column & y-values in the second column.
#
#   Outputs:
#
#   No outputs. This function just draws a plot. We could change it so it returns a matplotlib object (figure or axes) and then use that to plot later.
#
#   TODO:
#
#   -Make more flexible/robust
#   -If it's always going to be 8760 data, we can work on making the x-axis prettier with month names
def plot_x(df):
    print(
        "\nHere's a preview of the data you're trying to plot:\n")  # show a preview of the data passed to the function
    print(df.head())

    x_values = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
    y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis

    x_label = df.columns[0]  # Name of 1st column is x-axis label
    y_label = df.columns[1]  # Name of 2nd column is y-axis label

    print("\nx-values are of type: ", type(x_values[1]))  # print data types to the console
    print("y-values are of type: ", type(y_values[1]))

    # do a quick check that the data is plottable (i.e. not a string - this could be more robust)
    if (type(x_values[1]) == str) or (type(y_values[1]) == str):
        print("\nERROR: Please make sure you are plotting numerical data.\n")
        return

    # make the plot
    print('\nData looks good. Ready to plot. Here we gooooooooo!!!!!\n')
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.set_title(str(y_label) + ' vs. ' + str(x_label))  # set the title
    ax.set_xlabel(x_label)  # label the x-axis
    ax.set_ylabel(y_label)  # label the y-axis
    ax.plot(x_values, y_values, lw=0.1)  # Plot the data
    plt.show()  # show the plot
    return

##############################################################################
# 4.l : Disstribution Energy Consumption
## Input
## Outputs
