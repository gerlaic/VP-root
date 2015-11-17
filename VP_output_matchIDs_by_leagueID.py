#library
import urllib.request, json
import csv

#project
import VP_variable_chart

#parameters
league_id = '4039'
output_file_string = VP_variable_chart.output_file_string

url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key='+VP_variable_chart.api_key+'&leagueid='+league_id

#Functions
#function readin json
def readin_json(request_url):
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
matches = readin_json(url)['result']['matches'];

matchIDs = []
for match in matches:
    matchIDs.append(match['match_id'])

#print(matchIDs)



