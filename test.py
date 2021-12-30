''' This python script basically checks the data populated in the table.'''
import os
import sys
import psycopg2


def create_dbconnect():
    try:
        conn = psycopg2.connect("host=localhost dbname=sparkifydb user=s0k01c6 password=SetuHome")
        curr = conn.cursor()
        conn.set_session(autocommit = True)
        print("Connection established successfully")
        return curr, conn

    except psycopg2.Error as e:
        print("Error: Could not connect to the databas")
        print(e)

def songs_count(curr):
    try:
        curr.execute("Select * from songs limit 5")
        row = curr.fetchone()
        print("Songs table data below")
        while(row):
            print(row)
            row = curr.fetchone()
    except psycopg2.Error as e:
        print("Error: Could not fetch the table records")
        print(e) 

def artists_count(curr):
    try:
        curr.execute("Select * from artists limit 5")
        row = curr.fetchone()
        print("artists table data below")
        while(row):
            print(row)
            row = curr.fetchone()
    except psycopg2.Error as e:
        print("Error: Could not fetch the table records")
        print(e)

def users_count(curr):
    try:
        curr.execute("Select * from users limit 5")
        row = curr.fetchone()
        print("Users table data below")
        while(row):
            print(row)
            row = curr.fetchone()
    except psycopg2.Error as e:
        print("Error: Could not fetch the table records")
        print(e)

def time_count(curr):
    try:
        curr.execute("Select * from time limit 5")
        row=curr.fetchone()
        print("Time table data below")
        while(row):
            print(row)
            row = curr.fetchone()
    except psycopg2.Error as e:
        print("Error: Could not fetch the table records")
        print(e)


def songplays_count(curr):
    try:
        curr.execute("Select * from songplays limit 5")
        row = curr.fetchone()
        print("Songplays table data below")
        while(row):
            print(row)
            row = curr.fetchone()
    except psycopg2.Error as e:
        print("Error: Could not fetch the table records")
        print(e)

def close_connection(curr, conn):
    curr.close()
    conn.close()

def main():

    curr, conn = create_dbconnect()
    songs_count(curr)
    artists_count(curr)
    users_count(curr)
    time_count(curr)
    songplays_count(curr)
    close_connection(curr,conn)


if __name__ == "__main__":
    main()
