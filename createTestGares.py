#!/usr/bin/python3.4
import psycopg2, json 

from config import config 
from prepare import PreparingCursor

def createGares():
    """ Create and fill "gares" table to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
	cur.execute("CREATE TABLE gares (test VARCHAR(20)) ;")
        cur.close()
	print(conn.notices)
        
 # execute a statement
        
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    createGares()
