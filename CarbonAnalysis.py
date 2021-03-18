import pandas as pd # Comment out once merged into "heat-calc.py" file


# ======
# # Calculating total time - create function "data_normalization"
# df = pd.read_csv('2019 CHP Raw Trend.csv') # Comment out once merged into "heat-calc.py" file
# time = df['Time'].astype('datetime64[ns]')
# print("Oldest date is ", time.min())
# print("Latest date is ", time.max())
# delta_time = (time.max() - time.min()).days
# print('Number of days is', delta_time)
#
# # Calculating total therms - Tara/Jonathan already calculated this value, revise to reference
# HHWST = df['CHP HHWS Temp']
# HHWRT = df['CHP HHWR Temp']
# CHPF = df['CHP Flow']
# BoilerMBH = (HHWST - HHWRT) * CHPF / 1000 / .85 # Assuming 85% efficiency, placeholder for user input
# total_BoilerMBH = BoilerMBH.sum()
# print('Total MBH from data is ', total_BoilerMBH)
# # Include kWh usage and convert to MBH (1,000 Btu)
#
# # Normalizing usage to represent 1 year (365 days)
# annual_therm = (total_BoilerMBH / delta_time) * 365
# ======

# Location in SoCalGas territory, use EIA data: Emission factor = 53.07 kgCO2/MMBtu, MMBtu = 10 BoilerMBH
# Source: https://www.eia.gov/environment/emissions/co2_vol_mass.php
# https://www.socalgas.com/regulatory/documents/a-16-12-010/SCG-CIP-Rebuttal-Testimony-A1612010-2017-11-03%20Final.pdf
# Location not in SoCalGas territory, use Energy Star data: Emission factor = 53.11 kgCO2/MMBtu, MMBtu = 10 BoilerMBH
# https://portfoliomanager.energystar.gov/pdf/reference/Emissions.pdf

BoilerAnnualTherms = 500 # variable from 4.e : Boiler Consumption Function, 5000 is placeholder
ChillerKwConsumption = 250000 # variable from 4.f : Chiller Consumption Function, 250000 is placeholder; use .sum() if dataframe

# Calculating emissions - create a function "carbon_calculator"
emission_factor_kwh = 53.07 * 3.41214 / 1000  # kgCO2/MMBtu, where MMBtu = 1,000,000 Btu = 10 therms;  1 kWh = 3412.14 Btu
emission_factor_therm = 5.307
# change emission_factor_kwh and emission factor_therm to user input from excel
co2_gas = BoilerAnnualTherms * emission_factor_therm
co2_elec = ChillerKwConsumption * emission_factor_kwh
total_carbon = (co2_elec + co2_gas).__round__(1)
print('Amount of CO2 emitted per year is', total_carbon, 'kg or', (total_carbon*2.204).__round__(1),'lbs')