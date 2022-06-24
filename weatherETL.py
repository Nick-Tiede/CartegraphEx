'''
Runs entire ETL process of retrieving weather data from API, 
tranforming it to a better format, then loading it in the database

'''

from databaseInterface import getAllData, insertWeatherData
from extract import getDailyWeather, getTestDailyWeather
from transform import transformWeatherData


def runWeatherETL():
    #dfRaw = getTestDailyWeather()
    dfRaw = getDailyWeather()
    if dfRaw is not None:    
        transformedData = transformWeatherData(dfRaw)
        insertWeatherData(transformedData)


runWeatherETL()
#print(getAllData())