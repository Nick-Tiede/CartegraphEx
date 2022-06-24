'''
Transforms raw data to a useable format
'''

from datetime import datetime
import pandas as pd

# Converts temperature in Celsius to Fahrenheit
def convertCtoF(tempC):
    return (1.8 * tempC) + 32

# Converts length in centimeters to inches
def convertCentimetertoInch(lengthC):
    return 0.3937 * lengthC

# Transforms raw dataframe into final weather data tuple 
def transformWeatherData(dfRaw):
    df = pd.DataFrame(dfRaw, columns=['name', 'datetime', 'tempmax', 'tempmin', 'precip', 'snowdepth'])
    date = df.loc[0, 'datetime']
    latitude, longitude = eval(df.loc[0, 'name'])
    max_temp_f = convertCtoF(float(df.loc[0, 'tempmax']))
    min_temp_f = convertCtoF(float(df.loc[0, 'tempmin']))
    total_rain_in = convertCentimetertoInch(float(df.loc[0, 'precip']))
    total_snow_in = convertCentimetertoInch(float(df.loc[0, 'snowdepth']))
    return str(date), str(latitude), str(longitude), float(max_temp_f), float(min_temp_f), float(total_rain_in), float(total_snow_in)