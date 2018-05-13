#!/bin/bash

#cette commande run le programme toutes les 25 secondes avec un paramètre qui
#correspond à l uid qui est query en temps réel, soit la gare qu on veut observer

#tableau d UID, tout les uid que nous analysons
tab=


#indice de lUID observé
n=0
nbuid=${#tableau[@]} # taille du tableau

#script qui lance la requete sur les UID
while true;do
	modulo=$n%nbuid
	bash requetetempsreel.sh $tab[$modulo]
	n++
	sleep 25
done
