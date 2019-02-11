import requests

traffic_url = 'https://www.anwb.nl/feeds/gethf'
headers = {'User-agent': 'Mozilla/5.0'}

traffic_json_data = requests.get(traffic_url, headers=headers).json()

r = 'A12'
road = [d for d in traffic_json_data['roadEntries'] if d['road'] == r]

traffic_jams = [d for d in road[0]['events']['trafficJams'] if d['from'] == 'knp. Velperbroek']
road_works = [d for d in road[0]['events']['roadWorks'] if d['segStart'] == 'Hengelo']
radars = [d for d in road[0]['events']['radars'] if d['segStart'] == 'Amersfoort']

print(road[0])
print(traffic_jams)
print(road_works)
print(radars)
