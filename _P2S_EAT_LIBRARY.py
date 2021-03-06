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
from openpyxl import load_workbook

# Step 2 - Lets Define all the User Inputs Required

# Step 3 - Lets Define all the variables that we will use with description


#################################################################################################################
# Step 4 - Define all the equipment Classes:

# define a class for my boiler, maybe we want this in a function and read all the classes at once
class Boiler:
    def __init__(self, quantity, capacityMBH, turndown, efficiency):
        self.quantity = quantity
        self.capacityMBH = capacityMBH
        self.turndown = turndown  # number in percent. like 10
        self.efficiency = efficiency  # just the number like 81
        

# define a class for my Chiller, maybe we want this in a function and read all the classes at once
class Chiller:
    def __init__(self, quantity, capacityMBH, turndown):
        self.quantity = quantity
        self.capacityMBH = capacityMBH
        self.turndown = turndown  # number in percent. like 10
        
# define a class for pumps, maybe we want this in a function and read all the classes at once
class Pump:
    def __init__(self, quantity, HP, MaxGPM, turndown, efficiency):
        self.quantity = quantity
        self.HP = HP
        self.MaxGPM = MaxGPM
        self.turndown = turndown
        self.efficiency = efficiency


# =============================================================================
# I defined the pump variables here, but we would like this to be read from a file


# Create a test boiler
TestBoiler = Boiler(1, 7000, 10, 81)

CHWP1 = Pump(1, 10, 40, 10, 90)
print(CHWP1.__dict__)


# Create a test Chiller
TestChiller = Chiller(1, 150, 10)
# Here we define the chiller tons and kw s but its user input in future, we have to read this from CSV 
tons = np.array([200, 180, 160, 140, 120, 100, 80, 60, 48])
kws = np.array([236.10, 191.70, 157.20, 131.20, 105.70, 80.02, 59.81, 47.39, 41.89])
n = 6  # need to find R value to optimize this


#######################################################################################


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
# main_start_time = time.time()
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
formatted_headers = []


def read_csv():
    # create dataframe object from csv file
    df = pd.read_csv(filepath_or_buffer=csv_file, header=0, mangle_dupe_cols=True, parse_dates=[0])

    # print('READ CSV FILE')
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

    # print('HEADERS FORMATTED')
    # print()
    return df


# print(format_data_headers().head())


# ====================================================================================================
# UPDATE HEADER NAMES VIA USER INPUT
# ====================================================================================================


class UserInputsApp:
    def __init__(self, parent, *args, **kwargs):
        df = format_data_headers()
        header_lst = df.columns
        self.user_inputs = []
        self.user_inputs_sel = []
        self.bldg_prefix = ""
        self.myParent = parent

        self.myContainer1 = tk.Frame(parent, relief=tk.SUNKEN, borderwidth=4, *args, **kwargs)
        self.myContainer1.grid(padx=5, pady=5)
        self.myContainer2 = tk.Frame(parent, relief=tk.FLAT, borderwidth=4, *args, **kwargs)
        self.myContainer2.grid(padx=5, pady=5)

        self.label_entry1 = tk.Label(self.myContainer1, text="SAMPLE NAME:", font=font)
        self.label_entry1.grid(row=2, column=0, sticky='nsew')
        self.label_entry2 = tk.Label(self.myContainer1, text="[ BLDG ] _ [ EQUP TYPE ] _ [ EQUP NO. ] _ [ SYS ]",
                                     width=41, font=font)
        self.label_entry2.grid(row=2, column=1, sticky='nsew')

        for idx, text in enumerate(header_lst, 1):
            self.preset = tk.StringVar(root, value=text)
            self.entry2 = tk.Entry(self.myContainer1, width=40, textvariable=self.preset)
            self.entry2.grid(row=idx + 3, column=1, sticky='nsew')
            self.user_inputs.append(self.entry2)

            self.chkValue = tk.IntVar(root, value=1)
            self.chkBtn = tk.Checkbutton(self.myContainer1, text=text, variable=self.chkValue)
            self.chkBtn.grid(row=idx + 3, column=0, sticky='w')
            self.user_inputs_sel.append(self.chkValue)

        self.button2 = tk.Button(self.myContainer2, text="Submit", width=10, font=font,
                                 activebackground='grey', activeforeground='blue')
        self.button2.bind('<Button-1>', self.get_values)
        self.button2.grid(row=0, column=1, sticky='nsew')

        self.button3 = tk.Button(self.myContainer2, text="Close", width=5, font=font)
        self.button3.bind('<Button-1>', self.close_wind)
        self.button3.grid(row=0, column=2, sticky='nsew')

    def get_values(self, event):
        temp_lst_1 = []
        temp_lst_2 = []

        df = format_data_headers().copy()
        formatted_headers_temp = list(df.columns)

        for chkValue in self.user_inputs_sel:
            temp_lst_1.append(chkValue.get())

        for entry in self.user_inputs:
            temp_lst_2.append(entry.get())

        lst_zip = zip(temp_lst_1, temp_lst_2, formatted_headers_temp)
        zipped_list = list(lst_zip)

        i = 0
        while i < len(zipped_list):
            if zipped_list[i][0] == 1:
                revised_headers.append(zipped_list[i][1])
                formatted_headers.append(zipped_list[i][2])
                i += 1
            else:
                i += 1
                pass

        print("ORIGINAL COLUMN NAMES: ")
        print(formatted_headers)
        print("USER DEFINED COLUMN NAMES: ")
        print(revised_headers)
        self.myParent.quit()

    def close_wind(self, event):
        self.myParent.quit()


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title('Header Names')
    root.geometry("500x500")
    UserInputsApp(root)
    root.mainloop()
    root.destroy()


