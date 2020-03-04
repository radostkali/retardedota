from dota_api.modules.open_dota_api import OpenDotaApi
from dota_api.const_data import RETARDS_HEROES, OBSCENT_WORDS
from dota_api.modules.db_data import meta_heroes
from pprint import pprint
from datetime import datetime, timedelta
from dota_api.const_data import ACHIEVEMENTS


class AchivesCalculator:
    data = {}
    achievements = ACHIEVEMENTS

    def __init__(self, user_data):
        self.data = user_data
        try:
            self.data['total_games'] = self.data['total_wins'] + self.data['total_loses']
        except KeyError as e:
            print(e)
            print(self.data)

    def one_hero_play(self):
        self.achievements['one_hero_play']['status'] = 0
        one_hero_games = self.data['most_played_hero']['hero_games']
        percent = round(one_hero_games / self.data['total_games'] * 100) if self.data['total_games'] else 0
        if percent >= 10 and one_hero_games > 100:
            self.achievements['one_hero_play']['status'] = 1
            self.achievements['one_hero_play']['details'] = {
                'games': one_hero_games,
                'hero': self.data['most_played_hero']['hero_name'],
                'percent_from_total': percent
            }
            # print(str(percent) + '% games on ' + self.data['most_played_hero']['hero_name'])

    def one_love_hero(self):
        self.achievements['one_love_hero']['status'] = 0
        if self.achievements['one_hero_play']['status'] == 1:
            winrate = self.data['most_played_hero']['hero_winrate']
            print(winrate)
            if winrate <= 40:
                self.achievements['one_hero_play']['status'] = -1
                self.achievements['one_love_hero']['status'] = 1
                self.achievements['one_love_hero']['details'] = {
                    'games': self.data['most_played_hero']['hero_games'],
                    'hero': self.data['most_played_hero']['hero_name'],
                    'winrate': winrate
                }
                # print(f'{winrate}% winrate on {self.data["most_played_hero"]["hero_name"]}')

    def one_hero_abuse(self):
        self.achievements['one_hero_abuse']['status'] = 0
        if self.achievements['one_hero_play']['status'] in [1, -1]:
            winrate = self.data['most_played_hero']['hero_winrate']
            if winrate >= 70:
                self.achievements['one_hero_abuse']['status'] = 1
                self.achievements['one_hero_play']['status'] = -1
                self.achievements['one_hero_abuse']['details'] = {
                    'games': self.data['most_played_hero']['hero_games'],
                    'hero': self.data['most_played_hero']['hero_name'],
                    'winrate': winrate
                }
                # print(f'{winrate}% winrate on {self.data["most_played_hero"]["hero_name"]}')

    def retards_hero_play(self):
        self.achievements['retards_hero_play']['status'] = 0
        if self.achievements['one_hero_play']['status'] in [1, -1] \
                and self.data['most_played_hero']['hero_name'] in RETARDS_HEROES:
            self.achievements['retards_hero_play']['status'] = 1
            self.achievements['one_hero_play']['status'] = -1
            self.achievements['retards_hero_play']['details'] = self.achievements['one_hero_play']['details']
            # print('%s is retarded' % self.data['most_played_hero']['hero_name'])

    def retards_hero_abuse(self):
        self.achievements['retards_hero_abuse']['status'] = 0
        if self.achievements['one_hero_abuse']['status'] == 1 \
                and self.data['most_played_hero']['hero_name'] in RETARDS_HEROES:
            self.achievements['retards_hero_abuse']['status'] = 1
            self.achievements['retards_hero_play']['status'] = -1
            self.achievements['one_hero_abuse']['status'] = -1
            self.achievements['retards_hero_abuse']['details'] = self.achievements['one_hero_abuse']['details']

    def meta_hero_abuse(self):
        self.achievements['meta_hero_abuse']['status'] = 0
        one_hero_games = self.data['last_month_hero']['hero_games']
        percent = round(one_hero_games / self.data['last_month_hero']['total_games'] * 100) \
            if self.data['last_month_hero']['total_games'] else 0
        if percent >= 10 and self.data['last_month_hero']['hero_winrate'] > 70 and \
                self.data['last_month_hero']['hero_games'] >= 10:
            self.achievements['meta_hero_abuse']['status'] = 1
            self.achievements['meta_hero_abuse']['details'] = {
                'hero': self.data['last_month_hero']['hero_name'],
                'games': self.data['last_month_hero']['hero_games'],
                'winrate': self.data['last_month_hero']['hero_winrate']
            }
            # print('%d games on meta %s with %d%% winrate' % (
            #     self.data['last_month_hero']['hero_games'],
            #     self.data['last_month_hero']['hero_name'],
            #     self.data['last_month_hero']['hero_winrate']
            # ))

    def total_looser(self):
        self.achievements['total_looser']['status'] = 0
        if self.data['total_winrate'] < 40:
            self.achievements['total_looser']['status'] = 1
            self.achievements['total_looser']['details']['winrate'] = self.data['total_winrate']
            # print('Total players winrate is %d' % self.data['total_winrate'])

    def newfag(self):
        self.achievements['newfag']['status'] = 0
        if self.data['total_games'] < 100:
            self.achievements['newfag']['status'] = 1
            self.achievements['newfag']['details']['games'] = self.data['total_games']
            # print('Total players games is %d' % self.data['total_games'])

    def syich(self):
        self.achievements['syich']['status'] = 0
        if self.data['total_games'] > 10000:
            self.achievements['syich']['status'] = 1
            self.achievements['syich']['details']['games'] = self.data['total_games']
            # print('Total players games is %d' % self.data['total_games'])

    def bad_internet(self):
        self.achievements['bad_internet']['status'] = 0
        abandoned = round(self.data['total_abandons'] / self.data['total_games'] * 100) \
            if self.data['total_games'] else 0
        if abandoned > 10:
            self.achievements['bad_internet']['status'] = 1
            self.achievements['bad_internet']['details']['games'] = self.data['total_abandons']
            # print('Total players games is %d (%d%%)' % (self.data['total_games'], abandoned))

    def mmr_addict(self):
        self.achievements['mmr_addict']['status'] = 0
        mmr_percent = round(self.data['total_mmr'] / self.data['total_games'] * 100) \
            if self.data['total_games'] else 0
        if mmr_percent > 70:
            self.achievements['mmr_addict']['status'] = 1
            self.achievements['mmr_addict']['details'] = {
                'percent': mmr_percent,
                'games': self.data['total_mmr']
            }
            # print('Total players mmr games is %d (%d%%)' % (self.data['total_mmr'], mmr_percent))

    def worst_hero(self):
        self.achievements['worst_hero']['status'] = 0
        if self.data['worst_hero']:
            self.achievements['worst_hero']['status'] = 1
            self.achievements['worst_hero']['details'] = {
                'hero': self.data['worst_hero']['hero_name'],
                'games': self.data['worst_hero']['hero_games'],
                'winrate': self.data['worst_hero']['hero_winrate'],
            }
            # print('Worst hero is %s (%d games, %d%% winrate)' %
            #       (self.data['worst_hero']['hero_name'],
            #        self.data['worst_hero']['hero_games'],
            #       self.data['worst_hero']['hero_winrate']))

    def donater(self):
        self.achievements['donater']['status'] = 0
        if self.data['dota_plus']:
            self.achievements['donater']['status'] = 1
            # print('Dota plus is connected')

    def bm(self):
        self.achievements['bm']['status'] = 0
        if len(self.data['wordcloud']['words']):
            obscent = [{i: self.data['wordcloud']['words'][i]} for i in self.data['wordcloud']['words']
                       if i.lower() in OBSCENT_WORDS]
            percent = round(sum([sum(i.values()) for i in obscent]) / self.data['wordcloud']['total_words'] * 100)
            if percent >= 3:
                self.achievements['bm']['status'] = 1
                zipped = zip([list(i.keys())[0] for i in obscent], [list(i.values())[0] for i in obscent])
                self.achievements['bm']['details']['top_words'] = sorted(zipped, key=lambda k: k[1])[:3]
                # print('Bad speaking: ' + str(self.achievements['bm']['details']['top_words']))

    def feeder(self):
        self.achievements['feeder']['status'] = 0
        if self.data['total_kills']:
            total = self.data['total_kills'] + self.data['total_deaths']
            percent_kills = round(self.data['total_kills'] / total * 100)
            if percent_kills <= 40:
                self.achievements['feeder']['status'] = 1
                self.achievements['feeder']['details'] = {
                    'kills': self.data['total_kills'],
                    'deaths': self.data['total_deaths'],
                }
                # print('Has %s%% of kills to deaths' % percent_kills)

    def he_is_dead(self):
        self.achievements['he_is_dead']['status'] = 0
        if self.data['last_match']:
            last_match = datetime.utcnow() - self.data['last_match']
            if last_match >= timedelta(weeks=12):
                self.achievements['he_is_dead']['status'] = 1
                self.achievements['he_is_dead']['details']['last_match'] = str(last_match.days)
                # print('He is dead for %s' % str(last_match))

    def humble_guy(self):
        self.achievements['humble_guy']['status'] = 0
        if self.data['loosing_streak']:
            if self.data['loosing_streak'] >= 20:
                self.achievements['humble_guy']['status'] = 1
                self.achievements['humble_guy']['details']['loosing_streak'] = self.data['loosing_streak']
                # print('Has %d loosing streak' % self.data['loosing_streak'])

    def machine(self):
        self.achievements['machine']['status'] = 0
        if self.data['longest_match']:
            if self.data['longest_match'] >= 180:
                self.achievements['machine']['status'] = 1
                self.achievements['machine']['details']['match_duration'] = self.data['longest_match']
                # print('Has match with %d minutes duration' % self.data['longest_match'])

    def oldfag(self):
        self.achievements['oldfag']['status'] = 0
        if self.data['first_match']:
            if self.data['first_match'] <= datetime(2013, 12, 31):
                self.achievements['oldfag']['status'] = 1
                self.achievements['oldfag']['details']['first_match'] = self.data['first_match']
                # print('Old. First match: %s' % self.data['first_match'])

    def eyes_on_the_ass(self):
        self.achievements['eyes_on_the_ass']['status'] = 0
        if self.data['purchase_ward_observer']:
            if self.data['purchase_ward_observer'] >= 50:
                self.achievements['eyes_on_the_ass']['status'] = 1
                self.achievements['eyes_on_the_ass']['details']['wards'] = self.data['purchase_ward_observer']
                # print('Bought %d wards in a game' % self.data['purchase_ward_observer'])

    def comeback(self):
        self.achievements['comeback']['status'] = 0
        if self.data['comeback']:
            if self.data['comeback'] >= 50000:
                self.achievements['comeback']['status'] = 1
                self.achievements['comeback']['details']['comeback'] = self.data['comeback']
                # print('Comeback from %d ' % self.data['comeback'])

    def clear(self):
        status = 1
        for i in self.achievements:
            if self.achievements[i]['status'] == 1 and self.achievements[i]['priority'] != 0:
                status = 0
                break
        self.achievements['clear']['status'] = status

    def run(self):
        if self.data['total_games'] == 0:
            return None
        self.one_hero_play()
        self.one_love_hero()
        self.one_hero_abuse()
        self.retards_hero_play()
        self.retards_hero_abuse()
        self.meta_hero_abuse()
        self.total_looser()
        self.newfag()
        self.syich()
        self.bad_internet()
        self.mmr_addict()
        self.worst_hero()
        self.donater()
        self.bm()
        self.feeder()
        self.he_is_dead()
        self.humble_guy()
        self.machine()
        self.oldfag()
        self.eyes_on_the_ass()
        self.comeback()
        self.clear()
        return self.achievements


if __name__ == '__main__':
    # data = OpenDotaApi('120150156').run()  # me
    # data = OpenDotaApi('111620041').run()  # highest mmr
    data = OpenDotaApi('165406803').run()  # techster
    # data = OpenDotaApi('836727572').run()  # budger
    # data = OpenDotaApi('250114507').run()  # Iceberg
    # data = OpenDotaApi('19672354').run()  # Notail
    # data = OpenDotaApi('43276219').run()  # EE
    # data = OpenDotaApi('132851371').run()  # Ramzes

    data['meta_heroes'] = ['Ogre']

    # pprint(data)
    c = AchivesCalculator(data)
    achievements = c.run()
    pprint(achievements)
