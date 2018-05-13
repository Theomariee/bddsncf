#!/usr/bin/python3.4
import psycopg2
from departureRequest import departureRequest

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
	cur.execute('SELECT uic FROM gares;')
 	# display the PostgreSQL database server version
        gares = cur.fetchall()
	i = 0
        for gare in gares:
		if i < 2475 :
			uic = gare[0]
			print("gare " + uic + " requested")
			departureRequest(int(uic))
			print("gare " + uic + " request done")
			print(i)
			i += 11 
		else :
			break       
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
