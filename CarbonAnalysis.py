# WORKING - Finding latest, oldest, and delta between dates from data set
import pandas as pd

df = pd.read_csv(r'input.csv')
df['Start'] = df['Start'].astype('datetime64[ns]')
df['End'] = df['End'].astype('datetime64[ns]')

latest = df.End.max()
oldest = df.Start.min()
delta_days = (df.Start.max() - df.End.min()).days

print("Latest date: ", latest)
print("Oldest date:", oldest)
print("Number of days between:", delta_days)

# DOES NOT WORK - Calculating total usage from "Usage" column.
therm = pd.read_csv(r'input.csv')
next(therm) # <-- troubleshoot here; meant to skip first row (header) before iterating
total = 0
for row in therm:
   total += float(row[2])
   print("Total usage witin billing period is ", total)


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

emission_factor = 53.07 # kgCO2/MMBtu, where MMBtu = 10 therm
carbon_emission = annual_therm * emission_factor * 10
print('Amount of CO2 emitted per year is ', carbon_emission, ' kgCO2/MMBtu.')