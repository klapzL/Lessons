from bs4 import BeautifulSoup as BS
import requests as rq

URL = 'https://akipress.org/'
main_page = rq.get(URL)
soup = BS(main_page.text, 'html.parser')

last50 = soup.find('table', id ='last50')

links = last50.find_all('a')
paths = []
for l in links:
	p = l.get('href')
	if p and 'tazabek.kg/' in p:
		paths.append('https:'+p)

file = open('text.txt')
ph = []
print(paths[0])
for tzbk in paths:
	tzbk_page = rq.get(tzbk)
	if tzbk != tzbk.page.url:
		continue
	tzbk_soup = BS(tzbk_page.text, 'html.parser')
	title = tzbk_soup.find('h2', class_= 'title')
	paragraph = tzbk_soup.find(id = 'native-reklama').find_all('p')
	if len(title) > 0 and len(paragraph) > 0:
		print(title)
		print(paragraph)
		# file.write(str(title) + '\n')

	# if len(paragraph) > 0:


