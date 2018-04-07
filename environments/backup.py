import requests,json,datetime
#partie du script qui récupère, en fonction de l'uic, les 21 derniers jours d'une gare en JSON
#les dates ne sont pas automatisées, le script doit être executé tout les 21 du mois
uic=87391003

from datetime import datetime
#now=datetime.now()

for i in range(15,21) : #de 1 à 21
	prefixejour=0
	jour=i%10
	if (10 <= i <=19):
		prefixejour=1
	if (20 <=i <=29):
		prefixejour=2
	if (30 <= i <=31):
		prefixejour=3	

	mois=int(datetime.now().strftime('%m'))-1 #le mois dernier

	url = "https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:OCE:SA:"+str(uic)+"/departures?datetime="+datetime.now().strftime('%Y')+"0"+str(mois)+str(prefixejour)+str(jour)+"T100000" #à10h00m00s
	#TOKEN f4d7c70e-074a-4866-afae-f63e4116e3d5

	print("lancement de la requête "+url+" et écriture")

	data = requests.get(url,headers={'Authorization': '3a845050-a232-4e4c-bb42-b8d0a8c085b6'}).json()
	#data=requests.get(url).json()	

	f=open('file.json','w')
	f.write(repr(data))
	f.close()
	
	#print(json.dumps(data, indent=2, sort_keys=True))
