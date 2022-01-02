# Udacity-Relational_Data_Modeling
Udacity - Relational Data Modeling with PostgresSQL
# Problem Statement:
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.
# Implementation Details
This project is aimed at creating a data modeling with Postgres and build an ETL pipeline using Python. 
To complete data modeling, this project defines fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into tables in Postgres using Python and SQL.
This project aims at testing your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.
# Database Details
Database Name: sparkifydb
Table names & Schema 
  # Artists
  CREATE TABLE IF NOT EXISTS public.artists
(
    artist_id character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    location character varying COLLATE pg_catalog."default",
    latitude numeric,
    longitude numeric,
    CONSTRAINT artist_key PRIMARY KEY (artist_id)
)
 # Songs
  CREATE TABLE IF NOT EXISTS public.songs
(
    song_id character varying COLLATE pg_catalog."default" NOT NULL,
    title character varying COLLATE pg_catalog."default",
    artist_id character varying COLLATE pg_catalog."default",
    year integer,
    duration numeric,
    CONSTRAINT song_key PRIMARY KEY (song_id)
)
 # Users
 CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL,
    first_name character varying COLLATE pg_catalog."default",
    last_name character varying COLLATE pg_catalog."default",
    gender character varying COLLATE pg_catalog."default",
    level character varying COLLATE pg_catalog."default",
    CONSTRAINT user_key PRIMARY KEY (user_id)
)
# Time
CREATE TABLE IF NOT EXISTS public."time"
(
    start_time timestamp without time zone,
    hour character varying COLLATE pg_catalog."default",
    day character varying COLLATE pg_catalog."default",
    week character varying COLLATE pg_catalog."default",
    month character varying COLLATE pg_catalog."default",
    year character varying COLLATE pg_catalog."default",
    weekday character varying COLLATE pg_catalog."default"
)
# songplays
CREATE TABLE IF NOT EXISTS public.songplays
(
    songplay_id integer NOT NULL DEFAULT nextval('songplays_songplay_id_seq'::regclass),
    start_time timestamp without time zone,
    user_id character varying COLLATE pg_catalog."default",
    level character varying COLLATE pg_catalog."default",
    song_id character varying COLLATE pg_catalog."default",
    artist_id character varying COLLATE pg_catalog."default",
    session_id character varying COLLATE pg_catalog."default",
    location character varying COLLATE pg_catalog."default",
    user_agent character varying COLLATE pg_catalog."default",
    CONSTRAINT songplays_key UNIQUE (songplay_id, user_id, song_id, artist_id, start_time)
)

# File Details:
 sql_queries.py -> This python file consists of all sql queries to create, drop and insert data in the postgres table.
 create_tables.py -> This file basically creates the databas connection, drops the table if exists and create the tables.
 etl_process.py -> This file basically connects to the database, and execute the song and log data set to insert records in the sparkify database tables.
 test.py -> This file basically counts the records present in database tables.



