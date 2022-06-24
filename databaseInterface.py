'''
Interface to the AWS RDS MySQL database.
createDatabase() has already been run and does not need to again
'''

import pymysql
import logging

# Connects to the AWS RDS database
db = pymysql.connect(host='database-1.c7gcexcv61xq.us-west-1.rds.amazonaws.com', 
                     port=3306, 
                     user='admin', 
                     password='Password123!', 
                     db='weather_data')
cursor = db.cursor()

# Creates the MySQL database and the weather table
# Should only be used once for initial database set up
def createDatabase():
    sql = '''create database weather_data'''
    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        logging.error('Failed to create weather_data database')

    sql = '''
        CREATE TABLE weather (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        latitude TEXT,
        longitude TEXT,
        max_temp_f FLOAT,
        min_temp_f FLOAT,
        total_rain_in FLOAT,
        total_snow_in FLOAT)      
        '''
    try:
        cursor.execute(sql)
    except:
        logging.error('Failed to create weather table in database')
    return

# Inserts pre-cleaned weather data into weather table
# Takes in a tuple containing each value in order
def insertWeatherData(data):
    date, latitude, longitude, max_temp_f, min_temp_f, total_rain_in, total_snow_in = data
    sql = '''
        INSERT INTO weather(date, latitude, longitude, max_temp_f, min_temp_f, total_rain_in, total_snow_in)
        VALUES(STR_TO_DATE('%s', '%%Y-%%m-%%d'), %s, %s, %s, %s, %s, %s)
        ''' % (date, latitude, longitude, max_temp_f, min_temp_f, total_rain_in, total_snow_in)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        logging.error('Failed to insert weather data into database')
    return

# Returns all data from the weather table
# Used for testing
def getAllData():
    output = None
    try:
        sql = '''SELECT * FROM weather'''
        cursor.execute(sql)
        output = cursor.fetchall()
    except:
        logging.error('Failed to get data from database')
    return output
