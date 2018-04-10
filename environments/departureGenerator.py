#!/usr/bin/python3.4
import psycopg2
from departureRequest import departureRequest
from config import config 

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname='sncf' user='postgres' host='localhost' password='esaco15obofo'") 
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        cur.execute('SELECT * FROM gares;')
 
        # display the PostgreSQL database server version
        gares = cur.fetchall()
        for gare in gares:
			uic = gare['uic']
			print("gare " + uic + " requested")
			departureRequest(gare['uic'])
			print("gare " + uic + " request done")
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()
