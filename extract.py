'''
Extracts data from the Timeline Weather API from https://www.visualcrossing.com/weather-api

*This API allows queries that can clean and format the data, however I chose to retrieve 
their standard settings to better show the automation and ETL process.
'''

import os
import sys
import urllib.error
import urllib.request
import csv
import codecs
import pandas as pd
import logging

# Returns latitude and longitude values from cfg.txt
def getCoordinates():
    latitude, longitude = None, None
    try:
        with open(os.path.join(sys.path[0], 'cfg.txt')) as text:
            strCoords = text.readline().rstrip()
        latitude, longitude = eval(strCoords)
    except:
        logging.error('Unable to get coordinates from cfg file')
        sys.exit()
    return str(latitude), str(longitude)

# Returns dataframe of today's raw weather data
def getDailyWeather():
    df = None
    # Weather API website generated query that has been edited
    try: 
        latitude, longitude = getCoordinates()
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+latitude+"%2C%20"+longitude+"/today?unitGroup=metric&include=days&key=P453U46BWCHGSJWZACMLF3HNB&contentType=csv"
        ResultBytes = urllib.request.urlopen(url)
        data = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        header = data.__next__()
        df = pd.DataFrame(data, columns=header)
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode() 
        logging.error('Failed to connect to Weather API: Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode() 
        logging.error('Failed to connect to Weather API: Error code: ', e.code,ErrorInfo)
        sys.exit()
    return df

# Returns dataframe of fake raw weather data for testing
def getTestDailyWeather():
    df = None
    try:
        df = pd.read_csv(os.path.join(sys.path[0], 'fakeAPIQueryCSV.csv'))
    except:
        logging.error('Unable to read fake API data')
    return df
