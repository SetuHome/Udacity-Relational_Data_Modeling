# This Python file basically runs all SQL Queries which are responsible for dropping the table and recreating the table.
# Also import the postgresql python package, creates the connection and assign a cursor for executing the queries.

import psycopg2
from sql_queries_prj import drop_queries,create_queries

#Creating the connection with default database

def create_database():

    # creating the database connection with default database
    try:
        conn = psycopg2.connect("host=localhost user=s0k01c6 password=SetuHome")
        print("Connection Successful")
        curr = conn.cursor()
        conn.set_session(autocommit=True)
    except psycopg2.Error as e:
        print("Error: Could not connect to the database")
        print(e)
    
    # create sparkify database with UTF8 encoding
    try:
        curr.execute("DROP DATABASE IF EXISTS sparkifydb")
        curr.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
        print("Database creation Successful")
    except psycopg2.Error as e:
        print("Error: Could not create the database")
        print(e)
    
    #Closing the connection with current/default database
    conn.close()
    
    # creating the database connection with sparkifydb database

    try:
        conn = psycopg2.connect("host=localhost dbname=sparkifydb user=s0k01c6 password=SetuHome")
        print("Connection to sparkify database is successful")
        curr = conn.cursor()
        conn.set_session(autocommit=True)
        return curr, conn
    except psycopg2.Error as e:
        print("Error: Could not create the database")
        print(e)


def drop_tables(curr,conn):
    #Processing the drop table query list created in the file sql_queries_prj.py
    try:
        for query in drop_queries:
            curr.execute(query)
            conn.commit()
        print("All tables dropped successfully")
    except psycopg2.Error as e:
        print("Error: Could not execute the drop query successfully")
        print(e)


def create_tables(curr,conn):
    try:
        for query in create_queries:
            curr.execute(query)
            conn.commit()
        print("All tables created successfully")
    except psycopg2.Error as e:
        print("Error: Could not execute the create query successfully")
        print(e) 



def main():
    curr, conn = create_database()
    drop_tables(curr,conn)
    create_tables(curr,conn)

if __name__ == "__main__":
    main()

