from dota_api.const_data import STEAM_API
import requests
import json


class GetSteamId:
    steam_api = None

    def __init__(self):
        self.steam_api = STEAM_API

    def get_id_by_vanity_name(self, vanity_name):
        url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s' % \
              (self.steam_api, vanity_name)
        r = requests.get(url)
        if r.status_code == 200:
            return int(json.loads(r.content)['response']['steamid'])
        else:
            return None

    def define_id(self, string):
        if string is None:
            return None
        dota_id = None
        try:
            undefined_id = int(string)
            if undefined_id > 76561197960265728:
                dota_id = undefined_id - 76561197960265728
            else:
                dota_id = undefined_id
        except ValueError:
            try:
                splited_url = string.split('/')
                while splited_url[-1] == '':
                    splited_url = splited_url[:-1]
                if 'profiles' in splited_url[:-1]:
                    dota_id = int(splited_url[-1]) - 76561197960265728
                elif 'id' in splited_url[:-1]:
                    vanity_name = splited_url[-1]
                    dota_id = self.get_id_by_vanity_name(vanity_name) - 76561197960265728
                elif 'players' in splited_url[:-1]:
                    dota_id = int(splited_url[-1])
            except Exception:
                return None
        return dota_id


if __name__ == '__main__':
    string = 'https://steamcommunity.com/profiles/76561198080415884/'
    dota_id = GetSteamId().define_id(string)
    print(dota_id)
