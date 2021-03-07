####################################################################################################################
#
# script for demonstrating weekly progress - Max
# imports and calls functions from eatlib
#
####################################################################################################################

# IMPORTS
from eatlib import *

# SCRIPT

root = '/Users/maxsun/EAT' # define path to sample data

df = pd.read_csv(root + '/EquipmentOutput.csv') # read data into a DataFrame and print some info
print('\nDATA READ SUCCESSFULLY:\n')
print(df)
print()
print(df.dtypes)

plot_time(df) #call a function from eatlib to plot the data