# print()
# print(revised_headers)
# print()


# # ====================================================================================================
# # CHECK FOR MISSING DATA, ANALYZE MISSING DATA & RETURN UPDATED DF WITH NEW HEADER NAMES
# # ====================================================================================================


def consec_miss_data():
    df = format_data_headers()
    df1 = df[formatted_headers]
    df1.columns = revised_headers
    df_md_ind = pd.DataFrame()
    df_md_ind_results = pd.DataFrame()

    counter = 0
    header_main = list(df1.columns)
    header_count = len(df1.columns)

    while counter < header_count:
        lst_temp = []
        df_temp = df1.copy()

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

    # print('CONSECUTIVE MISSING DATA REVIEW COMPLETE')
    return df_md_ind_results, df_md_ind, df1


# print()
# print(consec_miss_data()[2].head())
# print()


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

    # print('EMPTY FIELDS ANALYZED')
    return df_md


# print(analyze_empty_fields().head())
# print()


def merge_df():
    df_md = analyze_empty_fields()
    df_md_ind_results = consec_miss_data()[0]
    # merge dataframe df_md with df_md_ind_results
    df_md_review = pd.merge(df_md_ind_results, df_md, how='inner')

    # print('DATAFRAME MERGE COMPLETE')
    return df_md_review


# print(merge_df().head())
# print()


# # ====================================================================================================
# # FILL EMPTY DATA POINTS WITH VALUES FROM PREVIOUS ROW FOR EACH COLUMN
# # ====================================================================================================


def fill_empty_fields():
    df = consec_miss_data()[2]
    # fill in empty cells through linear interpolation
    df.interpolate(axis=0, method="linear", inplace=True)

    # print('EMPTY FIELDS POPULATED')
    return df.round(2)


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
    df.to_csv(csv_file.replace('.csv', '_OUT_1_Clean_Data.csv'))
    df_md_review.to_csv(csv_file.replace('.csv', '_OUT_2_Missing_Data_Summary.csv'))
    df_md_ind.to_csv(csv_file.replace('.csv', '_OUT_3_Missing_Data_Report.csv'))

    print('RESULTS EXPORTED INTO CSV FILES')
    return


# export_csv()

# # ====================================================================================================
# # >>>END OF SCRIPT<<<
# # ====================================================================================================

# print("\n" + ">>>DATA CLEANING PROCESS COMPLETE!<<<")
# print(">>>TOTAL RUNTIME: %s seconds" % (time.time() - main_start_time).__round__(3))

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


