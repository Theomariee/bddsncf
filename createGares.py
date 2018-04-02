#!/usr/bin/python3.4
import psycopg2, json
from config import config 

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

        cur.execute("""CREATE TABLE IF NOT EXISTS gares (
	uic CHAR(10) PRIMARY KEY NOT NULL,
	departement CHAR(100) NOT NULL,
	intitule CHAR(200) NOT NULL,
	region CHAR(100) NOT NULL,
	commune CHAR(200) NOT NULL,
	latitude NUMERIC(10,7) NOT NULL,
	longitude NUMERIC(10,7) NOT NULL""")
        cur.close()
	

        cur = conn.cursor(cursor_factory=PreparingCursor)
        
        #execute statement
        cur.prepare("INSERT INTO gares (uic, departement, intitule, region, commune, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        with open('output/outputgares.json', 'r') as f:
        data = json.load(f)
        for rec in data :
            uic = rec.get("uic")
            departement = rec.get("departement")
            intitule = rec.get("intitule_gare")
            region = rec.get("region")
            commune = rec.get("commune")
            latitude = rec.get("latitude_wgs84")
            longitude = rec.get("longitude_wgs84")
            print(uic, departement, intitule, region, commune, latitude, longitude, sep=', ')
            #cur.execute((uic, departement, intitule, region, commune, latitude, longitude))

        

        

        
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
