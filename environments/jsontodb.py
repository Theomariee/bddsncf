import glob,os,json,pprint

#script permettant de parcourir tout les fichiers JSON écrits grace à la requete
#et d'ajouter les infos intéressantes dans la BDD

#os.chdir("~/Documents/SNCF/environments/output")
os.chdir("output")
for file in glob.glob("*.json"):
	json_data=open(file).read()
	data=json.loads(json_data)

	for i in range(0, len(data['departures'])):
		train_direction=data['departures'][i]['display_informations']['direction'] 
		train_headsign=data['departures'][i]['display_informations']['headsign'] #nom du train
		
		train_type=data['departures'][i]['stop_point']['physical_modes'][0]['name']
		stop_area_id=data['departures'][i]['stop_point']['stop_area']['id'] #il faut parser en supprimant les lettres de 0 à 16 inclues, pour 9 lettres car c'est un ID
		stop_area_id=stop_area_id[17,27]
		print(stop_area_id)

		train_arrival_date_time=data['departures'][i]['stop_date_time']['arrival_date_time']		
		train_base_arrival_date_time=data['departures'][i]['stop_date_time']['base_arrival_date_time']
		train_departure_date_time=data['departures'][i]['stop_date_time']['departure_date_time']
		train_base_departure_date_time=data['departures'][i]['stop_date_time']['base_departure_date_time']
		
		#faire l'ajout à la BDD table Arrivals avec clé = stop_area_id, train_headsign, train_arrival_base_date_time

	print('')

#info : pour ajouter a SQL un JSON il faut utiliser json.dumps(data) pour transformer le json en un json string utilisable dans un text field SQL

