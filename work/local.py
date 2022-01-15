from bs4 import BeautifulSoup as bs

with open('page.html', 'r', encoding='utf-8') as f:
    contents = f.read()
    soup = bs(contents, 'html.parser')
    # print("HEAD", soup.head)
    # print("TITLE", soup.title)
    header = soup.find('header')
    ul = header.find('ul')
    links = ul.find_all('a')
    for l in links:
        print('Текст', l.string)
        print('Текст', l.text)
        print('Название тега', l.name)
        print('Аттрибуты', l['href'])
        print(f"href ссылки '{l.get('href')}'")