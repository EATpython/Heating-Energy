####################################################################################################################
#
# eatlib - Energy Automation Team (EAT) Library
#
# this is a library of functions and classes to be used in EAT scripts



####################################################################################################################
# IMPORTS

import os
import random
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import numpy as np
# import warnings
# import time
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from scipy.optimize import curve_fit
from matplotlib import pyplot as plt



####################################################################################################################
# FUNCTIONS:

###########################################################################
# e.g. DATA CLEANING FUNCTIONS:

###########################################################################
# e.g. ENERGY FUNCTIONS:

###########################################################################
# PLOTTING FUNCTIONS:

# testing

#####################################################
# plot_time(df) - variable vs. time plotting function
#
#   Imports:
#
#   import pandas as pd
#   import datetime
#   import plotly.graph_objects as go (IF USING PLOTLY)
#   from matplotlib import pyplot as plt (IF USING MATPLOTLIB)
#
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
#   -Show interpolated data in a different color
#
# PLOTLY.GRAPH_OBJECTS VERSION - STABLE
def plot_time(df):
    # import pandas as pd
    # import plotly.graph_objects as go
    # import datetime
    print('\nPLOT_TIME FUNCTION ACTIVATED') # let the user know this function has been called

    # print some information about the data being plotted
    print("\n HERE'S A PREVIEW OF THE DATA YOU'RE PLOTTING:")
    print(df)
    print()
    print(df.dtypes)

    # convert timestamps to datetime64 objects
    print('\nconverting timestamp data...')
    timestamps = pd.to_datetime(df.iloc[:, 0])
    print('TIMESTAMP DATA CONVERTED FROM', type(df.iloc[0, 0]), 'TO', type(timestamps[0]))
    df.iloc[:, 0] = timestamps
    print(df.iloc[:, 0].head())

    # use graph_objects to create the figure
    fig = go.Figure()

    # create traces for each column vs. time
    for i in range(df.shape[1] - 1):
        fig.add_trace(go.Scatter(x=timestamps, y=df.iloc[:, i + 1],
                                 visible='legendonly',
                                 mode='lines',
                                 name=df.columns[i + 1]))
        #TODO add label for max value
        # fig.add_annotation(x=2, y=5,
        #                    text="Text annotation with arrow",
        #                    showarrow=True,
        #                    arrowhead=1)

    fig.update_layout(showlegend=True)    # force the legend for single-trace plots
    fig.update_layout(legend_title_text='Points:')
    fig.update_layout(hovermode='x')
    # fig.show()    # changed this to return a fig instead of plotting. can change back if we want.
    return fig
#
# # PLOTLY.EXPRESS VERSION - STABLE
# def plot_time(df):
#     # import pandas as pd
#     # import plotly.express as px
#     # import datetime
#     print('\nPLOT_TIME FUNCTION ACTIVATED') # let the user know this function has been called
#
#     pd.options.plotting.backend = "plotly"  # activate Plotly backend
#     print('plotly backend activated...')
#
#     print("\n HERE'S A PREVIEW OF THE DATA YOU'RE PLOTTING:")
#     print(df)   # print some information about the data being plotted
#     print()
#     print(df.dtypes)
#
#     print('\nconverting timestamp data...')  # convert timestamps to datetime64 objects
#     timestamp = pd.to_datetime(df.iloc[:, 0])
#     print('TIMESTAMP DATA CONVERTED FROM', type(df.iloc[0, 0]), 'TO', type(timestamp[0]))
#     df.iloc[:, 0] = timestamp
#     print(df.iloc[:, 0].head())
#
#     y_values = df.iloc[:,1] # values in the 2nd column will be plotted on the y-axis
#     x_values = df.iloc[:,0] # timestamps on the x-axis
#
#     y_label = df.columns[1] # name of 2nd column is y-axis label
#     x_label = df.columns[0] # name of 1st column is x-axis label
#     xy_labels = {'x': x_label, 'y': y_label}    # create a dictionary of the labels to pass to px.line
#
#     fig = px.line(x=x_values, y=y_values, labels=xy_labels, title=y_label + ' vs. ' + x_label)  # plot using plotly
#     fig.show()
#     return
#
# MATPLOTLIB VERSION - STABLE
# def plot_time(df):
#     # import pandas as pd
#     # from matplotlib import pyplot as plt
#
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


#####################################################
# plot_x(df) - variable vs. variable plotting function
#
#   Imports:
#
#   import pandas as pd
#   import plotly.express as px (IF USING PLOTLY)
#   from matplotlib import pyplot as plt (IF USING MATPLOTLIB)
#
#
#   Inputs:
#
#   df - 'nx2' pandas DataFrame object with x-values in the first column & y-values in the second column.
#
#
#   Outputs:
#
#   No outputs. This function just draws a plot. We could change it so it returns a matplotlib object (figure or axes) and then use that to plot later.
#
# PLOTLY VERSION - STABLE
def plot_x(df):
    # import pandas as pd
    # import plotly.express as px
    print("\n HERE'S A PREVIEW OF THE DATA YOU'RE PLOTTING:")  # show a preview of the data passed to the function
    print(df)   # print some information about the data being plotted
    print()
    print(df.dtypes)

    x_values = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
    y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis

    x_label = df.columns[0]  # Name of 1st column is x-axis label
    y_label = df.columns[1]  # Name of 2nd column is y-axis label
    xy_labels = {'x': x_label, 'y': y_label}    # create a dictionary of the labels to pass to px.line

    if (type(x_values[1]) == str) or (type(y_values[1]) == str):    # do a quick check that the data is plottable (i.e. not a string - this could be more robust)
        print("\nERROR: Please make sure you are plotting numerical data.\n")
        return

    fig = px.scatter(x=x_values, y=y_values, labels=xy_labels, title=y_label + ' vs. ' + x_label, trendline="ols")  # plot using plotly
    fig.show()
    return
#
# MATPLOTLIB VERSION - STABLE
# def plot_x(df):
#     # import pandas as pd
#     # from matplotlib import pyplot as plt
#
#     print("\n HERE'S A PREVIEW OF THE DATA YOU'RE PLOTTING:")  # show a preview of the data passed to the function
#     print(df)   # print some information about the data being plotted
#     print()
#     print(df.dtypes)
#
#     x_values = df.iloc[:, 0]  # Values in the 1st column will be plotted on the x-axis
#     y_values = df.iloc[:, 1]  # Values in the 2nd column will be plotted on the y-axis
#
#     x_label = df.columns[0]  # Name of 1st column is x-axis label
#     y_label = df.columns[1]  # Name of 2nd column is y-axis labelxy_labels = {'x': x_label, 'y': y_label}    # create a dictionary of the labels to pass to px.line
#
#     # make the plot
#     fig, ax = plt.subplots()  # Create a figure containing a single axes.
#     ax.set_title(str(y_label) + ' vs. ' + str(x_label))  # set the title
#     ax.set_xlabel(x_label)  # label the x-axis
#     ax.set_ylabel(y_label)  # label the y-axis
#     ax.plot(x_values, y_values, lw=0.1)  # Plot the data
#     plt.show()  # show the plot
#     return
##############################################################################



####################################################################################################################
# CLASSES:

# class