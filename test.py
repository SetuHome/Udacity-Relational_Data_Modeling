''' This python script basically checks the data populated in the table.'''
import os
import sys
import psycopg2


def create_dbconnect():
    """This function basically craetes the connection with the database

    Returns:
        curr: the cursor object
        conn: the connection object
    """
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
    """This function calculates the number of rows present in song table

    Args:
        curr : [The cursor object]
    """
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
    """This function calculates the number of rows present in artists table

    Args:
        curr : [The cursor object]
    """
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
    """This function calculates the number of rows present in users table

    Args:
    curr : [The cursor object]
    """
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
    """This function calculates the number of rows present in time table

    Args:
        curr : [The cursor object]
    """
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
    """This function calculates the number of rows present in songplays table

    Args:
        curr: [The cursor object]
    """
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
    """This function basically calls different functions which shows the table count value
    """

    curr, conn = create_dbconnect()
    songs_count(curr)
    artists_count(curr)
    users_count(curr)
    time_count(curr)
    songplays_count(curr)
    close_connection(curr,conn)


if __name__ == "__main__":
    """This function is the main function
    """
    main()
