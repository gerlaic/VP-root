import urllib.request, json
request_url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?key=605A60989EAE14462B6020917BD2E375&league_id=3502";

response = urllib.request.urlopen(request_url)
content = response.read()
data = json.loads(content.decode('utf8'))

#print(data['result'])
result = data['result'];
total_results = result['total_results'];
results_remaining = result['results_remaining'];
matches = result['matches'];

for match_item in matches:
	print(match_item['match_id'])
