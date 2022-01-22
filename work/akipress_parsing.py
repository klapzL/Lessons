import requests as rq
from bs4 import BeautifulSoup as BS


URL = 'https://akipress.org/'
main_page = rq.get(URL)
soup = BS(main_page.text, 'lxml')

last50 = soup.find('table', id ='last50')

links = last50.find_all('a')
paths = []
for l in links:
	p = l.get('href')
	if p and 'tazabek.kg/news:' in p:
		paths.append('https:'+p)

with open('text.txt', 'w', encoding='utf-8') as file:
	for tzbk in paths:
		tzbk_page = rq.get(tzbk)
		if tzbk != tzbk_page.url:
			continue
		tzbk_soup = BS(tzbk_page.text, 'lxml')
		title = tzbk_soup.find('h2', class_= 'title')
		paragraph = tzbk_soup.find(id = 'native-reklama').find_all('p')
		if len(title) > 0:
			n = ''.join(list(map(lambda n: n.text, paragraph)))
			file.write(title.text + '\n' + n +'\n')
