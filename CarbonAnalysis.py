# EIA data: 1.17 lbCO2/therm, 0.92 lbCO2/kWh
# Source: https://www.eia.gov/environment/emissions/co2_vol_mass.php
# Source: https://www.eia.gov/tools/faqs/faq.php?id=74&t=11

import pandas as pd  # Comment out once merged into "_P2S_EAT_LIBRARY.py" file

BoilerAnnualTherms = 500  # variable from 4.e : Boiler Consumption Function, 5000 is placeholder
ChillerKwConsumption = 250000  # variable from 4.f : Chiller Consumption Function, 250000 is placeholder; use .sum() if dataframe

def normalization_therm():
  df = pd.read_csv('2019 CHP Raw Trend.csv') # Comment out if already called out above
  time = df['Time'].astype('datetime64[ns]')
  delta_time = (time.max() - time.min()).days + 1
  HHWST = df['CHP HHWS Temp']
  HHWRT = df['CHP HHWR Temp']
  CHPF = df['CHP Flow']
  BoilerMBH = (HHWST - HHWRT) * CHPF / 1000 / .80 # 80% efficiency placeholder, update to reference user defined value
  total_BoilerMBH = BoilerMBH.sum()
  BoilerAnnualTherms = (total_BoilerMBH / delta_time) * 365
  return BoilerAnnualTherms

def normalization_kWh():
  df = pd.read_csv('2019 CHP Raw Trend.csv') # Comment out if already called out above
  time = df['Time'].astype('datetime64[ns]')
  delta_time = (time.max() - time.min()).days + 1
  ChillerAnnualkWh = ChillerKwConsumption.sum() / delta_time * 365
  return ChillerAnnualkWh

def carbon_calculator():
  from openpyxl import load_workbook
  wb = load_workbook(filename="User Inputs.xlsx")
  sheet = wb['Sheet1']
  emission_factor_kwh = sheet['AF5'].value # does not work if cell is blank, add if loop w/0.92 lbCO2/kWh
  emission_factor_therm = sheet['Z4'].value # does not work if cell is blank, add if loop w/1.17 lbCO2/therm
  ChillerAnnualkWh = ChillerKwConsumption#.sum() # Update to use normalization function in future
  co2_gas = BoilerAnnualTherms * emission_factor_therm
  co2_elec = ChillerAnnualkWh * emission_factor_kwh
  total_carbon = (co2_elec + co2_gas).__round__(1)
  # print('Amount of CO2 emitted per year is', (total_carbon),'lbs')
  return total_carbon

carbon_calculator()