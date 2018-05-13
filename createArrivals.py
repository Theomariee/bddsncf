#!/usr/bin/python3.4
import psycopg2, json 

from config import config 
from prepare import PreparingCursor

def createGares():
    """ Create and fill "gares" table to the PostgreSQL database server """
    conn = None

    # read connection parameters
    params = config()
 
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect("dbname='sncf' user='postgres' host='localhost' password='esaco15obofo'") 

    # create a cursor
    cur = conn.cursor()
    #cur.execute("""DROP TABLE Arrivals;""")
    cur.execute("""CREATE TABLE Arrivals ( stop_area_id CHAR(10) REFERENCES gares(uic), train_headsign CHAR(10) NOT NULL, train_base_arrival_date_time DATETIME, train_arrival_date_time DATETIME, train_departure_date_time DATETIME, train base_departure_date_time DATETIME, train_direction CHAR(100), PRIMARY KEY (stop_area_id, train_arrival_date_time , train_headsign ));""")
    cur.close()
    print(conn.notices)
    conn.commit()
    conn.close()       
    #execute statement
    	

        
 # execute a statement
        
       
     # close the communication with the PostgreSQL

      
    if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    createGares()
