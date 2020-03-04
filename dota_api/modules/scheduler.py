import requests
from bs4 import BeautifulSoup
from dota_api.modules.db_data import mongo_auth


def get_info():
    get_meta_heroes()
    remove_blanked()


def remove_blanked():
    mongo = mongo_auth()
    collection = mongo.achievements
    collection.remove({'status': 'no_games'})


def get_meta_heroes():
    url = 'https://www.dotabuff.com/heroes/played'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print('=== Error while getting meta heroes info from Dotabuff')
        print(r.content)
    else:
        heroes = []
        page = BeautifulSoup(r.content, features="html.parser")
        table = page.find('tbody').find_all('tr')
        for line in table:
            cols = line.find_all('td')
            hero_name = cols[1].get_text()
            hero_winrate = float(cols[4]['data-value'])
            if hero_winrate >= 52.5:
                heroes.append({
                    'hero_name': hero_name,
                    'hero_winrate': hero_winrate
                })
        mongo = mongo_auth()
        collection = mongo.meta_heroes
        collection.remove({})
        collection.insert(heroes)
