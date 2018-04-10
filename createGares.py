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
    cur.execute("""DROP TABLE gares;""")
    cur.execute("""CREATE TABLE IF NOT EXISTS gares (uic VARCHAR(10) PRIMARY KEY NOT NULL, departement VARCHAR(100) NOT NULL, intitule VARCHAR(200) NOT NULL, region VARCHAR(100) NOT NULL, commune VARCHAR(200) NOT NULL, latitude FLOAT(10) NOT NULL, longitude FLOAT(10) NOT NULL);""")
    cur.close()
    print(conn.notices)
    conn.commit()
    conn.close()       
    #execute statement
    with open('output/outputgares.json', 'r') as f:
        data = json.loads(f.read())   	   
    for rec in data: 
	conn = psycopg2.connect("dbname='sncf' user='postgres' host='localhost' password='esaco15obofo'")
	cur = conn.cursor()
	#print(rec)
	uic = rec.get("uic")
        departement = rec.get("departement")
        intitule = rec.get("intitule_gare")
        region = rec.get("region")
        commune = rec.get("commune")
        latitude = rec.get("latitude_wgs84")
        longitude = rec.get("longitude_wgs84")
        print("Insertion : gare(", uic, departement, intitule, region, commune, latitude, longitude, ")...")
	try:
            cur.execute("""INSERT INTO gares (uic, departement, intitule, region, commune, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s);""", (uic, departement, intitule, region, commune, latitude, longitude))
	    cur.close()
	    conn.commit()
	    conn.close()
	except (Exception, psycopg2.DatabaseError) as error:
	    pass
	    #print(error)	

        
 # execute a statement
        
       
     # close the communication with the PostgreSQL

      
    if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    createGares()
