'''This python file basically deals with extracting data from the json files provided as part of the project work, and load the data in 
 postgres sql tables created.
'''

#Importing Different Packages as required in the project
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
    #The function below establishes the connection
    curr, conn = create_connection()

    #songs_data_insert(curr, conn, songdatafilepath, func = process_song_data)
    logs_data_insert(curr, conn, logdatafilepath, func = process_log_file_data)


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

def getallfiles(filepath):
        all_files = []
        for root, dir, files in os.walk(filepath):
            files = glob.glob(os.path.join(root,'*.json'))
            for f in files:
                all_files.append(os.path.abspath(f))
        return all_files

def songs_data_insert(curr, conn, songdatafilepath, func):
    print(songdatafilepath)
    # Truncating tables before loading the data
    curr.execute (songs_data_truncate_query)
    curr.execute (artists_data_truncate_query)
    # To get the details of all files in a list
    song_data_files = getallfiles(songdatafilepath)
    # To get the length of list in song_data_files
    filedata = len(song_data_files)
    print("The length of the song list is: {} and found at the path {}".format(filedata,songdatafilepath))

    # Processing song data by iterating over files and process.
    for i, filepath in enumerate(song_data_files):
        #print(i , filepath)
        func(curr,filepath)
        

def logs_data_insert(curr, conn, logdatafilepath, func):
    print(logdatafilepath)
    #Truncating the tables before loading the data
    curr.execute(users_data_truncate_query)
    curr.execute(time_data_truncate_query)
    curr.execute(songplays_data_truncate_query)
    #To get the details of all files in a list
    log_data_files = getallfiles(logdatafilepath)
    #To get the length of the list in log data files
    filedata = len(log_data_files)
    print("The length of the log list is: {} and found at the path {}".format(filedata,logdatafilepath))

    #Processing log data by iterating over files and process.
    for i, filepath in enumerate(log_data_files):
        func(curr,filepath)



def process_song_data(curr,filepath):

    songdf = pd.read_json(filepath,lines=True)
    songdatafile = songdf[['song_id','title','artist_id','year','duration']].values.tolist()
    for songrow in songdatafile:
        curr.execute(songs_data_insert_query,songrow)
    
    artistdatafile = songdf[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values.tolist()
    for artistrow in artistdatafile:
        curr.execute(artists_data_insert_query,artistrow)


def process_log_file_data(curr, filepath):
    logdf = pd.read_json(filepath,lines=True)
    
    '''
    #Inserting users data to the table

    userdf = logdf[['userId','firstName','lastName','gender','level']].values.tolist()
    for userdatafiles in userdf:
        curr.execute(users_data_insert_query,userdatafiles)
    
    #Inserting time data to the table
    
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
    print("time table data insertion successful")'''

    #Inserting songplays data to the table
    for index, row in logdf.iterrows():
        curr.execute(song_data_select)
        results = curr.fetchone()
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None
        
        songplaylist = logdf[["ts","userId","level","sessionId","location","userAgent"]].values.tolist()
        songplaylist.insert(4,song_id)
        songplaylist.insert(5,artist_id)
        curr.execute(songplays_data_insert_query,songplaylist)


# Creating the main function for the python program
if __name__ == "__main__":
    songdatafilepath = '/Users/s0k01c6/Documents/MyGitRepos/Udacity-Relational_Data_Modeling/data/song_data'
    logdatafilepath = '/Users/s0k01c6/Documents/MyGitRepos/Udacity-Relational_Data_Modeling/data/log_data'
    main()
         