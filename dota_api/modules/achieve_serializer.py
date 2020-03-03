from dota_api.const_data import HEROES_ICONS


prototype = {
    'name': str,
    'detail': str,
    'description': str,
    'achieve_img': str,
    'detail_img': str,
    'rank': int,
}

assets = '/img/cosplay/'


def one_hero_play(achieve):
    name = 'One hero player'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. ' \
                  'It\'s <accent>%d%%</accent> from all games on the account. Hope you enjoy your life.'\
                  % (achieve['details']['games'], achieve['details']['hero'], achieve['details']['percent_from_total'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def one_love_hero(achieve):
    name = 'One love hero'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. ' \
                  'And there is only <accent>%d%%</accent> win rate. Press F.' % \
                  (achieve['details']['games'], achieve['details']['hero'], achieve['details']['winrate'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def one_hero_abuse(achieve):
    name = 'One hero abuser'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. ' \
                  'This is the most played hero on the account.' \
                  'And there is <accent>%d%%</accent> win rate. Fuck you moron.' % \
                  (achieve['details']['games'], achieve['details']['hero'], achieve['details']['winrate'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def retards_hero_play(achieve):
    name = 'Retarded hero player'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on fucking %s. ' \
                  'It\'s <accent>%d%%</accent> from all games on this account.' \
                  ' Why? Why are you doing this?'\
                  % (achieve['details']['games'], achieve['details']['hero'], achieve['details']['percent_from_total'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def retards_hero_abuse(achieve):
    name = 'Retarded hero abuser'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. ' \
                  'This is the most played hero on the account. ' \
                  'And there is <accent>%d%%</accent> win rate. You are the worst. Just die idiotic peace of shame.' % \
                  (achieve['details']['games'], achieve['details']['hero'], achieve['details']['winrate'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def meta_hero_abuse(achieve):
    name = 'Meta heroes abuser'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. ' \
                  'This is the most played hero this month and' \
                  ' there is <accent>%d%%</accent> win rate. The hero is in top ten month hero by win rate. ' \
                  'Good job sucker.' % \
                  (achieve['details']['games'], achieve['details']['hero'], achieve['details']['winrate'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def total_looser(achieve):
    name = 'Total looser'
    detail = '%d%% win rate' % achieve['details']['winrate']
    description = 'The retard has <accent>%d%%</accent> win rate on the account. Is he still playing Dota?' % \
                  (achieve['details']['winrate'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/c/cf/Cinder_Brew_icon.png/' \
                 '120px-Cinder_Brew_icon.png?version=8fb0a5431d758723f2f50627bbf39268'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def newfag(achieve):
    name = 'Newfag'
    detail = '%d games' % achieve['details']['games']
    description = 'The retard has <accent>%d</accent> games on the account. ' \
                  'There is still a chance to escape. Run away.' % \
                  (achieve['details']['games'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/07/Divided_We_Stand_icon.png/' \
                 '120px-Divided_We_Stand_icon.png?version=e339cf3906c859cc21fbbb0752228ad3'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def syich(achieve):
    name = 'No lifer'
    detail = '%d games' % achieve['details']['games']
    description = 'The retard has <accent>%d</accent> games on the account. Wasted.' % \
                  (achieve['details']['games'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/8/8a/Cold_Embrace_icon.png/' \
                 '120px-Cold_Embrace_icon.png?version=ffaa0f5b245d6038fb4ad710bc3122f4'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def bad_internet(achieve):
    name = 'Bad internet connection'
    detail = '%d abandoned games' % achieve['details']['abandoned']
    description = 'The retard has <accent>%d</accent> abandoned games on the account. Man. Please. Fix it.' % \
                  (achieve['details']['games'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/4/4d/Charge_of_Darkness_icon.png/' \
                 '120px-Charge_of_Darkness_icon.png?version=680c763375bcebb049622a6b3cb06763'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def mmr_addict(achieve):
    name = 'MMR addicted'
    detail = '%d%% of mmr games' % achieve['details']['percent']
    description = 'The retard has <accent>%d</accent> mmr games. ' \
                  'It\'s <accent>%d%%</accent> from all games on this account.' \
                  ' Hope mom is proud of you.' % \
                  (achieve['details']['games'], achieve['details']['percent'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/6a/Berserker%27s_Blood_icon.png/' \
                 '120px-Berserker%27s_Blood_icon.png?version=515968917110730f08c1340ef831baa8'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def worst_hero(achieve):
    name = 'Worst hero ever'
    detail = achieve['details']['hero']
    description = 'The retard has <accent>%d</accent> games on <accent>%s</accent>. And there is <accent>%d%%</accent>' \
                  ' win rate. Stop. Don\'t pick it.' % \
                  (achieve['details']['games'], achieve['details']['hero'], achieve['details']['winrate'])
    detail_img = [i[achieve['details']['hero']] for i in HEROES_ICONS if achieve['details']['hero'] in i][0]
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def donater(achieve):
    name = 'Donater'
    detail = 'Real businessman'
    description = 'The retard pays Gaben for Dota Plus. Dota Plus, money minus.'
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/9/94/Greevil%27s_Greed_icon.png/' \
                 '120px-Greevil%27s_Greed_icon.png?version=063fc85ba6e41d45fb6384b45dd7b045'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def bm(achieve):
    name = 'BM'
    detail = 'Top word: %s' % achieve['details']['top_words'][0][0]
    description = 'The retard has an excellent education and comes from an aristocratic family. ' \
                  'Here is a list of his frequently used words: '
    for i in achieve['details']['top_words']:
        description = description + '<accent>%s</accent>, ' % i[0]
    description = description[:-2] + '.'
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/6/67/Plague_Ward_icon.png/' \
                 '120px-Plague_Ward_icon.png?version=0cb60837b23704316a40f40337d86fe3'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def feeder(achieve):
    name = 'Feeder'
    detail = 'In love with death'
    description = 'The retard has <accent>%d</accent> deaths and only ' \
                  '<accent>%d</accent> kills from all matches on the account.' % \
                  (achieve['details']['deaths'], achieve['details']['kills'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/17/Heartstopper_Aura_icon.png/' \
                 '120px-Heartstopper_Aura_icon.png?version=46f54e33a1726c875035b5dca34accc3'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def he_is_dead(achieve):
    name = 'He\'s dead'
    detail = 'Don\'t look back'
    description = 'The retard played his last match <accent>%s</accent> days ago. Rejoice for him.' % \
                  (achieve['details']['last_match'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/d/dd/Reincarnation_%28Skeleton_King%29_icon.png'\
                 '/120px-Reincarnation_%28Skeleton_King%29_icon.png?version=b40e8772a5e23228298a1e85a4eccd38'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def humble_guy(achieve):
    name = 'Humble guy'
    detail = '%d losses in a row' % achieve['details']['loosing_streak']
    description = 'The retard has a beautiful <accent>%d-games</accent> loosing streak. ' \
                  'This is no longer willpower. This is humility.' % \
                  (achieve['details']['loosing_streak'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8d/Minefield_Sign_icon.png?' \
                 'version=714ed980c7c0f176b1591c4ec03d17f7'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def machine(achieve):
    name = 'Machine'
    detail = '%d minutes match' % achieve['details']['match_duration']
    description = 'The retard played <accent>%d minutes</accent> duration game. ' \
                  'Retard: Become robot.' % \
                  (achieve['details']['match_duration'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/f/f5/March_of_the_Machines_icon.png/' \
                 '120px-March_of_the_Machines_icon.png?version=96b93300423c335d1c65c7fa850ef3c1'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def oldfag(achieve):
    name = 'Oldfag'
    detail = 'Here from %s' % achieve['details']['first_match'].strftime('%Y')
    description = 'The retard first played Dota 2 in <accent>%s</accent>. ' \
                  'How are you doing ancient?' % \
                  (achieve['details']['first_match'].date())
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/0/0a/Bash_%28Roshan%29_icon.png/' \
                 '120px-Bash_%28Roshan%29_icon.png?version=6600845c0280277e05075224f256fa63'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def eyes_on_the_ass(achieve):
    name = 'Eyes on the ass'
    detail = '%d wards' % achieve['details']['wards']
    description = 'The retard bought <accent>%d</accent> observer wards in one game. ' \
                  'Look at you and wipe the sweat.' % \
                  (achieve['details']['wards'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f6/Observer_Ward_icon.png?' \
                 'version=112131780ebabfef26bb8b84c6ae8d5f'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def comeback(achieve):
    name = 'Comebacker'
    detail = 'From %d' % achieve['details']['comeback']
    description = 'The retard made comeback from <accent>%d</accent> gold. ' \
                  'Dark magic is involved here.' % \
                  (achieve['details']['comeback'])
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/1/16/Time_Lapse_icon.png/' \
                 '120px-Time_Lapse_icon.png?version=1f492478b3d359816cf47c9e3db8a768'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


def clear(achieve):
    name = 'Holy doter'
    detail = 'Bless you'
    description = 'He\'s not retarded. Perhaps.'
    detail_img = 'https://gamepedia.cursecdn.com/dota2_gamepedia/thumb/a/a4/Illuminate_%28Spirit_Form%29_icon.png/' \
                 '120px-Illuminate_%28Spirit_Form%29_icon.png?version=53a2a37f85d73b1ecac608c8cab2c735'
    rank = achieve['priority']
    response = {
        'name': name,
        'detail': detail,
        'description': description,
        'detail_img': detail_img,
        'rank': rank,
    }
    return response


functions = {
    'one_hero_play': one_hero_play,
    'one_love_hero': one_love_hero,
    'one_hero_abuse': one_hero_abuse,
    'retards_hero_play': retards_hero_play,
    'retards_hero_abuse': retards_hero_abuse,
    'meta_hero_abuse': meta_hero_abuse,
    'total_looser': total_looser,
    'newfag': newfag,
    'syich': syich,
    'bad_internet': bad_internet,
    'mmr_addict': mmr_addict,
    'worst_hero': worst_hero,
    'donater': donater,
    'bm': bm,
    'feeder': feeder,
    'he_is_dead': he_is_dead,
    'humble_guy': humble_guy,
    'machine': machine,
    'oldfag': oldfag,
    'eyes_on_the_ass': eyes_on_the_ass,
    'comeback': comeback,
    'clear': clear,
}


def serialize(achievements):
    achievements = [i for i in achievements.values() if i['status'] == 1]
    serialized = [functions[i['name']](i) for i in achievements]
    return serialized


if __name__ == '__main__':
    achieve_ = {'one_hero_play': {'priority': 3, 'name': 'one_hero_play', 'status': -1, 'details': {'games': 1804, 'hero': 'Techies', 'percent_from_total': 47}}, 'one_love_hero': {'priority': 2, 'name': 'one_love_hero', 'status': 0, 'details': {'games': None, 'hero': None, 'winrate': None}}, 'one_hero_abuse': {'priority': 4, 'name': 'one_hero_abuse', 'status': 0, 'details': {'hero': None, 'games': None, 'winrate': None}}, 'retards_hero_play': {'priority': 4, 'name': 'retards_hero_play', 'status': 1, 'details': {'games': 1804, 'hero': 'Techies', 'percent_from_total': 47}}, 'retards_hero_abuse': {'priority': 5, 'name': 'retards_hero_abuse', 'status': 0, 'details': {'hero': None, 'games': None, 'winrate': None}}, 'meta_hero_abuse': {'priority': 4, 'name': 'meta_hero_abuse', 'status': 0, 'details': {'games': None, 'hero': None, 'winrate': None}}, 'total_looser': {'priority': 2, 'name': 'total_looser', 'status': 0, 'details': {'winrate': None}}, 'newfag': {'priority': 1, 'name': 'newfag', 'status': 0, 'details': {'games': None}}, 'syich': {'priority': 1, 'name': 'syich', 'status': 0, 'details': {'games': None}}, 'bad_internet': {'priority': 3, 'name': 'bad_internet', 'status': 0, 'details': {'abandoned': None}}, 'mmr_addict': {'priority': 2, 'name': 'mmr_addic t', 'status': 0, 'details': {'percent': None, 'games': None}}, 'worst_hero': {'priority': 2, 'name': 'worst_hero', 'status': 0, 'details': {'hero': None, 'games': None, 'winrate': None}}, 'donater': {'priority': 1, 'name': 'donater', 'status': 0}, 'bm': {'priority': 3, 'name': 'bm', 'status': 0, 'details': {'top_words': []}}, 'feeder': {'priority': 3, 'name': 'feeder', 'status': 0, 'details': {'kills': None, 'deaths': None}}, 'he_is_dead': {'priority': 3, 'name': 'he_is_dead', 'status': 0, 'details': {'last_match': '253'}}, 'clear': {'priority': 0, 'name': 'clear', 'status': 0}}
    print(serialize(achieve_))
