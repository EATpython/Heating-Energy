# ====================================================================================================
# Author:         Jonathan Herrera
# Created on:     August 24, 2020
# Last Modified:  August 24, 2020
# Python Ver:     3.8
# Copyright:      P2S Inc. 2020
# ====================================================================================================
import pandas as pd
import time
from time import strptime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# ====================================================================================================
# CONFIGURATION: NONE
# ====================================================================================================
# begin tracking overall runtime
main_start_time = time.time()
print("\n" + 'Starting heating and cooling calculation...')
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
                 parse_dates=[0], decimal='.')

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

# convert selected columns to numeric values
df_numb = df.replace(to_replace=",", value="", inplace=True, regex=True)
df_numb = df.iloc[:, 5:].apply(pd.to_numeric)

# create datetime object
date_temp = pd.DataFrame()
date_year = '2020'  # inserted as placeholder for testing purposes only
date_temp['Month'] = df['TIME'].apply(lambda x: strptime(x, '%b').tm_mon)
date_temp['Day'] = df['DAY']

# todo: subtract one hour
date_temp['Hour'] = df['HOUR']
date_temp['Hour'].astype(int).apply(lambda: df['Hour'] - 1)


date_temp['Time'] = date_year + "-" + date_temp['Month'].map(str) + "-" + date_temp['Day'].map(str) + \
                    " " + date_temp['Hour'].map(str) + ":" + "00" + ":" + "00"
date_temp['Time'] = pd.to_datetime(date_temp['Time'], errors='coerce', format='%Y-%m-%d %H:%M:%S')


def calc_htg_clg():
    results = pd.DataFrame()
    results['TIME'] = date_temp['Time']

    # constants
    hrc_max_c = 200
    hrc_ratio = 1.33

    # todo: - find min value between two variables
    #       - obtain abs values from htg
    # minimum (HRC_max_C and the number in column E )
    demand_hrc_c = (hrc_max_c + df_numb['ALT_1_ALL_COOLING_COILS_TONS'])  #.min() # between two values
    # minimum of (demand_HRC_C * 12 * HRC_ratio and Column F )
    demand_hrc_h = min(demand_hrc_c * 12 * hrc_ratio, df_numb['ALT_1_ALL_COOLING_COILS_TONS'])
    # column F - demand_HRC_H
    demand_boiler = df_numb['ALT_1_ALL_HEATING_COILS_MBH'] - demand_hrc_h

    results['demand_hrc_c'] = demand_hrc_c
    results['demand_hrc_h'] = demand_hrc_h
    results['demand_boiler'] = demand_boiler
    results.to_csv(csv_file.replace('.csv', '_OUT_Heating and Cooling Calc.csv'))
    return results


print('RESULTS:')
print(calc_htg_clg().head())

print("\n" + ">>>CALC TESTING COMPLETE<<<")
print(">>>RUNTIME: %s seconds" % (time.time() - start_time).__round__(3))

# ====================================================================================================
# >>>END OF SCRIPT<<<
# ====================================================================================================
print("\n" + ">>>PROCESS COMPLETE!<<<")
print(">>>TOTAL RUNTIME: %s seconds" % (time.time() - main_start_time).__round__(3))

# alert user upon successful completion
tk.messagebox.showinfo('Status', 'Heating and cooling Calculations Complete!')

# ====================================================================================================
# >>>END OF SCRIPT<<<
# ====================================================================================================
