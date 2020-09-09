import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://trend.sabamedia.info/')
soup = BeautifulSoup(r.text, 'html.parser')

items = soup.find_all('a', {'class': 'collection-item'})
pars_items = dict()

for item in items[0:10]:
    name = item.find('span', {'class': 'pf'}).text.strip()
    count = int(re.sub(r'^(\d*).*', '\g<1>', item.find('span', {'class': 'pfn'}).text.strip()))
    pars_items[name] = {'count': count}
    
print('Trends in persian twitter:')
i = 1
for item in pars_items:
    print('%2i- The Hashtag #%30s trended by %9i twits and retwits.' % (i, item, pars_items[item]['count']))
    i += 1