
#!/bin/bash

output_head="outputgares"
output_tail=".json"

$(curl -X GET --header 'Accept: application/json' 'https://data.sncf.com/api/records/1.0/search/?dataset=referentiel-gares-voyageurs&sort=region_sncf&facet=segment_drg&pretty=true' > $output_head$output_tail)

echo $output_head$output_tail
