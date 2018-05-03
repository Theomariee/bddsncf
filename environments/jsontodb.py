import glob,os,json,pprint

#script permettant de parcourir tout les fichiers JSON écrits grace à la requete
#et d'ajouter les infos intéressantes dans la BDD

#os.chdir("~/Documents/SNCF/environments/output")
os.chdir("output")
for file in glob.glob("*.json"):
	json_data=open(file).read()
	data=json.loads(json_data)
	#pprint.pprint(data)

	#pprint.pprint(data["departures"]) #test; il suffit de prendre les champs qu'on veut avec []

	for i in range(0, len(data['departures'])):
		print(data['departures'][i])
	
	print('')

#info : pour ajouter a SQL un JSON il faut utiliser json.dumps(data) pour transformer le json en un json string utilisable dans un text field SQL

