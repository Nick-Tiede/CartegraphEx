'''


'''

from databaseInterface import insertWeatherData
from extract import getDailyWeather
from transform import transformWeatherData


def runWeatherETL():
    dfRaw = getDailyWeather()    
    transformedData = transformWeatherData(dfRaw)
    #insertWeatherData(transformedData)


runWeatherETL()