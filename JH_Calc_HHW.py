# ====================================================================================================
# Author:         Jonathan Herrera
# Created on:     August 24, 2020
# Last Modified:  August 24, 2020
# Python Ver:     3.8
# Copyright:      P2S Inc. 2020
# ====================================================================================================
import pandas as pd
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# ====================================================================================================
# CONFIGURATION: NONE
# ====================================================================================================
# begin tracking overall runtime
main_start_time = time.time()
print("\n" + 'Starting HHW calculation...')
# ====================================================================================================
# DEFINE CSV FUNCTION
# ====================================================================================================
# begin tracking runtime for code section
start_time = time.time()

# establish global variables
file_open_title = "Select Clean CSV File"


def open_csv_file():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('CSV', '*.csv')], title=file_open_title)
    print("\n" + "     FILE LOADED: " + file_path)
    return file_path


print("\n" + ">>>DEFINE CSV FUNCTION COMPLETE<<<")
print(">>>RUNTIME: %s seconds" % (time.time() - start_time).__round__(3))

# ====================================================================================================
# PROMPT USER TO SPECIFY CSV FILE & ANALYZE FILE CONTENTS
# ====================================================================================================
# begin tracking runtime for code section
start_time = time.time()
csv_file = open_csv_file()

# create dataframe object
df = pd.read_csv(filepath_or_buffer=csv_file, header=0, mangle_dupe_cols=True,
                 parse_dates=[0])

# get total number of columns
header_count = len(df.columns)
# get total number of rows
data_body_count = len(df)
print("     NO. OF COLUMNS : " + str(header_count))
print("     NO. OF ROWS    : " + str(data_body_count))

print("\n" + ">>>PROMPT USER TO SPECIFY CSV FILE & ANALYZE FILE CONTENTS COMPLETE<<<")
print(">>>RUNTIME: %s seconds" % (time.time() - start_time).__round__(3))
print()

# ====================================================================================================
# CALC
# ====================================================================================================
# begin tracking runtime for code section
start_time = time.time()


def calc_hhw():
    results = pd.DataFrame()
    results['TIME'] = df['TIME']
    results['MBH'] = (500 * (df['ZNI_HHWS_TEMP'] - df['ZNI_HHWR_TEMP']) * df['BCC_HHWR_FLOW'] / 1000).__round__(2)
    results.to_csv(csv_file.replace('.csv', '_OUT_HHW Calc.csv'))
    return results


print('RESULTS:')
print(calc_hhw().head())

print("\n" + ">>>CALC TESTING COMPLETE<<<")
print(">>>RUNTIME: %s seconds" % (time.time() - start_time).__round__(3))

# ====================================================================================================
# >>>END OF SCRIPT<<<
# ====================================================================================================
print("\n" + ">>>PROCESS COMPLETE!<<<")
print(">>>TOTAL RUNTIME: %s seconds" % (time.time() - main_start_time).__round__(3))

# alert user upon successful completion
tk.messagebox.showinfo('Status', 'HHW Calculations Complete!')

# ====================================================================================================
# >>>END OF SCRIPT<<<
# ====================================================================================================
