#This python file consist of all SQL Queries to be used in the assignment. These SQL Queries are created as python variables which is 
#to be used for further implementation

#Drop Table Variables defined 

drop_users = ("""DROP TABLE IF EXISTS users""")
drop_songs = ("""DROP TABLE IF EXISTS songs""")
drop_artists = ("""DROP TABLE IF EXISTS artists""")
drop_time = ("""DROP TABLE IF EXISTS time""")
drop_songplays = ("""DROP TABLE IF EXISTS songplays""")


#Create Table Variables defined

create_users = ("""CREATE TABLE IF NOT EXISTS users(user_id int,\
                                                   first_name varchar,\
                                                   last_name varchar,\
                                                    gender varchar,\
                                                    level varchar,\
                                                    CONSTRAINT user_key PRIMARY KEY (user_id))""")

create_songs = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar,\
                                                   title varchar,\
                                                   artist_id varchar,\
                                                    year int,\
                                                    duration decimal,\
                                                    CONSTRAINT song_key PRIMARY KEY (song_id))""")

create_artists = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar,\
                                                     name varchar,\
                                                     location varchar,\
                                                     latitude decimal,\
                                                     longitude decimal,\
                                                     CONSTRAINT artist_key PRIMARY KEY (artist_id))""")

create_time = ("""CREATE TABLE IF NOT EXISTS time(start_time timestamp,\
                                                     hour varchar,\
                                                     day varchar,\
                                                     week varchar,\
                                                     month varchar,\
                                                     year varchar,\
                                                     weekday varchar)""")

create_songplays = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL,\
                                                     start_time timestamp,\
                                                     user_id int,\
                                                     level varchar,\
                                                     song_id varchar,\
                                                     artist_id varchar,\
                                                     session_id varchar,\
                                                     location varchar,\
                                                     user_agent varchar,
                                                     CONSTRAINT songplays_key UNIQUE (songplay_id,user_id,song_id,artist_id,start_time))""")

#Insert Table Variables defined

users_data_insert_query = ("""INSERT INTO users(user_id,first_name,last_name,gender,level) \
                        values(%s,%s,%s,%s,%s)""")
songs_data_insert_query = ("""INSERT INTO songs(song_id,title,artist_id,year,duration) \
                        values(%s,%s,%s,%s,%s)""")
artists_data_insert_query = ("""INSERT INTO artists(artist_id,name,location,latitude,longitude) \
                        values(%s,%s,%s,%s,%s) """)
time_data_insert_query = ("""INSERT INTO time(start_time,hour,day,week,month,year,weekday) \
                        values(%s,%s,%s,%s,%s,%s,%s) """)
songplays_data_insert_query = ("""INSERT INTO songplays(songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) \
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """)

#Truncate Table Variables defined
songs_data_truncate_query = ("""TRUNCATE TABLE songs""")
artists_data_truncate_query = ("""TRUNCATE TABLE artists""")
users_data_truncate_query = ("""TRUNCATE TABLE users""")
time_data_truncate_query = ("""TRUNCATE TABLE time""")
songplays_data_truncate_query = ("""TRUNCATE TABLE songplays""")

#Variables desfined for Songplays table
song_data_select = (""" Select a.song_id, b.artist_id from \
public.songs a inner join public.artists b on a.artist_id = b.artist_id """)

# creating a list of variables to be used for further implementation

drop_queries = [drop_users,drop_songs,drop_artists,drop_time,drop_songplays]
create_queries = [create_users,create_songs,create_artists,create_time,create_songplays]