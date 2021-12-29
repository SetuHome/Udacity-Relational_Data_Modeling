'''This python file basically deals with extracting data from the json files provided as part of the project work, and load the data in 
 postgres sql tables created.
'''

#Importing Different Packages as required in the project
from io import DEFAULT_BUFFER_SIZE
import os
import sys
import psycopg2
import pandas as pd
import json
import glob
from array import *
from sql_queries_prj import *
import datetime
import numpy as np

def main():
    #The function below establishes the connection with the database
    curr, conn = create_connection()
    
    # Calling functions to process and insert song and log data
    songs_data_insert(curr, conn, songdatafilepath, func = process_song_data)
    logs_data_insert(curr, conn, logdatafilepath, func = process_log_file_data)
    #Calling a function to close the connection with the database
    close_connection(curr, conn)

#Conection creation with the database
def create_connection():
    try:
        conn = psycopg2.connect("host=localhost dbname=sparkifydb user=s0k01c6 password=SetuHome")
        curr = conn.cursor()
        conn.set_session(autocommit = True)
        print("Connection establshed successfully")
        return curr, conn
    except psycopg2.Error as e:
        print("Error: Could not conenct to the database mentioned")
        print(e)

# Code to retrieve all .json files present under the spcified path
def getallfiles(filepath):
        all_files = []
        for root, dir, files in os.walk(filepath):
            files = glob.glob(os.path.join(root,'*.json'))
            for f in files:
                all_files.append(os.path.abspath(f))
        return all_files

# Code to start the processing and inserting song data 
def songs_data_insert(curr, conn, songdatafilepath, func):
    print(songdatafilepath)
    
    # Truncating song and artists table before loading the data
    curr.execute (songs_data_truncate_query)
    curr.execute (artists_data_truncate_query)

    # To get the details of all files in a list with absolute path
    song_data_files = getallfiles(songdatafilepath)

    # To get the length of list in song_data_files
    filedata = len(song_data_files)
    print("The length of the song list is: {} and found at the path {}".format(filedata,songdatafilepath))

    # Processing song data by iterating over files and process.
    for i, filepath in enumerate(song_data_files):
        func(curr,filepath)
        

def logs_data_insert(curr, conn, logdatafilepath, func):
    print(logdatafilepath)
    
    #Truncating users, time and songplays tables before loading the data
    curr.execute(users_data_truncate_query)
    curr.execute(time_data_truncate_query)
    curr.execute(songplays_data_truncate_query)

    #To get the details of all files in a list with absolute path
    log_data_files = getallfiles(logdatafilepath)

    #To get the length of the list in log data files
    filedata = len(log_data_files)
    print("The length of the log list is: {} and found at the path {}".format(filedata,logdatafilepath))

    #Processing log data by iterating over files and process.
    for i, filepath in enumerate(log_data_files):
        func(curr,filepath)



def process_song_data(curr,filepath):
    
    # Code to read json files specidied in the variable filepath 
    songdf = pd.read_json(filepath,lines=True)
    
    # Code to frame the list from given dataframe for songs table
    songdatafile = songdf[['song_id','title','artist_id','year','duration']].values.tolist()
    #Iterating over the list data to insert records in songs table
    for songrow in songdatafile:
        curr.execute(songs_data_insert_query,songrow)
    
    # Code to frame the list from given dataframe for artists table
    artistdatafile = songdf[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values.tolist()
    #Iterating over the list data to insert records in artists table
    for artistrow in artistdatafile:
        curr.execute(artists_data_insert_query,artistrow)


def process_log_file_data(curr, filepath):

    # Code to read json files specidied in the variable filepath 
    logdf = pd.read_json(filepath,lines=True)
    
    #Code to Insert users data to the table
    # Code to frame the list from given dataframe for users table
    userdf = logdf[['userId','firstName','lastName','gender','level']].values.tolist()
    #Iterating over the list data to insert records in users table
    for userdatafiles in userdf:
        curr.execute(users_data_insert_query,userdatafiles)
    
    #Code to Insert time data to the table
    # Code to frame the list from given dataframe for time table
    df = pd.to_numeric(logdf["ts"])
    x = np.array(df)
    y = x.astype(int)
    for i in y:
        dt = datetime.datetime.fromtimestamp(i / 1000.0)
        year = dt.year
        month = dt.month
        hour = dt.hour
        day = dt.day
        weekday = dt.weekday()
        week = datetime.date(year,month,day).isocalendar().week
        timedatalist = [dt,hour,day,week,month,year,weekday]
        curr.execute(time_data_insert_query,timedatalist)
    print("time table data insertion successful")

    # Code to Insert songplays data to the table
    # Code to frame the list from given dataframe for songplays table
    for index, row in logdf.iterrows():
        #Code to fetch song_id and artist_id based on value of song, artist and length of song      
        curr.execute(song_data_select,(row.song, row.artist, row.length))
        results = curr.fetchone()
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None
        
        #Code to create the list for inserting data to songplays table
        songplaylist = [datetime.datetime.fromtimestamp((row.ts)/1000.0),row.userId,row.level,row.sessionId,row.location,row.userAgent]
        #Code to append song_id and artist_id values in the list
        songplaylist.insert(4,song_id)
        songplaylist.insert(5,artist_id)
        #Code to insert data to songplays table
        curr.execute(songplays_data_insert_query,songplaylist)


def close_connection(curr, conn):
    curr.close()
    conn.close()

# Creating the main function for the python program
if __name__ == "__main__":
    #Assigning file path name for song and log data
    songdatafilepath = '/Users/s0k01c6/Documents/MyGitRepos/Udacity-Relational_Data_Modeling/data/song_data'
    logdatafilepath = '/Users/s0k01c6/Documents/MyGitRepos/Udacity-Relational_Data_Modeling/data/log_data'
    main()
         