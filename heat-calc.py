# Practice collaboration file


# Step 1 - Lets list all the libraries that needs to be imported
import pandas as pd
import numpy as np
import warnings
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

# Step 2 - Lets Define all the User Inputs Required

# Step 3 - Lets Define all the variables that we will use with description


#################################################################################################################
# Step 4 - Lets Create all the functions 
## Input
## Outputs 
#################################################################################################################


#################################################################################################################
# 4.a : User Prompt Input, save to
## Input 
## Outputs 
#################################################################################################################


#################################################################################################################
# 4.b : Data Cleaning
# ====================================================================================================
# import pandas as pd
# import time
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# ====================================================================================================


# ====================================================================================================
# begin tracking overall runtime
main_start_time = time.time()
print("\n" + 'Data cleaning in process...')

# ====================================================================================================
# DEFINE CSV FUNCTION
# ====================================================================================================
file_open_title = "Select Raw CSV File"


# Todo: identify process for reading xls files in lieu of csv
def open_csv_file():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('CSV', '*.csv')], title=file_open_title)
    print("\n" + "     FILE LOADED: " + file_path)
    return file_path


# ====================================================================================================
# PROMPT USER TO SPECIFY CSV FILE, READ FILE CONTENTS & FORMAT HEADER NAMES
# ====================================================================================================
csv_file = open_csv_file()
font = ("Verdana", 8)
revised_headers = []


def read_csv():
    # create dataframe object from csv file
    df = pd.read_csv(filepath_or_buffer=csv_file, header=0, mangle_dupe_cols=True, parse_dates=[0])

    print('READ CSV FILE')
    return df


def format_data_headers():
    df = read_csv()
    # specify name for first column header
    first_column_name = 'TIME'
    # rename first column header to first_column_name
    df.rename(columns={df.columns[0]: first_column_name}, inplace=True)
    # drop rows under the first_column_name column when empty
    df.dropna(subset=[first_column_name], inplace=True)

    # remove any trailing spaces
    df.columns = df.columns.str.strip()
    # replace spaces " " with an "_"
    df.columns = df.columns.str.replace(' ', '_')
    # make all header names uppercase
    df.columns = df.columns.str.upper()

    print('HEADERS FORMATTED')
    print()
    return df


print(format_data_headers().head())

# ====================================================================================================
# UPDATE HEADER NAMES VIA USER INPUT
# ====================================================================================================


class UserInputsApp:
    def __init__(self, parent, *args, **kwargs):
        df = format_data_headers()
        header_lst = [item + ':' for item in df.columns]
        self.user_inputs = []
        self.bldg_prefix = ""
        self.myParent = parent
        self.myContainer1 = tk.Frame(parent, relief=tk.SUNKEN, borderwidth=4, *args, **kwargs)
        self.myContainer1.grid(padx=5, pady=5)

        self.myContainer2 = tk.Frame(parent, relief=tk.FLAT, borderwidth=4, *args, **kwargs)
        self.myContainer2.grid(padx=5, pady=5)

        self.label_entry2 = tk.Label(self.myContainer1, text="[ BLDG ] _ [ EQUP TYPE ] _ [ EQUP NO. ] _ [ SYS ]",
                                     width=41, font=font)
        self.label_entry2.grid(row=2, column=1, sticky='nsew')

        for idx, text in enumerate(header_lst):
            self.label2 = tk.Label(self.myContainer1, text=text, width=25, font=font)
            self.label2.grid(row=idx + 3, column=0, sticky='e')

            self.entry2 = tk.Entry(self.myContainer1, width=40)
            self.entry2.grid(row=idx + 3, column=1, sticky='nsew')
            self.user_inputs.append(self.entry2)

        self.button2 = tk.Button(self.myContainer2, text="Submit", width=10, font=font,
                                 activebackground='grey', activeforeground='blue')
        self.button2.bind('<Button-1>', self.get_values)
        self.button2.grid(row=0, column=1, sticky='nsew')

        self.button3 = tk.Button(self.myContainer2, text="Close", width=5, font=font)
        self.button3.bind('<Button-1>', self.close_wind)
        self.button3.grid(row=0, column=2, sticky='nsew')

    def get_values(self, event):
        for entry in self.user_inputs:
            revised_headers.append(entry.get())
        self.myParent.quit()

    def close_wind(self, event):
        self.myParent.quit()


