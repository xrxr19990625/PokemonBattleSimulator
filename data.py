import requests
from bs4 import BeautifulSoup
from pokemon import DualTypePokemon, SingleTypePokemon


def fetch_data_from_webdb():
    dex_page = requests.get('https://pokemondb.net/pokedex/all')
    with open('data.html', 'w', encoding='utf-8') as file:
        file.write(dex_page.text)


def fetch_data_from_localdb():
    dex_page = ''
    with open('data.html', 'r', encoding='utf-8') as file:
        for i in file:
            dex_page += i.strip()
    return dex_page
    pass


if __name__ == '__main__':
    dex_page = fetch_data_from_localdb()
    with open('data.html', 'r', encoding='utf-8') as file:
        for i in file:
            dex_page += i.strip()
    dex_soup = BeautifulSoup(dex_page, 'html.parser')
    dex_table = dex_soup.find('table', attrs={'id': 'pokedex'})
    dex_tbody = dex_table.find('tbody')
    pokemons = dex_tbody.find_all('tr')
    pokemon_list = []
    for i in pokemons:
        attrs = i.find_all('td')
        national_id = attrs[0].find('span', attrs={'class': 'infocard-cell-data'}).text
        national_id = int(national_id)
        name_tag = attrs[1]
        name = name_tag.find('a')
        morph = name_tag.find('small')
        if morph is not None:
            name = morph.text
        else:
            name = name.text
        stats = []
        for j in attrs[4:]:
            stats.append(int(j.text))
        type_tag = attrs[2]
        type_ = type_tag.find_all('a')
        type1_ = None
        type2_ = None
        if len(type_) == 2:
            type1_ = type_[0].text
            type2_ = type_[1].text
            pokemon = DualTypePokemon(name, national_id, type1_, type2_)
            pokemon.set_stats(stats)
        else:
            type1_ = type_[0].text
            pokemon = SingleTypePokemon(name, national_id, type1_)
            pokemon.set_stats(stats)
        pokemon_list.append(pokemon)
    print(pokemon_list[3].id_)
    pass
