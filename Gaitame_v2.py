import requests

# Gaitame Position API (they serve raw JSON from this URL)
url = "https://navi.gaitame.com/v3/info/tools/position"

response = requests.get(url)
print(response.status_code)

data = response.json()

# Check the data
for item in data['data']:
    pair = item['pair']
    ratios = item['ratios']
    if pair in ["USDJPY", "EURJPY","GBPJPY","AUDJPY"]:
        print(f"{pair}: {ratios[0]}")
        #print(f"{ratios[0]['buy']}")