if __name__ == "__main__":
    root = tk.Tk()
    user_inputs = []
    root.wm_title('Header Names')
    root.geometry("500x400")
    UserInputsApp(root)
    root.mainloop()
    root.destroy()

print()
print(revised_headers)
print()

# # ====================================================================================================
# # CHECK FOR MISSING DATA, ANALYZE MISSING DATA & RETURN UPDATED DF WITH NEW HEADER NAMES
# # ====================================================================================================


def consec_miss_data():
    df = format_data_headers()
    df.columns = revised_headers
    df_md_ind = pd.DataFrame()
    df_md_ind_results = pd.DataFrame()

    counter = 0
    header_main = list(df.columns)
    header_count = len(df.columns)

    while counter < header_count:
        for i in header_main:
            lst_temp = []
            df_temp = df.copy()

            df_temp['Group'] = df_temp[header_main[counter]].notnull().astype(int).cumsum()
            df_temp = df_temp[df_temp[header_main[counter]].isnull()]

            df_temp = df_temp[df_temp['Group'].isin(df_temp['Group'].value_counts().index)]
            df_temp['Count'] = df_temp.groupby('Group')['Group'].transform('size')

            max_value = df_temp['Count'].max()
            df_md_ind = df_md_ind.append(df_temp)

            lst_temp.append([header_main[counter], str(max_value)])
            df_md_ind_results = df_md_ind_results.append(lst_temp)
            counter += 1

    df_md_ind_results.columns = ['Name', 'Long_Count']
    df_md_ind_results.reset_index(drop=True, inplace=True)

    df_md_ind.drop_duplicates(inplace=True)
    df_md_ind.sort_values(by='TIME', ascending=False, inplace=True)
    df_md_ind.drop(['Group', 'Count'], axis=1, inplace=True)

    print('CONSECUTIVE MISSING DATA REVIEW COMPLETE')
    return df_md_ind_results, df_md_ind, df


print()
print(consec_miss_data()[2].head())
print()

# # ====================================================================================================
# # ANALYZE & SUMMARIZE MISSING DATA FROM MAIN DATA SOURCE
# # ====================================================================================================


def analyze_empty_fields():
    df = consec_miss_data()[2]
    # find total count cells with missing data
    missing_data_count = df.isnull().sum()
    # create new dataframe for missing data
    df_md = pd.DataFrame(missing_data_count)
    # calculate percentage of missing data
    pct = round((df_md[0] / len(df)) * 100, 2)
    # add columns header names
    df_md['%'] = pct
    df_md.reset_index(inplace=True)
    df_md.columns = ['Name', 'Total_Count', '%']

    print('EMPTY FIELDS ANALYZED')
    return df_md


print(analyze_empty_fields().head())
print()


def merge_df():
    df_md = analyze_empty_fields()
    df_md_ind_results = consec_miss_data()[0]
    # merge dataframe df_md with df_md_ind_results
    df_md_review = pd.merge(df_md_ind_results, df_md, how='inner')

    print('DATAFRAME MERGE COMPLETE')
    return df_md_review


print(merge_df().head())
print()

# # ====================================================================================================
# # FILL EMPTY DATA POINTS WITH VALUES FROM PREVIOUS ROW FOR EACH COLUMN
# # ====================================================================================================


def fill_empty_fields():
    df = consec_miss_data()[2]
    # allowable_missing_data = 20
    # fill in cells with missing data with value from previous row
    df.fillna(axis=0, method='ffill', inplace=True)  # , limit=allowable_missing_data)
    # TODO: Use average values. Use last known value in any given column and the next
    # TODO: available value to obtain avg values to fill in gaps with

    print('EMPTY FIELDS POPULATED')
    return df


print(fill_empty_fields().head())
print()

# # ====================================================================================================
# # EXPORT NEW CSV FILES WITH FORMATTED DATA
# # ====================================================================================================


def export_csv():
    df = fill_empty_fields()
    df_md_review = merge_df()
    df_md_ind = consec_miss_data()[1]
    # export revised dataframes to new csv file
    df.to_csv(csv_file.replace('.csv', '_OUT_Clean_Data.csv'))
    df_md_review.to_csv(csv_file.replace('.csv', '_OUT_Missing_Data_Summary.csv'))
    df_md_ind.to_csv(csv_file.replace('.csv', '_OUT_Missing_Data_Report.csv'))

    print('RESULTS EXPORTED INTO CSV FILES')
    return


export_csv()

# # ====================================================================================================
# # >>>END OF SCRIPT<<<
# # ====================================================================================================