def calc_bldg_load_mbh():
    df = pd.DataFrame(fill_empty_fields())
    results = pd.DataFrame()

    # Todo: establish standard naming scheme for header labels
    results['TIME'] = df['TIME']
    results['HHWS_TEMP'] = df['UVO_HHWS_TEMP']
    results['HHWR_TEMP'] = df['UVO_HHWR_TEMP']
    results['HHWFLOW'] = df['UVO_HHW_RET_FLOW']
    results['CHWS_TEMP'] = df['UVO_CHWS_TEMP']
    results['CHWR_TEMP'] = df['UVO_CHWR_TEMP']
    results['CHWFLOW'] = df['UVO_CHW_RET_FLOW'].str.replace(",", "").astype(float)

    results['HHWMBH'] = abs ((500 * (results['HHWS_TEMP'] - results['HHWR_TEMP'])
                         * results['HHWFLOW'] / 1000).__round__(2) )

    results['CHWMBH'] = abs ((500 * (results['CHWS_TEMP'] - results['CHWR_TEMP'])
                         * results['CHWFLOW'] / 1000).__round__(2) )

    # ToDo need to do the same for chiller water for now

    results.to_csv(csv_file.replace('.csv', '_OUT_0_HHW Calc.csv'))
    return results


tk.messagebox.showinfo('Status', ' Calculation complete!')

print('RESULTS:')
print(calc_bldg_load_mbh().head())

#################################################################################################################
# 4.d : EquipmentDemand Function  right now not utilizing this but this needs to be implemented inside of other chiller adn boiler functions 
## Libraries : Pandas as pd
## Input : LoadProfile, data_path, Equipment
## df variable pulled from calc_bldg_load_mbh function. Returns clean dataset.
## Outputs : EquipmentOutput
print('Running 4.d : EquipmentDemand Function')

LoadProfile = calc_bldg_load_mbh()  # returns dataframe 'df' values

# =============================================================================
# Todo : Unmet hours count , so you can after 10 of unmet hours run at turn done 1 time

# *** Defining the calculation Function ***
def EquipmentDemand(row, title, Equipment):
    title = title
    EquipQuantity = Equipment.quantity
    EquipMax = Equipment.capacityMBH
    EquipTD = Equipment.turndown

    if abs(row[title]) > EquipMax * EquipTD/100:
        EquipmentOut = min(abs(row[title]), EquipMax * EquipQuantity)
    else:
        EquipmentOut = 0

    return EquipmentOut


# =============================================================================
# ***How to call this function ***

##this is a place holder for how we select which column to do calcs on
EquipmentOutput = pd.DataFrame()

# Function Call
EquipmentOutput['TIME'] = LoadProfile['TIME']
EquipmentOutput['EquipmentOutput'] = LoadProfile.apply(EquipmentDemand, title='HHWMBH', axis=1, Equipment=TestBoiler)
## title in the call above is a place holder for how we select which column to do calcs on 

print(EquipmentOutput.head())
print('End of 4.d : EquipmentDemand Function')
print()


#################################################################################################################


#################################################################################################################
# 4.e : Boiler Consumption Function
## Libraries : Pandas as pd
## Input DataPath, EquipmentOutput, Boiler
## Outputs BoilerConsumption

# =============================================================================
# *** Defining the calculation Function ***

def BoilerInput(row, title, Boiler):
    title = title
    BoilerEfficiency = Boiler.efficiency
    return row[title] *100 / BoilerEfficiency 


# =============================================================================
# ***How to call this function ***


BoilerConsumption = pd.DataFrame()
BoilerConsumption['TIME'] = LoadProfile['TIME']
BoilerConsumption['BoilerInput'] = LoadProfile.apply(BoilerInput, title='HHWMBH', axis=1, Boiler=TestBoiler)
## title in the call above is a place holder for how we select which column to do calcs on 

print(BoilerConsumption.head())
print('End of 4.e : BoilerInput Function')
print()

##############################################################################


