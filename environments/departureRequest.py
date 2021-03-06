
import requests,json,datetime,pprint
from datetime import datetime

#partie du script qui recupere, en fonction de son UIC, les X informations de X jours d'une gare en JSON
#modifier les dates manuellement pour changer les jours ou l'heure de la gare, et donc acceder a de nouvelles informations
def departureRequest(uic):
    

	#uic = 87391003 #test avec gare montparnasse


	tabmois=[31,27,31,30,31,30,31,31,30,31,30,31] #tableau avec le nombre de jours par mois

	for mois in range(5,6) : #boucle des mois

		for i in range(01,13) : #boucle des jours

			prefixejour=0 
			jour=i%10
			if (10 <= i <=19):
				prefixejour=1
			if (20 <= i <=29):
				prefixejour=2
			if (30 <= i <=31):
				prefixejour=3	
	
			#mois=int(datetime.now().strftime('%m'))-1 #recuperation du mois dernier (le 0 n'est pas affiche il faut gerer le prefixe; soit en creant un int prefixe soit en changeant le mois en string et en mettant 0 devant)

			if (0 < mois <10):	
				prefixemois=0
			else:
				prefixemois=1


			annee=int(datetime.now().strftime('%Y')) #annee en int

			heure="000000" #00h00m00s

			url = "https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:OCE:SA:"+str(uic)+"/departures?from_datetime="+str(annee)+str(prefixemois)+str(mois)+str(prefixejour)+str(jour)+"T"+str(heure)+"&count=1000"


			token = "f4d7c70e-074a-4866-afae-f63e4116e3d5" #token theo

			print("lancement de la requete "+url+" et ecriture")

			#token = '3a845050-a232-4e4c-bb42-b8d0a8c085b6' #=token coco

			data = requests.get(url,auth=(token,'')) #requete HTML

			#'3b036afe-0110-4202-b9ed-99718476c2e0'	#=sandbox token
	

			#pprint.pprint(data.json()) #affichage de l'output json
	

			#ecriture dans le dossier output d'un fichier json nomme : uic_jour_mois_annee_heure
			f=open('./output2/'+str(uic)+"_"+str(prefixejour)+str(jour)+"_"+str(prefixemois)+str(mois)+"_"+str(annee)+'.json','w')
			f.write(repr(json.dumps(data.json()))[1:-1])
			f.close()

if __name__ == '__main__':
    departureRequest(87391003) #gare montparnasse
