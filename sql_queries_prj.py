#This python file consist of all SQL Queries to be used in the assignment. These SQL Queries are created as python variables which is 
#to be used for further implementation

#Drop Table Variables defined 

drop_users = ("""DROP TABLE IF EXISTS users""")
drop_songs = ("""DROP TABLE IF EXISTS songs""")
drop_artists = ("""DROP TABLE IF EXISTS artists""")
drop_time = ("""DROP TABLE IF EXISTS time""")
drop_songplays = ("""DROP TABLE IF EXISTS songplays""")


#Create Table Variables defined

create_users = ("""CREATE TABLE IF NOT EXISTS users(userid int,\
                                                   first_name varchar,\
                                                   last_name varchar,\
                                                    gender varchar,\
                                                    level int)""")

create_songs = ("""CREATE TABLE IF NOT EXISTS songs(song_id int,\
                                                   title varchar,\
                                                   artist_id int,\
                                                    year int,\
                                                    duration time)""")

create_artists = ("""CREATE TABLE IF NOT EXISTS artists(artist_id int,\
                                                     name varchar,\
                                                     location varchar,\
                                                     latitude decimal,\
                                                     longitude decimal)""")

create_time = ("""CREATE TABLE IF NOT EXISTS time(start_time time,\
                                                     hour decimal,\
                                                     day int,\
                                                     week int,\
                                                     month int,\
                                                     year int,\
                                                     weekday int)""")

create_songplays = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id int,\
                                                     start_time timestamp,\
                                                     user_id int,\
                                                     level int,\
                                                     song_id int,\
                                                     artist_id int,\
                                                     session_id int,\
                                                     location varchar,\
                                                     user_agent varchar)""")


# creating a list of variables to be used for further implementation

drop_queries = [drop_users,drop_songs,drop_artists,drop_time,drop_songplays]
create_queries = [create_users,create_songs,create_artists,create_time,create_songplays]