# ====================================================================================================
# Author:         Jonathan Herrera
# Created on:     July 3, 2020
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


# def main():
#     open_csv_file()
#     read_csv()
#     format_data_headers()
#     user_inputs_2()
#     consec_miss_data()
#     analyze_empty_fields()
#     merge_df()
#     fill_empty_fields()
#     export_csv()


# ====================================================================================================
# begin tracking overall runtime
main_start_time = time.time()
print("\n" + 'Data cleaning in process...')

# ====================================================================================================
# DEFINE CSV FUNCTION
# ====================================================================================================
file_open_title = "Select Raw CSV File"


def open_csv_file():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('CSV', '*.csv')], title=file_open_title)
    print("\n" + "     FILE LOADED: " + file_path)
    return file_path


# ====================================================================================================
# PROMPT USER TO SPECIFY CSV FILE & ANALYZE FILE CONTENTS
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

    # get total number of columns
    header_count = len(df.columns)
    # get total number of rows
    data_body_count = len(df)

    # remove any trailing spaces
    df.columns = df.columns.str.strip()
    # replace spaces " " with an "_"
    df.columns = df.columns.str.replace(' ', '_')
    # make all header names uppercase
    df.columns = df.columns.str.upper()

    print('>>>HEADERS FORMATTED')
    print()
    return df


# print(format_data_headers().head())

# ====================================================================================================
# STANDARDIZE HEADER NAMES VIA USER INPUT
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

        # self.label_entry = tk.Label(self.myContainer1, text="BLDG PREFIX:", width=25, font=font)
        # self.label_entry.grid(row=1, column=0, sticky='e')

        self.label_entry2 = tk.Label(self.myContainer1, text="[ BLDG ] _ [ EQUP TYPE ] _ [ EQUP NO. ] _ [ SYS ]",
                                     width=41, font=font)
        self.label_entry2.grid(row=2, column=1, sticky='nsew')

        # self.entry1 = tk.Entry(self.myContainer1, width=20)
        # self.entry1.grid(row=1, column=1, sticky='nsew')
        # self.user_inputs.append(self.entry1)

        for idx, text in enumerate(header_lst):
            self.label2 = tk.Label(self.myContainer1, text=text, width=25, font=font)
            self.label2.grid(row=idx + 3, column=0, sticky='e')

            self.entry2 = tk.Entry(self.myContainer1, width=40)
            self.entry2.grid(row=idx + 3, column=1, sticky='nsew')
            self.user_inputs.append(self.entry2)

        # self.button1 = tk.Button(self.myContainer2, text='Clear All', width=10, font=font,
        #                          activebackground='grey', activeforeground='blue')
        # self.button1.bind('<Button-1>', self.clear_values)
        # self.button1.grid(row=0, column=0, sticky='nsew')

        self.button2 = tk.Button(self.myContainer2, text="Submit", width=10, font=font,
                                 activebackground='grey', activeforeground='blue')
        self.button2.bind('<Button-1>', self.get_values)
        self.button2.grid(row=0, column=1, sticky='nsew')

        self.button3 = tk.Button(self.myContainer2, text="Close", width=5, font=font)
        self.button3.bind('<Button-1>', self.close_wind)
        self.button3.grid(row=0, column=2, sticky='nsew')

    def clear_values(self, event):
        self.entry2.delete(first=0, last=50)

    def get_values(self, event):
        for entry in self.user_inputs:
            user_inputs_2(entry.get())
            print(entry.get())
        self.myParent.quit()

    def close_wind(self, event):
        self.myParent.quit()


def user_inputs_2():  # def user_inputs_2(user_inputs)
    global revised_headers
    revised_headers.append(user_inputs)
    return revised_headers


if __name__ == "__main__":
    root = tk.Tk()
    user_inputs = []
    root.wm_title('Header Names')
    root.geometry("500x400")
    UserInputsApp(root)
    root.mainloop()
    root.destroy()


# ==== TEMP ==== REMOVE '#' ONCE READY TO PASS revised_headers
# df.columns = revised_headers
# # remove any trailing spaces
# df.columns = df.columns.str.strip()
# # replace spaces " " with an "_"
# df.columns = df.columns.str.replace(' ', '_')
# # make all header names uppercase
# df.columns = df.columns.str.upper()
# ==== TEMP ====


# # ====================================================================================================
# # CHECK FOR MISSING DATA
# # ====================================================================================================


def consec_miss_data():
    df = format_data_headers()
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
    return df_md_ind_results, df_md_ind


# print(consec_miss_data())


def analyze_empty_fields():
    df = format_data_headers()
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


# print(analyze_empty_fields())


def merge_df():
    df_md = analyze_empty_fields()
    df_md_ind_results = consec_miss_data()[0]
    # merge dataframe df_md with df_md_ind_results
    df_md_review = pd.merge(df_md_ind_results, df_md, how='inner')

    print('DATAFRAME MERGE COMPLETE')
    return df_md_review


# print(merge_df())


def fill_empty_fields():
    df = format_data_headers()
    # allowable_missing_data = 20
    # fill in cells with missing data with value from previous row
    df.fillna(axis=0, method='ffill', inplace=True)  # , limit=allowable_missing_data)
    #TODO: Use average values. Use last known value in any given column and the next
    #TODO: available value to obtain avg values to fill in gaps with

    print('EMPTY FIELDS POPULATED')
    return df


# print(fill_empty_fields())

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


print("\n" + ">>>PROCESS COMPLETE!<<<")
print(">>>TOTAL RUNTIME: %s seconds" % (time.time() - main_start_time).__round__(3))

# alert user upon successful completion
tk.messagebox.showinfo('Status', 'Data Cleaning Process Complete!')

# ====================================================================================================
# >>>END OF DATA CLEANING SCRIPT<<<
# ====================================================================================================
# if __name__ == "__main__":
#     main()