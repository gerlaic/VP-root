#library
import urllib.request, json
import csv

#project
import VP_variable_chart

#parameters
match_id = '1919873245'
output_file_string = VP_variable_chart.output_file_string


#Functions
#function readin json
def readin_json(request_url,key, id):

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
print('###FINDING REPLAY SALT')

api_url = "https://api.steampowered.com/IDOTA2Match_570"

url1 = api_url + "/GetMatchDetails/V001/?key=" + VP_variable_chart.api_key + "&match_id=" + match_id;

urls = [url1];

for url in urls:
    match_detail = readin_json(url,VP_variable_chart.api_key,match_id)
    if ('replay_salt' in match_detail) or ('cluster' in match_detail):
        print(url)