##############################################################################
# 4.f : Chiller Consumption Function
## Libraries : Pandas as pd, numpy as np, from scipy.optimize import curve_fit
## Input : ChillerPerformance ( tons and kw) and Load.CHWwhihc i called Load_CHW
## Outputs R, ChillerKw
# =============================================================================

# =============================================================================

# =============================================================================
# Method 2 : Calculate the polynomial and sending the polynomial out
# to do : find the R for the fitted curve

def ChillerConsumption(Load, curveTons, curveKws):
    def DefineChillerCurve(curveTons, curveKws):
        curve_coef = np.polyfit(tons, kws, n)
        chillerpoly = np.poly1d(curve_coef)
        return chillerpoly

    ChillerCurve = DefineChillerCurve(curveTons, curveKws)
    return ChillerCurve(Load)


# how to call this function
ChillerKwConsumption = pd.DataFrame()
ChillerKwConsumption['TIME'] = LoadProfile['TIME']
title = 'CHWMBH'  # this is where we select which column to use
ChillerKwConsumption['Chiller_KW'] = pd.DataFrame(ChillerConsumption(LoadProfile[title], curveTons=tons, curveKws=kws))

print(BoilerConsumption.head())
print('End of 4.f : ChillerConsumption Function')
print()



# =============================================================================
##############################################################################
# 4. PUMP POWER CONSUMPTION
##############################################################################

#Have to fix Later
flow = pd.DataFrame(data=LoadProfile['HHWFLOW'])


# =============================================================================

def PumpConsumption(row, pump):
    GPM = pump.MaxGPM
    TD = pump.turndown
    HP = pump.HP
    if row['HHWFLOW'] > (GPM * TD / 100):
        power = ((row['HHWFLOW'] / GPM) ** 3) * HP
    else:
        power = 0
    return power


# output data frame
PumpKw = pd.DataFrame(columns=['Pump Consumption'])

# =============================================================================
# Function Call

PumpKw['Pump Consumption'] = flow.apply(PumpConsumption, axis=1, pump=CHWP1)



# =============================================================================
##############################################################################
# 4.g ELECTRIC COST CALCULATOR
##############################################################################
# 4.g : Electric Cost Calculator Function - @aks
# import pandas as pd
# from pandas import ExcelWriter
# from pandas import ExcelFile
# import numpy as np

# kw data imported fro Tara's section

Energyusage = EquipmentOutput
Energycost = pd.DataFrame(columns=['Costofenergy'])


