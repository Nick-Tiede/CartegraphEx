'''
Extracts data from the Timeline Weather API from https://www.visualcrossing.com/weather-api

*This API allows queries that can clean and format the data, however I chose to retrieve 
their standard settings to better show the automation and ETL process.
'''
import urllib.error
import urllib.request
import csv
import codecs
import pandas as pd

from pymysql import NULL

# Returns latitude and longitude values from cfg.txt
def getCoordinates():
    with open('cfg.txt') as text:
        strCoords = text.readline().rstrip()
    latitude, longitude = eval(strCoords)
    return str(latitude), str(longitude)

# Returns dataframe of today's raw weather data
def getDailyWeather():
    df = NULL
    try: 
        latitude, longitude = getCoordinates()
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+latitude+"%2C%20"+longitude+"/today?unitGroup=metric&include=days&key=P453U46BWCHGSJWZACMLF3HNB&contentType=csv"
        ResultBytes = urllib.request.urlopen(url)
        data = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        header = data.__next__()
        df = pd.DataFrame(data, columns=header)
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode() 
        print('Error code: ', e.code, ErrorInfo)
    return df

# Returns dataframe of fake raw weather data for testing
def getTestDailyWeather():
    return pd.read_csv('fakeAPIQueryCSV.csv')
