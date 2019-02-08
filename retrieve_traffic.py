import requests

traffic_url = 'https://www.anwb.nl/feeds/gethf'
headers = {'User-agent': 'Mozilla/5.0'}

traffic_json_data = requests.get(traffic_url, headers=headers).json()

print(traffic_json_data)
