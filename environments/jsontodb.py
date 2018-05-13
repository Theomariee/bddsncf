import glob,os,json,pprint,ast

#script permettant de parcourir tout les fichiers JSON ecrits grace a la requete
#et d'ajouter les infos interessantes dans la BDD

#os.chdir("~/Documents/SNCF/environments/output")
os.chdir("test") 
for file in glob.glob("*.json"):
	with open(file,'r') as json_data:
		temp=(json_data.read())
		print(temp[47064])
		data=json.loads(temp.replace("\\",""))
	print(data)
	#print(str(data['departures']))

	#print(data)
	#print(type(data))

	#data=ast.literal_eval(json_data)
	#print(type(data))	

	#print(data)

	for i in range(0, len(data['departures'])):
		train_direction=data['departures'][i]['display_informations']['direction'] 
		train_headsign=data['departures'][i]['display_informations']['headsign'] #nom du train
		
		train_type=data['departures'][i]['stop_point']['physical_modes'][0]['name']
		stop_area_id=data['departures'][i]['stop_point']['stop_area']['id'] #il faut parser en supprimant les lettres de 0 a 16 inclues, pour 9 lettres car c'est un ID
		stop_area_id=stop_area_id[17:27]
		print(stop_area_id)

		train_arrival_date_time=data['departures'][i]['stop_date_time']['arrival_date_time']		
		train_base_arrival_date_time=data['departures'][i]['stop_date_time']['base_arrival_date_time']
		train_departure_date_time=data['departures'][i]['stop_date_time']['departure_date_time']
		train_base_departure_date_time=data['departures'][i]['stop_date_time']['base_departure_date_time']
		
		#faire l'ajout a la BDD table Arrivals avec cle = stop_area_id, train_headsign, train_arrival_base_date_time



		#test des infos
		print(train_direction+" "+train_headsign+" "+train_type+" "+stop_area_id+" "+train_arrival_date_time+" "+train_base_arrival_date_time+" "+train_departure_date_time+" "+train_base_departure_date_time)


	print('')

#info : pour ajouter a SQL un JSON il faut utiliser json.dumps(data) pour transformer le json en un json string utilisable dans un text field SQL

