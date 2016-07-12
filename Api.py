import requests
import xmltodict


api_key = 'l1eCwD6ckPZinhRvhA9MSQ'

url = 'https://www.goodreads.com/review/list/46998003.xml?key={}&v=2'.format(api_key)
res = requests.get(url)

data = xmltodict.parse(res.text)

print(data['GoodreadsResponse']['reviews']['review'][2]['book']['title'])

for title in data['GoodreadsResponse']['reviews']['review']:
    print(title['book']['title'])
