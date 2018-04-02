#!bin/bash

random=$(pwgen 20 1)
output_head="outputgaresbreizh_"
output_tail=".json"



$(curl -X GET --header 'Accept: application/json' 'https://data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&q=REGION%20BRETAGNE&sort=region_sncf&facet=segment_drg&pretty=true' > $output_head$random$output_tail)

echo $output_head$random$output_tail
