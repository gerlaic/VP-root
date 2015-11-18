import json
import urllib.request
import ssl
import bz2

print('Downloading Replay!')

match_detail_json = 'Result_Match_details.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def download_replay(file_string):
	jsonData = read_in_json(file_string)

	cluster = jsonData['match']['cluster']
	replay_salt = jsonData['match']['replay_salt']
	match_id = jsonData['match']['match_id']['low']

	api_string = 'https://replay'+str(cluster)+'.valve.net/570/'+str(match_id)+'_'+str(replay_salt)+'.dem.bz2'
	file_name = str(match_id)+'_'+str(replay_salt)+'.dem.bz2'
	rep_name = str(match_id)+'.dem'

	print(api_string)

	with urllib.request.urlopen(api_string, context=ctx) as u:
		f = open(file_name, 'wb')
		f.write(u.read())

	print('Download Complete! v(?8?)v')
	return [file_name,rep_name]

def unzip_replay(fin,fout):
	print('Start unzipping > 8 <')
	o = bz2.open(fin)
	with open(fin, 'rb') as source, open(fout,'wb') as dest:
		dest.write(bz2.decompress(source.read()))

	print('Unzip Complete! v(?8?)v')
	return

def read_in_json(file_string):
	with open(file_string, encoding='utf-8') as data_file:
		data = json.load(data_file)

	print('data received')
	return data


[fin,fout] = download_replay(match_detail_json)
#fout = '1941168342.dem'
#fin = '1941168342_1779967112.dem.bz2'
unzip_replay(fin,fout)