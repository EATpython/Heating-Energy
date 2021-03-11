# WORKING - Finding latest, oldest, and delta between dates from data set
# Update to reference the raw data file being used and references to the data via headers
# NOT WORKING - calculating the therms from data (need to skip first row)
import pandas as pd

df = pd.read_csv('2019 CHP Raw Trend.csv')
time = df['Time'].astype('datetime64[ns]')
# print(time)
print("Oldest date is ", time.min())
print("Latest date is ", time.max())
delta_time = time.max() - time.min()
print(delta_time)


# DOES NOT WORK - Calculating therms from HHWST, HHWRT, and Flow
therm = df[('CHP HHWS Temp' - 'CHP HHWR Temp')*'CHP Flow'*.005]
print(therm.sum())



# Calculations - normalize (therm/day), then typical annual usage (therm/year); need to fix above section
therm_per_day = total / delta_days
annual_therm = therm_per_day * 365
print(therm_per_day)
print(annual_therm)

# Location in SoCalGas territory, use EIA data: Emission factor = 53.07 kgCO2/MMBtu, MMBtu = 10 therm; #
# Source: https://www.eia.gov/environment/emissions/co2_vol_mass.php
# https://www.socalgas.com/regulatory/documents/a-16-12-010/SCG-CIP-Rebuttal-Testimony-A1612010-2017-11-03%20Final.pdf
# Location not in SoCalGas territory, use Energy Star data: Emission factor = 53.11 kgCO2/MMBtu, MMBtu = 10 therm
# https://portfoliomanager.energystar.gov/pdf/reference/Emissions.pdf

emission_factor = 53.07  # kgCO2/MMBtu, where MMBtu = 1,000,000 Btu = 10 therm
carbon_emission = annual_therm * emission_factor * 10
print('Amount of CO2 emitted per year is ', carbon_emission, ' kgCO2/MMBtu.')