####################################
# Calculation inside the fuction
#####################################
def Energycalc(Energycost, Energy_usage):
    wb = load_workbook(filename="User Inputs 2.xlsx")
    sheet = wb['Sheet1']

    ##################################SUMMER VALUES #############################

    Summer_start = sheet['AE25'].value
    Summer_end = sheet['AE26'].value
    Summer_superpeak_start = sheet['AE9'].value
    Summer_superpeak_end = sheet['AF9'].value
    Summer_superpeak_cost = sheet['AG9'].value
    Summer_peak_start = sheet['AE10'].value
    Summer_peak_end = sheet['AF10'].value
    Summer_peak_cost = sheet['AG10'].value
    Summer_midpeak_start = sheet['AE11'].value
    Summer_midpeak_end = sheet['AF11'].value
    Summer_midpeak_cost = sheet['AG11'].value
    Summer_base_start = sheet['AE12'].value
    Summer_base_end = sheet['AF12'].value
    Summer_base_cost = sheet['AG12'].value
    Summer_superbase_start = sheet['AE13'].value
    Summer_superbase_end = sheet['AF13'].value
    Summer_superbase_cost = sheet['AG13'].value

    ############################ WINTER VALUES ###################

    Winter_superpeak_start = sheet['AE18'].value
    Winter_superpeak_end = sheet['AF18'].value
    Winter_superpeak_cost = sheet['AG18'].value
    Winter_peak_start = sheet['AE19'].value
    Winter_peak_end = sheet['AF19'].value
    Winter_peak_cost = sheet['AG19'].value
    Winter_midpeak_start = sheet['AE20'].value
    Winter_midpeak_end = sheet['AF20'].value
    Winter_midpeak_cost = sheet['AG20'].value
    Winter_base_start = sheet['AE21'].value
    Winter_base_end = sheet['AF21'].value
    Winter_base_cost = sheet['AG21'].value
    Winter_superbase_start = sheet['AE22'].value
    Winter_superbase_end = sheet['AF22'].value
    Winter_superbase_cost = sheet['AG22'].value

    # #Summer_start, Summer_end = input("Enter Summer start and end months").split()
    # Summer_superpeak_start, Summer_superpeak_end, Summer_superpeak_cost = input("Enter Summer superpeak start hour, end hour and Cost per kwh respectively").split()
    # Summer_peak_start, Summer_peak_end, Summer_peak_cost = input("Enter Summer peak start hour, end hour and Cost per kwh respectively").split()
    # Summer_midpeak_start, Summer_midpeak_end, Summer_midpeak_cost = input("Ener Summer midpeak start hour, end hour and Cost per kwh respectively").split()
    # Summer_base_start, Summer_base_end, Summer_base_cost = input("Enter summer Base start hour, end hour and Cost per kwh respectively").split()
    # Summer_superbase_start, Summer_superbase_end, Summer_superbase_cost = input("Enter summer Superbase start hour, end hour and Cost per kwh respectively").split()
    # # WINTER IS COMING##########
    # Winter_superpeak_start, Winter_superpeak_end, Winter_superpeak_cost = input("Enter Winter superpeak start hour, end hour and Cost per kwh respectively").split()
    # Winter_peak_start, Winter_peak_end, Winter_peak_cost = input("Enter Winter peak start hour, end hour and Cost per kwh respectively").split()
    # Winter_midpeak_start, Winter_midpeak_end, Winter_midpeak_cost = input("Ener Winter midpeak start hour, end hour and Cost per kwh respectively").split()
    # Winter_base_start, Winter_base_end, Winter_base_cost = input("Enter Winter Base start hour, end hour and Cost per kwh respectively").split()
    # Winter_superbase_start, Winter_superbase_end, Winter_superbase_cost = input("Enter Winter Superbase start hour, end hour and Cost per kwh respectively").split()

    # TRANSFER TDM DATA TO VARIABLES

    Time = Energyusage['Time'].dt.hour
    Day = Energyusage['Time'].dt.day
    Month = Energyusage['Time'].dt.month

    ##############SUMMER CALC#################

    if (Month >= Summer_start and Month <= Summer_end and Month <= 12 and Day >= 0 and Day <= 5):

        if (Time >= Summer_superpeak_start and Time >= Summer_superpeak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Summer_superpeak_cost

        elif (Time >= Summer_peak_start and Time <= Summer_peak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Summer_peak_cost

        elif (Time >= Summer_midpeak_start and Time <= Summer_midpeak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Summer_midpeak_cost

        elif (Time >= Summer_base_start and Time <= Summer_base_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Summer_base_cost

        elif (Time >= Summer_superbase_start and Time <= Summer_superbase_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Summer_superbase_cost

        else:
            print("Re-Enter values between 0-24 Error in summer months")

    ###############################################################################################################
    ###############   WINTER CALC ##########################
    ####################################################################################################
    elif (Month < Summer_start and Month > Summer_end and Month <= 12 and Day >= 0 and Day <= 5):

        if (Time >= Winter_superpeak_start and Time >= Winter_superpeak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Winter_superpeak_cost

        elif (Time >= Winter_peak_start and Time <= Winter_peak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Winter_peak_cost

        elif (Time >= Winter_midpeak_start and Time <= Winter_midpeak_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Winter_midpeak_cost

        elif (Time >= Winter_base_start and Time <= Winter_base_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Winter_base_cost

        elif (Time >= Winter_superbase_start and Time <= Winter_superbase_end):
            Energyusage['Cost'] = Energyusage['Energy'] * Winter_superbase_cost

        else:
            print("Re-Enter values between 0-24, Error in Winter months months")

    ########################################## SUMMER WEEKENDS ###################################

    elif (Day >= 6 and Day <= 7 and Month >= Summer_start and Month <= Summer_end and Month <= 12):

        Energyusage['Cost'] = Energyusage['Energy'] * Summer_base_cost

    ################### WINTER WEEKENDS #########################################################

    elif (Day >= 6 and Day <= 7 and Month < Summer_start and Month > Summer_end and Month <= 12):

        Energyusage['Cost'] = Energyusage['Energy'] * Summer_base_cost


#############################################################################################

####################################
# End of Fucntion
#####################################

# calling the function
Energycost.apply(Energycalc, axis=1, Energy_usage=Energyusage)

# export results to csv format
Energycost.to_csv('Costofenergy.csv')

#################### TOTAL ENERGY USAGE FOR THE YEAR ##################
#Annual_cost = Energycost['Costofenergy'].sum()
#Min_cost = Energycost['Costofenergy'].min()
#Max_cost = Energycost['Costofenergy'].max()

# print(Annual_cost, ' is the ANNUAL cost of electricity')
# print(Min_cost, ' is the MINIMUM cost of energy for the timestamp')
# print(Max_cost, ' is the MAXIMUM cost of energy for the timestamp')
print('End of 4.g : Electric Cost Calculator Function')
# print()

##############################################################################
# 4.h: Gas Cost Calculator FUnction
## Input
## Outputs
##############################################################################


##############################################################################
# 4.i : Carbon Calculator Function - @ate
## Input values from Excel: Date/Time, HHW info (values from Excel), emission_factor_kwh, emission_factor_therm
## Other Inputs: ChillerKwConsumption (dataframe, calculated above), openpyxl package needed
## Outputs: Annual carbon emissions (lbs of CO2)

# EIA data: 1.17 lbCO2/therm, 0.92 lbCO2/kWh
# Source: https://www.eia.gov/environment/emissions/co2_vol_mass.php
# Source: https://www.eia.gov/tools/faqs/faq.php?id=74&t=11

def normalization_therm():
    df = pd.read_csv('2019 CHP Raw Trend.csv')  # Comment out if already called out above
    time = df['Time'].astype('datetime64[ns]')
    delta_time = (time.max() - time.min()).days + 1
    HHWST = df['CHP HHWS Temp']
    HHWRT = df['CHP HHWR Temp']
    CHPF = df['CHP Flow']
    BoilerMBH = (
                            HHWST - HHWRT) * CHPF / 1000 / .80  # 80% efficiency placeholder, update to reference user defined value
    total_BoilerMBH = BoilerMBH.sum()
    BoilerAnnualTherms = (total_BoilerMBH / delta_time) * 365
    return BoilerAnnualTherms


def normalization_kWh():
    df = pd.read_csv('2019 CHP Raw Trend.csv')  # Comment out if already called out above
    time = df['Time'].astype('datetime64[ns]')
    delta_time = (time.max() - time.min()).days + 1
    ChillerAnnualkWh = ChillerKwConsumption.sum() / delta_time * 365
    return ChillerAnnualkWh


def carbon_calculator():
    from openpyxl import load_workbook
    wb = load_workbook(filename="User Inputs.xlsx")
    sheet = wb['Sheet1']
    emission_factor_kwh = sheet['AF5'].value  # does not work if cell is blank, add if loop w/0.92 lbCO2/kWh
    emission_factor_therm = sheet['Z4'].value  # does not work if cell is blank, add if loop w/1.17 lbCO2/therm
    ChillerAnnualkWh = ChillerKwConsumption.sum()  # Update to use normalization function in future
    co2_gas = BoilerAnnualTherms * emission_factor_therm
    co2_elec = ChillerAnnualkWh * emission_factor_kwh
    total_carbon = (co2_elec + co2_gas).__round__(1)
    # print('Amount of CO2 emitted per year is', (total_carbon),'lbs')
    return total_carbon


##############################################################################

# PLOTTING FUNCTIONS BELOW MAY BE DEPRECATED - see eatlib.py for most current plotting functions
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


plot_x(BoilerConsumption)
##############################################################################
# 4.l : Distribution Energy Consumption
## Libraries : Pandas as pd
## Input : Pumps information {quantity, hp, MaxGPM, turndown, efficiency, *config }
## Outputs PumpKw


# =============================================================================

# =============================================================================