print("\n" + ">>>DATA CLEANING PROCESS COMPLETE!<<<")
print(">>>TOTAL RUNTIME: %s seconds" % (time.time() - main_start_time).__round__(3))

# alert user upon successful completion
tk.messagebox.showinfo('Status', 'Data Cleaning Process Complete!')

# ====================================================================================================
# >>>END OF DATA CLEANING SCRIPT<<<
# ====================================================================================================


#################################################################################################################


#################################################################################################################
# 4.c : Load Profile Generation
## Input 
## Outputs 
#################################################################################################################


#################################################################################################################
# 4.d : EquipmentDemand Function
## Libraries : Pandas as pd 
## Input : LoadProfile, data_path, Equipment
## df variable pulled from fill_empty_fields function. Returns clean dataset.
## Outputs : EquipmentOutput

LoadProfile = fill_empty_fields()  # returns dataframe 'df' values

# =============================================================================
# *** User defined inputs ***

Equipment = {'Quantity': 1, 'Size': 200, 'Turndown' : 0.05 }
# Todo create popup to allow for user input

# =============================================================================
# Todo : Unmet hours count , so you can after 10 of unmet hours run at turn doen 1 time


# *** Defining the calculation Function ***
def EquipmentDemand(row, Equipment):
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
Load_Temp = abs(pd.DataFrame (data = LoadProfile['HWLoad'])) # converting back to Data frame
# Todo: move into data cleaning section of script
# output data frame
EquipmentOutput = pd.DataFrame(columns=['EquipmentOutput'])
# Function Call
EquipmentOutput['EquipmentOutput'] = Load_Temp.apply(EquipmentDemand, axis = 1, Equipment = Equipment)
# saving to CSV, this can be eliminated
# EquipmentOutput.to_csv('EquipmentOutput.csv')
print(EquipmentOutput)
#################################################################################################################


#################################################################################################################
# 4.e : Boiler Consumption Function 
## Libraries : Pandas as pd 
## Input DataPath, EquipmentOutput, Boiler 
## Outputs BoilerConsumption 

# =============================================================================
# *** User defined inputs ***

Boiler = {'Efficiency': 0.8, 'Type' : 'Gas' }
# Todo create popup to a lot for user input

# =============================================================================
# *** Defining the calculation Function ***

def BoilerInput(row , Boiler ):
    BoilerEfficiency = Boiler['Efficiency']
    return row['EquipmentOutput'] * BoilerEfficiency
# =============================================================================
# ***How to call this function *** 

BoilerConsumption = pd.DataFrame(columns=['BoilerInput'])

BoilerConsumption['BoilerInput'] = EquipmentOutput.apply(BoilerInput, axis = 1 , Boiler = Boiler)

BoilerAnnualConsumption = BoilerConsumption.sum(axis=0)

BoilerAnnualTherms = BoilerAnnualConsumption/1000
# Todo: simplify code through the use of dataframes to perform iteration in lieu of using .apply method
##############################################################################


##############################################################################
# 4.f : Chiller Consumption Function 
## Libraries : Pandas as pd, numpy as np, from scipy.optimize import curve_fit 
## Input : ChillerPerformance
## Outputs R, ChillerKw


# =============================================================================

# =============================================================================
# Here we define the chiller tons and kw s : we need to call this ChillerPerformance
tons = np.array([200,180,160,140,120,100,80,60,48])
kws = np.array([236.10,191.70,157.20,131.20,105.70,80.02,59.81,47.39,41.89])
n = 6 # we have to find R for numbers 1 through 6 and find the best fit, n anr R value
# Todo: identify what information would be needed from an end user stand point. big picture, different functions
## would call for specific columns of data
# =============================================================================

# =============================================================================
# Calculate the polynomial
# Todo: find the R for the fitted curve


def ChillerKW (Load_Frame, tons = tons, kws = kws):
    curve_coef = np.polyfit(tons, kws, n)
    chillerkw = np.poly1d(curve_coef)

    return chillerkw(Load_Frame)

# need to work on how to call this
##############################################################################


##############################################################################
# 4.g : Electric Cost Calculator Function - @aks
## Input 
## Outputs
# Todo: akshay to past in coding from local files
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
    y_values = df.iloc[:,1]  # Values in the 2nd column will be plotted on the y-axis
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
## Input 
## Outputs 
##############################################################################


##############################################################################
# 4.l : Disstribution Energy Consumption
## Input 
## Outputs
