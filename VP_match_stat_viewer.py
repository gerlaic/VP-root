#library
import urllib.request, json
import csv

#project
import VP_variable_chart

#parameters
match_id = '1865333487'
output_file_string = VP_variable_chart.output_file_string


#Functions
#function readin json
def readin_json(key, id):
    request_url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?key='+key+'&match_id='+id

    response = urllib.request.urlopen(request_url)
    content = response.read()
    data = json.loads(content.decode('utf8'))

    return data

#func export csv
#remember to set the output_file_string in parameter block
def exportFunc(detail, data_source):
	with open((output_file_string+detail+'.csv'), 'w', newline='') as f:
		writer = csv.writer(f)
		for row in data_source:
			writer.writerow(row)

#func add header for csv
def addHeader(header, csvdata):
	csvdata.insert(0,header)

#main program
print('###READING IN MATCH DETAIL')
match_detail = readin_json(VP_variable_chart.api_key,match_id)

#print(match_detail)
result=match_detail['result']

#init output csv list
output_detail = []

keys = ['account_id','hero_id','level','kills','deaths','assists','gold','last_hits','denies','gold_per_min','xp_per_min','gold_spent','hero_damage','tower_damage','hero_healing']
for player in result['players']:
    
    key_value = [];
    for key in keys:
        key_value.append(player[key])  

    output_detail.append(key_value)

addHeader(keys, output_detail)

desired_keys = ['radiant_win', 'duration','start_time','match_id','tower_status_radiant','tower_status_dire','barracks_status_radiant','barracks_status_dire','first_blood_time','lobby_type','leagueid','game_mode','radiant_team_id','radiant_name','dire_team_id','dire_name']


for key in desired_keys:
    if key in result.keys():
        output_detail.append([key,result[key]])

#export
exportFunc('match_detail',output_detail)

