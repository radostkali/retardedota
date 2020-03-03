import asyncio
import aiohttp
import json
import requests
from datetime import datetime
from dota_api.const_data import OPEN_DOTA_HEROES
from config import DOTA_API


class OpenDotaApi:

    urls = {}
    api_data = {}
    data = {}
    error = False

    def __init__(self, dota_id):
        r = requests.post('https://api.opendota.com/api/players/%s/refresh' % dota_id)
        response = json.loads(r.content)
        if 'error' in response:
            self.error = True
        self.urls = {
            'heroes': 'https://api.opendota.com/api/players/%s/heroes?api_key=%s' % (dota_id, DOTA_API),  # 6 achives
            'counts': 'https://api.opendota.com/api/players/%s/counts?api_key=%s' % (dota_id, DOTA_API),  # 6 achives
            'players_info': 'https://api.opendota.com/api/players/%s?api_key=%s' % (dota_id, DOTA_API),  # 1 achive & avatar
            'heroes_month': 'https://api.opendota.com/api/players/%s/heroes?date=30?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'last_match': 'https://api.opendota.com/api/players/%s/matches?limit=1?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'wordcloud': 'https://api.opendota.com/api/players/%s/wordcloud?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'total_stats': 'https://api.opendota.com/api/players/%s/totals?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'friends': 'https://api.opendota.com/api/players/%s/peers?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'matches': 'https://api.opendota.com/api/players/%s/matches?api_key=%s' % (dota_id, DOTA_API),  # 3 achive
            'wards': 'https://api.opendota.com/api/players/%s/matches?sort=purchase_ward_observer&limit=1?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
            'comeback': 'https://api.opendota.com/api/players/%s/matches?sort=comeback&limit=1?api_key=%s' % (dota_id, DOTA_API),  # 1 achive
        }

    async def request_api(self, url, name, session):
        async with session.get(url) as response:
            if response.status == 200:
                response = await response.text()
                try:
                    self.api_data[name] = json.loads(response)
                except Exception as e:
                    print(e)
                    print(response)
            else:
                print('======= Error while getting Open Dota API response...')
                print(response.status)
                print(await response.text())
                return None

    @staticmethod
    def get_hero_info(hero):
        hero_name = next((i['localized_name'] for i in OPEN_DOTA_HEROES if i['id'] == int(hero['hero_id'])), None)
        hero_games = hero['games']
        hero_winrate = round(hero['win'] / hero_games * 100) if hero_games else None
        return {
            'hero_name': hero_name,
            'hero_games': hero_games,
            'hero_winrate': hero_winrate
        }

    async def most_played_hero(self):
        data_name = 'heroes'
        api_data = self.api_data[data_name]

        self.data['most_played_hero'] = None

        if len(api_data):
            hero = api_data[0]
            self.data['most_played_hero'] = self.get_hero_info(hero)

    async def worst_hero(self):
        data_name = 'heroes'
        api_data = self.api_data[data_name]

        self.data['worst_hero'] = None

        heroes = [i for i in api_data if i['games'] >= 30 and round(i['win'] / i['games'] * 100) <= 35]
        if len(heroes):
            hero = (None, 0)
            for i in heroes:
                rate = round((i['games'] ** 2) / i['win'])
                hero = (i, rate) if rate > hero[1] else hero
            self.data['worst_hero'] = self.get_hero_info(hero[0])

    async def last_month_hero(self):
        data_name = 'heroes_month'
        api_data = self.api_data[data_name]

        self.data['last_month_hero'] = None

        if len(api_data):
            hero = api_data[0]
            self.data['last_month_hero'] = self.get_hero_info(hero)
            self.data['last_month_hero']['total_games'] = sum([i['games'] for i in api_data])

    async def mmr_games(self):
        data_name = 'counts'
        api_data = self.api_data[data_name]

        self.data['total_mmr'] = 0

        lobbies = api_data['lobby_type']
        try:
            self.data['total_mmr'] = lobbies['7']['games']
        except KeyError:
            pass

    async def total_games(self):
        data_name = 'counts'
        api_data = self.api_data[data_name]

        self.data['total_abandons'] = 0
        self.data['total_wins'] = 0
        self.data['total_loses'] = 0
        self.data['total_winrate'] = 0
        self.data['total_games'] = 0

        leaved = api_data['leaver_status']
        try:
            self.data['total_wins'] = leaved['0']['win']
            self.data['total_games'] = leaved['0']['games']
            self.data['total_loses'] = leaved['0']['games'] - leaved['0']['win']
            self.data['total_winrate'] = round(leaved['0']['win'] / leaved['0']['games'] * 100)
            self.data['total_abandons'] = sum([leaved[i]['games'] for i in leaved if int(i) >= 2])
        except KeyError:
            pass

    async def players_info(self):
        data_name = 'players_info'
        api_data = self.api_data[data_name]

        self.data['dota_plus'] = None
        self.data['avatar'] = None
        self.data['personaname'] = None

        try:
            self.data['dota_plus'] = api_data['profile']['plus']
            self.data['avatar'] = api_data['profile']['avatarfull']
            self.data['personaname'] = api_data['profile']['personaname']
        except KeyError:
            pass

    async def last_match(self):
        data_name = 'last_match'
        api_data = self.api_data[data_name]

        self.data['last_match'] = None

        try:
            self.data['last_match'] = datetime.utcfromtimestamp(api_data[0]['start_time']) if len(api_data) else None
        except KeyError:
            pass

    async def wordcloud(self):
        data_name = 'wordcloud'
        api_data = self.api_data[data_name]

        self.data['wordcloud'] = {}

        self.data['wordcloud']['words'] = api_data['my_word_counts']
        self.data['wordcloud']['total_words'] = sum(api_data['my_word_counts'].values())

    async def friends(self):
        data_name = 'friends'
        api_data = self.api_data[data_name]

        sorted_friends = sorted(api_data, key=lambda i: i['last_played'])
        sorted_friends.reverse()
        self.data['friends'] = [
            {
                'dota_id': i['account_id'],
                'personaname': i['personaname'],
                'avatarfull': i['avatarfull'],
            }
            for i in sorted_friends[:10]
        ]

    async def total_stats(self):
        data_name = 'total_stats'
        api_data = self.api_data[data_name]

        self.data['total_kills'] = 0
        self.data['total_deaths'] = 0

        try:
            self.data['total_kills'] = list(filter(lambda x: x['field'] == 'kills', api_data))[0]['sum']
            self.data['total_deaths'] = list(filter(lambda x: x['field'] == 'deaths', api_data))[0]['sum']
        except KeyError:
            pass

    async def matches(self):
        data_name = 'matches'
        api_data = self.api_data[data_name]

        self.data['loosing_streak'] = 0
        self.data['longest_match'] = 0
        self.data['first_match'] = None

        lobby_types = [0, 2, 5, 6, 7, 8, 9]

        try:
            if len(api_data):
                normal_matches = list(filter(lambda x: x['lobby_type'] in lobby_types, api_data))
                mathches = [
                    True
                    if (i['player_slot'] in range(128) and i['radiant_win']) or
                       (i['player_slot'] in range(128, 256) and not i['radiant_win'])
                    else False
                    for i in normal_matches
                ]
                streaks = []
                streak = 0
                for i in mathches:
                    if not i:
                        streak += 1
                    else:
                        streaks.append(streak)
                        streak = 0
                streaks.append(streak)
                self.data['loosing_streak'] = max(streaks)
                self.data['longest_match'] = round(max(i['duration'] for i in normal_matches) / 60)  # minutes
                self.data['first_match'] = datetime.fromtimestamp(normal_matches[-1]['start_time'])
        except KeyError as e:
            print(e)
            pass

    async def wards(self):
        data_name = 'wards'
        api_data = self.api_data[data_name]

        self.data['purchase_ward_observer'] = 0

        try:
            if len(api_data):
                self.data['purchase_ward_observer'] = api_data[0]['purchase_ward_observer']
        except KeyError as e:
            print(e)
            pass

    async def comeback(self):
        data_name = 'comeback'
        api_data = self.api_data[data_name]

        self.data['comeback'] = 0

        try:
            if len(api_data):
                self.data['comeback'] = api_data[0]['comeback']
        except KeyError as e:
            print(e)
            pass

    async def make_api_requests(self):
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.request_api(self.urls[name], name, session)) for name in self.urls]
            return await asyncio.wait(tasks)

    async def parse_data(self):
        tasks = [
            asyncio.create_task(self.most_played_hero()),
            asyncio.create_task(self.worst_hero()),
            asyncio.create_task(self.last_month_hero()),
            asyncio.create_task(self.mmr_games()),
            asyncio.create_task(self.total_games()),
            asyncio.create_task(self.players_info()),
            asyncio.create_task(self.last_match()),
            asyncio.create_task(self.wordcloud()),
            asyncio.create_task(self.total_stats()),
            asyncio.create_task(self.friends()),
            asyncio.create_task(self.matches()),
            asyncio.create_task(self.comeback()),
            asyncio.create_task(self.wards()),
        ]
        return await asyncio.wait(tasks)

    def run(self):
        asyncio.run(self.make_api_requests())
        asyncio.run(self.parse_data())
        return self.data


if __name__ == '__main__':
    data = OpenDotaApi('120150156').run()
