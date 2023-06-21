import requests
from pprint import pprint

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1687132800&todate=1687305600&order=desc&\
sort=activity&tagged=Python&site=stackoverflow'
response = requests.get(url)
# pprint(response.json())

items_list = response.json().get('items', [])
# pprint(items_list)
titles_list = []
for item in items_list:
    titles_list.append(item['title'])
print("Перечень тем за последние 2 дня на тему PYTHON:\n", '\n'.join(titles_list))