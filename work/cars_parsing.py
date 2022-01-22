import requests as rq
from bs4 import BeautifulSoup as BS

file = open('text.txt', 'w', encoding='utf-8')

url = 'https://cars.kg/offers/'
soup = BS(rq.get(url).text, 'lxml')
catalog_list = soup.find('div', class_='catalog-list')
links = catalog_list.find_all('a')
paths = []
for l in links:
	p = l.get('href')
	paths.append('https://cars.kg' + p)

for val, l  in enumerate(paths):
	cars_soup = BS(rq.get(l).text, 'lxml')
	title = cars_soup.find_all('h1')
	n = ''.join(list(map(lambda n: n.text, title)))
	file.write(n.strip())	
