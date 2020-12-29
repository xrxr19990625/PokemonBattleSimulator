import requests
from bs4 import BeautifulSoup
import re


base_url = 'https://wiki.52poke.com'


if __name__ == '__main__':
    f = open('main_page.html', 'r', encoding='utf-8')
    r = ''
    for i in f:
        r += i.strip()
    soup = BeautifulSoup(r, 'html.parser')
    all_tables = soup.find_all('table')
    kantou = all_tables[2]
    kantou_pokemons = kantou.find('tbody').find_all('tr')[2:]
    pokemon_pages = []
    for i in kantou_pokemons:
        pokemon_pages.append(base_url + i.find('a').attrs['href'])
    f = open('venasaur.html', 'r', encoding='utf-8')
    r = ''
    for i in f:
        r += i.strip()
    regex = '.*<tbody.*title="属性">属性</a></b>.*?<tbody><tr>(.*?)</tr></tbody>'
    result = re.match(regex, r, re.S)
    type_info = result.group(1)
    type_soup = BeautifulSoup(type_info, 'html.parser')
    print(type_soup.find_all('a')[0].text)
    print(type_soup.find_all('a')[1].text)
    print(type_soup.find_all('a')[2].text)
    print(type_soup.find_all('a')[3].text)
    pass
