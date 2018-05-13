#!/bin/bash

#script executé pour faire une requête à l'api
#prend en paramètre l UID qui est à requêter

uid=$1
#requete de l UID qui remplis notre fichier JSON
$(curl -u f4d7c70e-074a-4866-afae-f63e4116e3d5: https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:0CE:SA:$uid/departures >> bdd.json)
