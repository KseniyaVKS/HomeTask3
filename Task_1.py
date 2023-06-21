import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
intelligent_list = []
for geroy in response.json():
    if geroy["name"] in ['Hulk', 'Captain America', 'Thanos']:
        intelligent_list.append((geroy["name"], geroy["powerstats"]["intelligence"]))
        intelligent_sort = sorted(intelligent_list, key=lambda x: -x[1])
print(f'Самый умный из трех супергероев оказался {intelligent_sort[0][0]}')