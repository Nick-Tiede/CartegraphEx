'''
Runs entire ETL process of retrieving weather data from API, 
tranforming it to a better format, then loading it in the database

'''

from databaseInterface import getAllData, insertWeatherData
from extract import getDailyWeather, getTestDailyWeather
from transform import transformWeatherData
import logging


def runWeatherETL():
    #dfRaw = getTestDailyWeather()
    dfRaw = getDailyWeather()
    if dfRaw is not None:    
        try:
            transformedData = transformWeatherData(dfRaw)
        except:
            logging.error('Failed to transform raw weather data')
        try:
            insertWeatherData(transformedData)
        except:
            logging.error('Failed to connect to or interact with database')
    else:
        logging.error('No data has been extracted')


runWeatherETL()
#print(getAllData())