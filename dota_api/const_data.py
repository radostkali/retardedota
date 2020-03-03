STEAM_API = 'F075401D54564A3AAF185EED395B5C4E'

RETARDS_HEROES = ['Techies', 'Pudge', 'Broodmother', 'Void Spirit', 'Riki', 'Skywrath Mage']

ACHIEVEMENTS = {
    'one_hero_play':
        {
            'priority': 3,
            'name': 'one_hero_play',
            'status': None,
            'details':
                {
                    'games': None,
                    'hero': None,
                    'percent_from_total': None
                }
        },
    'one_love_hero':
        {
            'priority': 2,
            'name': 'one_love_hero',
            'status': None,
            'details':
                {
                    'games': None,
                    'hero': None,
                    'winrate': None
                }
        },
    'one_hero_abuse':
        {
            'priority': 4,
            'name': 'one_hero_abuse',
            'status': None,
            'details':
                {
                    'hero': None,
                    'games': None,
                    'winrate': None
                }
        },
    'retards_hero_play':
        {
            'priority': 4,
            'name': 'retards_hero_play',
            'status': None,
            'details':
                {
                    'games': None,
                    'hero': None,
                    'percent_from_total': None
                }
        },
    'retards_hero_abuse':
        {
            'priority': 5,
            'name': 'retards_hero_abuse',
            'status': None,
            'details':
                {
                    'hero': None,
                    'games': None,
                    'winrate': None
                }
        },
    'meta_hero_abuse':
        {
            'priority': 4,
            'name': 'meta_hero_abuse',
            'status': None,
            'details':
                {
                    'games': None,
                    'hero': None,
                    'winrate': None
                }
        },
    'total_looser':
        {
            'priority': 2,
            'name': 'total_looser',
            'status': None,
            'details':
                {
                    'winrate': None
                }
        },
    'newfag':
        {
            'priority': 1,
            'name': 'newfag',
            'status': None,
            'details':
                {
                    'games': None
                }
        },
    'syich':
        {
            'priority': 1,
            'name': 'syich',
            'status': None,
            'details':
                {
                    'games': None
                }
        },
    'bad_internet':
        {
            'priority': 3,
            'name': 'bad_internet',
            'status': None,
            'details':
                {
                    'abandoned': None
                }
        },
    'mmr_addict':
        {
            'priority': 2,
            'name': 'mmr_addict',
            'status': None,
            'details':
                {
                    'percent': None,
                    'games': None
                }
        },
    'worst_hero':
        {
            'priority': 2,
            'name': 'worst_hero',
            'status': None,
            'details':
                {
                    'hero': None,
                    'games': None,
                    'winrate': None
                }
        },
    'donater':
        {
            'priority': 1,
            'name': 'donater',
            'status': None
        },
    'bm':
        {
            'priority': 3,
            'name': 'bm',
            'status': None,
            'details': {
                'top_words': []
            }
        },
    'feeder':
        {
            'priority': 3,
            'name': 'feeder',
            'status': None,
            'details': {
                'kills': None,
                'deaths': None
            }
        },
    'he_is_dead':
        {
            'priority': 0,
            'name': 'he_is_dead',
            'status': None,
            'details': {
                'last_match': None
            }
        },
    'clear':
        {
            'priority': 0,
            'name': 'clear',
            'status': None,
        },
    'humble_guy':
        {
            'priority': 1,
            'name': 'humble_guy',
            'status': None,
            'details': {
                'loosing_streak': None
            }
        },
    'machine':
        {
            'priority': 3,
            'name': 'machine',
            'status': None,
            'details': {
                'match_duration': None
            }
        },
    'oldfag':
        {
            'priority': 0,
            'name': 'oldfag',
            'status': None,
            'details': {
                'first_match': None
            }
        },
    'eyes_on_the_ass':
        {
            'priority': 2,
            'name': 'eyes_on_the_ass',
            'status': None,
            'details': {
                'wards': None
            }
        },
    'comeback':
        {
            'priority': 0,
            'name': 'comeback',
            'status': None,
            'details': {
                'comeback': None
            }
        },

}

HEROES_ICONS = [{'Abaddon': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cc/Abaddon_minimap_icon.png?version=c9c278dc7a941fc07031d553906ef9d7'}, {'Alchemist': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1e/Alchemist_minimap_icon.png?version=8b6f3d7acbc478e76dc169f1b103329a'}, {'Ancient Apparition': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/25/Ancient_Apparition_minimap_icon.png?version=e3becf8cdf1503d69b7df8d34b6ccfe3'}, {'Anti-Mage': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/30/Anti-Mage_minimap_icon.png?version=a9126259d75fb8cb7cab5d968844ec09'}, {'Arc Warden': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e9/Arc_Warden_minimap_icon.png?version=2108ccde76ccd545797f4527c2f64f59'}, {'Axe': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f7/Axe_minimap_icon.png?version=db9be3e59e65d6e8d1cd483fd3b4386e'}, {'Bane': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0d/Bane_minimap_icon.png?version=e03643ab38abb02479508f69e536797f'}, {'Batrider': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0d/Batrider_minimap_icon.png?version=9dc6b2b3519c6d4f6d459db8498a9909'}, {'Beastmaster': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5c/Beastmaster_minimap_icon.png?version=275961e6c15455bebabc6b07c009f783'}, {'Bloodseeker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/57/Bloodseeker_minimap_icon.png?version=c0c7d8fd84c3d049ee3432b29f7cd3a7'}, {'Bounty Hunter': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9c/Bounty_Hunter_minimap_icon.png?version=4914405e8ba19df2e6b193ae378db02c'}, {'Brewmaster': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9b/Brewmaster_minimap_icon.png?version=6a42d3f5675c51576f5a7892f7e132a2'}, {'Bristleback': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a8/Bristleback_minimap_icon.png?version=d841167e40697bf90339b0a440e63e56'}, {'Broodmother': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/19/Broodmother_minimap_icon.png?version=cd2b7c20dde116e90139d6e132cba535'}, {'Centaur Warrunner': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5e/Centaur_Warrunner_minimap_icon.png?version=a04234cb2eb421ab9221a41c88a97da1'}, {'Chaos Knight': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9f/Chaos_Knight_minimap_icon.png?version=fdf6d6a1bd3ad984a41fce9f6ac7ff98'}, {'Chen': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/fc/Chen_minimap_icon.png?version=8708977032b37112575fc93ae51e9286'}, {'Clinkz': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/16/Clinkz_minimap_icon.png?version=86476fd5928bfc31aa6e1d71a5d46ed6'}, {'Clockwerk': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/12/Clockwerk_minimap_icon.png?version=b3b548c7089777c8db9932977841db55'}, {'Crystal Maiden': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b4/Crystal_Maiden_minimap_icon.png?version=da890fd626627fce6a1d30279b2e830f'}, {'Dark Seer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5a/Dark_Seer_minimap_icon.png?version=fad0973710daf7bb2a870a85ec359044'}, {'Dark Willow': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/47/Dark_Willow_minimap_icon.png?version=58d08f7aece6f67ad205b6869fa06237'}, {'Dazzle': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3b/Dazzle_minimap_icon.png?version=c7e866f5928190716d3238feb330c9ef'}, {'Death Prophet': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5d/Death_Prophet_minimap_icon.png?version=d308422e43a481d94a61a11f196f756a'}, {'Disruptor': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b9/Disruptor_minimap_icon.png?version=5ca58d2fb8197c6bcec69ad1b01e0c36'}, {'Doom': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/96/Doom_minimap_icon.png?version=39fe0265c418691f1c6159973e27bdc2'}, {'Dragon Knight': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/21/Dragon_Knight_minimap_icon.png?version=aea6131a77be71af69ffe7b87052d996'}, {'Drow Ranger': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/63/Drow_Ranger_minimap_icon.png?version=5a03f5ed7ec95c9a8ee1b203780e976a'}, {'Earth Spirit': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1f/Earth_Spirit_minimap_icon.png?version=5aa6736d89defd39b96dfb6cf1b430bc'}, {'Earthshaker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/42/Earthshaker_minimap_icon.png?version=a91966f35c358c765f592f78050e6a1c'}, {'Elder Titan': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9f/Elder_Titan_minimap_icon.png?version=53f5235961044534b30062d50e5d877f'}, {'Ember Spirit': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/fc/Ember_Spirit_minimap_icon.png?version=fa21609415641186a0e346b7ae675ca0'}, {'Enchantress': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ef/Enchantress_minimap_icon.png?version=243cb264081de5201bb4a50179c2159b'}, {'Enigma': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/03/Enigma_minimap_icon.png?version=0812c1530639012bb07691f4eb23ed10'}, {'Faceless Void': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8e/Faceless_Void_minimap_icon.png?version=f4efb4c4a25b6db01078ab20bfe6c321'}, {'Grimstroke': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bd/Grimstroke_minimap_icon.png?version=de34c5ffe784b29a388966757b5bc870'}, {'Gyrocopter': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f8/Gyrocopter_minimap_icon.png?version=bb4e432b7ddcea36a3d16a26d69c80f3'}, {'Huskar': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5b/Huskar_minimap_icon.png?version=c20b5c77ab8e2713b950347e75823d05'}, {'Invoker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7d/Invoker_minimap_icon.png?version=bc35d4f9454b804d05f93fc3bf5d9193'}, {'Io': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/86/Io_minimap_icon.png?version=9d918768c3b893df662714a952197c16'}, {'Jakiro': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b6/Jakiro_minimap_icon.png?version=014e74d79578feeb201a6bf42f8f7847'}, {'Juggernaut': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b2/Juggernaut_minimap_icon.png?version=4c0c536e5a662a5f5da50d58db880683'}, {'Keeper of the Light': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/76/Keeper_of_the_Light_minimap_icon.png?version=b760990eccc8f85eab818651fcf8214f'}, {'Kunkka': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5b/Kunkka_minimap_icon.png?version=983dc510d491eea2b061ab8ab3f7dc73'}, {'Legion Commander': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/10/Legion_Commander_minimap_icon.png?version=e98f5de9d8c78d784a3c486763a6f5cb'}, {'Leshrac': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c8/Leshrac_minimap_icon.png?version=95f4f3ca8e94a21149a9b64b07c354d2'}, {'Lich': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/08/Lich_minimap_icon.png?version=c9e43d4b23e4bbbb296b9f8f61f49355'}, {'Lifestealer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/74/Lifestealer_minimap_icon.png?version=b35526b96a716e532d775ce512c70aac'}, {'Lina': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/44/Lina_minimap_icon.png?version=411ec1ddf6bf0ad033e9a173d43f0b93'}, {'Lion': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/13/Lion_minimap_icon.png?version=eed65a79ddc3c88b1d8a6fc402039ba2'}, {'Lone Druid': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/08/Lone_Druid_minimap_icon.png?version=f48a126af8307f23f1e8ff48fa29ae59'}, {'Luna': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8c/Luna_minimap_icon.png?version=27e8c77e37ae743a48888eaac023e0b1'}, {'Lycan': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4f/Lycan_minimap_icon.png?version=07cce74ed8726787b301f91a835cce77'}, {'Magnus': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7f/Magnus_minimap_icon.png?version=39add4d2b3bea6a0bdb0e0959fa8b0cb'}, {'Mars': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6c/Mars_minimap_icon.png?version=83420a0949cdd6e2e4ef302355d8147c'}, {'Medusa': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/64/Medusa_minimap_icon.png?version=ceee8c149786dd7d60ad8257e47fb8cc'}, {'Meepo': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/17/Meepo_minimap_icon.png?version=fafb00c32e7f7a6da9644d89f5bdf8ec'}, {'Mirana': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b3/Mirana_minimap_icon.png?version=09f360d7f1300654921819cf61f82dc1'}, {'Monkey King': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/76/Monkey_King_minimap_icon.png?version=28c1848bdb886256c9105e06b64a3bf1'}, {'Morphling': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/13/Morphling_minimap_icon.png?version=80484acd87ec38efb07c5e76bb1f5263'}, {'Naga Siren': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6c/Naga_Siren_minimap_icon.png?version=f5136b41cc4b263edf3cc12340242ed1'}, {"Nature's Prophet": 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a4/Nature%27s_Prophet_minimap_icon.png?version=7f5d1ed4a0fa1c1deaaaada0ceb9da83'}, {'Necrophos': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/af/Necrophos_minimap_icon.png?version=befaf601c799781310d313bbf831aff8'}, {'Night Stalker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7f/Night_Stalker_minimap_icon.png?version=d61eee99e5689658b4fe0e9cc92efc12'}, {'Nyx Assassin': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/aa/Nyx_Assassin_minimap_icon.png?version=563e30257b87d670d5cdb5479fc5cb41'}, {'Ogre Magi': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/55/Ogre_Magi_minimap_icon.png?version=f566546a3dc686aec3c87534e37ccb61'}, {'Omniknight': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/05/Omniknight_minimap_icon.png?version=3f1bd08e6cf8cda23b9c36b4aa15147e'}, {'Oracle': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/61/Oracle_minimap_icon.png?version=38b9ffc27d2950a543c13a78111a8be4'}, {'Outworld Devourer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/28/Outworld_Devourer_minimap_icon.png?version=fd7d0ec404e4bdb83950c4c10741a07c'}, {'Pangolier': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/80/Pangolier_minimap_icon.png?version=4200308eb85621c70debde792bb5efbc'}, {'Phantom Assassin': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c9/Phantom_Assassin_minimap_icon.png?version=b53d999894b0b2e70a2d80f14baded31'}, {'Phantom Lancer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f9/Phantom_Lancer_minimap_icon.png?version=6a09614045af60885b11af3ab0dd928e'}, {'Phoenix': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/21/Phoenix_minimap_icon.png?version=740203b2905840eee8fda6b8d6a6d6e0'}, {'Puck': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cf/Puck_minimap_icon.png?version=23649d334ee1775eb7559e0b7febb88b'}, {'Pudge': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/55/Pudge_minimap_icon.png?version=e9f2d6945ca53b69e16dc7f51d691359'}, {'Pugna': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ab/Pugna_minimap_icon.png?version=c0cb75a88949671b39f46f43344f905c'}, {'Queen of Pain': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0f/Queen_of_Pain_minimap_icon.png?version=1d31a33f448e4f9eed3f81a6c1b75fb0'}, {'Razor': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2b/Razor_minimap_icon.png?version=d62c9825e3566f8551c6181d26121e51'}, {'Riki': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a4/Riki_minimap_icon.png?version=645aab1a30eb61c8367f0d306b504e14'}, {'Rubick': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/61/Rubick_minimap_icon.png?version=92aa8b442f812dbe56720662874e1516'}, {'Sand King': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9f/Sand_King_minimap_icon.png?version=2b963b3962ec5403867efa90b0e7a2ce'}, {'Shadow Demon': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/35/Shadow_Demon_minimap_icon.png?version=e040e55385d89594b12f23363a837f52'}, {'Shadow Fiend': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/00/Shadow_Fiend_minimap_icon.png?version=b4429679437211c98599bd8dfad8bc93'}, {'Shadow Shaman': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7e/Shadow_Shaman_minimap_icon.png?version=d61c783b4a082cc8062672f05e97ac3a'}, {'Silencer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0f/Silencer_minimap_icon.png?version=76041a91b75fea5dbea2bbe2e9d8a2cb'}, {'Skeleton King': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ae/Skeleton_King_minimap_icon.png?version=440f43e57d4b96865bd114e02c0ce671'}, {'Skywrath Mage': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/84/Skywrath_Mage_minimap_icon.png?version=c2e79d3133073d92754b289992ebb7d0'}, {'Slardar': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ef/Slardar_minimap_icon.png?version=0c53bc59007cc0cd319f0c6e0bc1e93c'}, {'Slark': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1c/Slark_minimap_icon.png?version=77c7a318551d5206181d5df31305a2ff'}, {'Snapfire': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e1/Snapfire_minimap_icon.png?version=6367834aa982d5c24937df65f03cf2ec'}, {'Sniper': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f1/Sniper_minimap_icon.png?version=78d1dfd90c4c9e376dc3c61795eb4b29'}, {'Spectre': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/64/Spectre_minimap_icon.png?version=afa506a97c57e7e9de28034d5e2a61b0'}, {'Spirit Breaker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/90/Spirit_Breaker_minimap_icon.png?version=28aeadae69499d7582d852225a23c814'}, {'Storm Spirit': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d6/Storm_Spirit_minimap_icon.png?version=886d9073992b04cbed2627f6707b11f6'}, {'Sven': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1c/Sven_minimap_icon.png?version=03dc1cd3cf971397f2cce4f1fe022725'}, {'Techies': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0c/Techies_minimap_icon.png?version=c370d69ad5d8345b791d527b23486d12'}, {'Templar Assassin': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6b/Templar_Assassin_minimap_icon.png?version=afd0e32f7db4cac6a5215c09447976c1'}, {'Terrorblade': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/72/Terrorblade_minimap_icon.png?version=79dc58d2cb639e730a8fd27ee9c0f6bc'}, {'Tidehunter': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d4/Tidehunter_minimap_icon.png?version=0b8e42c8dd518044c08640c42d7cac8d'}, {'Timbersaw': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/49/Timbersaw_minimap_icon.png?version=3a9a12c2a3cd16e8988cb149b3fa9ef0'}, {'Tinker': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1b/Tinker_minimap_icon.png?version=2670897aabc7ecdd9891046e2e0d696f'}, {'Tiny': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b2/Tiny_minimap_icon.png?version=d156ac2ce1398854569c0a6c4e762869'}, {'Treant Protector': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8f/Treant_Protector_minimap_icon.png?version=1c9847f8d0b76a7de6bb52262a4da53d'}, {'Troll Warlord': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a2/Troll_Warlord_minimap_icon.png?version=21f841d4447a6ce9cc990fd85e8f0d3f'}, {'Tusk': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c3/Tusk_minimap_icon.png?version=71a26ffafbef322d1916488f718d6d77'}, {'Underlord': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/29/Underlord_minimap_icon.png?version=bf6be887ccf596eb4effb99b69319374'}, {'Undying': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8a/Undying_minimap_icon.png?version=fc75be5c84502d4488b00252f43e5c11'}, {'Ursa': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ee/Ursa_minimap_icon.png?version=87085ea641dbc047c43d54f92a5e579e'}, {'Vengeful Spirit': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/09/Vengeful_Spirit_minimap_icon.png?version=87683fc18a59bd4a7412d451f220bd92'}, {'Venomancer': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/95/Venomancer_minimap_icon.png?version=71c512f03aa66b08df4dfadc6634389d'}, {'Viper': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cb/Viper_minimap_icon.png?version=c048293f62d3fe28207b067e9e1a0bb1'}, {'Visage': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2f/Visage_minimap_icon.png?version=e68a184def6d614b0468031b291c3bfc'}, {'Void Spirit': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/02/Void_Spirit_minimap_icon.png?version=600d4ddcb1336639dbd672abf0cd5cea'}, {'Warlock': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d3/Warlock_minimap_icon.png?version=386f7f195b8377f758dcc1e79c402938'}, {'Weaver': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d5/Weaver_minimap_icon.png?version=e17627d806ad76843cc01ef5bab99424'}, {'Windranger': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/df/Windranger_minimap_icon.png?version=cf8e182455f863016c33fdda719ef336'}, {'Winter Wyvern': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/06/Winter_Wyvern_minimap_icon.png?version=2305a44b3909c2f8b225499e3b41f1e9'}, {'Witch Doctor': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b6/Witch_Doctor_minimap_icon.png?version=3d2f24258ca98239972c708c7fac1374'}, {'Wraith King': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/22/Wraith_King_minimap_icon.png?version=8d3bd439fe901beec12eceb3753925c7'}, {'Zeus': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3a/Zeus_minimap_icon.png?version=612201e943577aed525fd9b7961bfe0a'}]

EMOTICONS = [{'Emoticon blush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4f/Emoticon_blush.gif?version=c2b3e3b72451c2d9332eaf0416defc9b'}, {'Emoticon cheeky.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/19/Emoticon_cheeky.gif?version=c1364fa001eb8bf0880116611bff5367'}, {'Emoticon cool.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ec/Emoticon_cool.gif?version=c9fbe6a76e463250b14e0ad468138a58'}, {'Emoticon crazy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cb/Emoticon_crazy.gif?version=2127132e0eb2816070198ce7eacbe04d'}, {'Emoticon cry.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/16/Emoticon_cry.gif?version=fd56e970eec8d3d589ffbcfeb7d96718'}, {'Emoticon disapprove.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ac/Emoticon_disapprove.gif?version=4aabd5e22b878598219435e4a3a71ec6'}, {'Emoticon doubledamage.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/09/Emoticon_doubledamage.gif?version=8d2f436eb372a324f015dc1cc2353d1d'}, {'Emoticon facepalm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/00/Emoticon_facepalm.gif?version=b6499085795ead6f5d71cfae55748e96'}, {'Emoticon happytears.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d9/Emoticon_happytears.gif?version=f2a268957172bb66562c4f236a838d59'}, {'Emoticon haste.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ea/Emoticon_haste.gif?version=1ab09768368705b24f481f0f644c4807'}, {'Emoticon hex.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bc/Emoticon_hex.gif?version=00091a7ca4982862f2f13cf5430f2b51'}, {'Emoticon highfive.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d9/Emoticon_highfive.gif?version=63ff5c706d8533cc8c4ecf5c1822c674'}, {'Emoticon huh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c9/Emoticon_huh.gif?version=4eed90b7d018ed29f735d50dce1431c9'}, {'Emoticon hush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/af/Emoticon_hush.gif?version=09d0bdbd69fe7757425de4127c147520'}, {'Emoticon illusion.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bc/Emoticon_illusion.gif?version=67d98ce0a9b40114a85686b8348240b6'}, {'Emoticon invisbility.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/66/Emoticon_invisbility.gif?version=769f5d26fcc0dfbbad880c8a44fe38e1'}, {'Emoticon laugh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/af/Emoticon_laugh.gif?version=82c6956e1d38f005c69b3023ee451462'}, {'Emoticon rage.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e4/Emoticon_rage.gif?version=ad2b266571a03d8ee8efb69893cc8e3f'}, {'Emoticon regeneration.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/61/Emoticon_regeneration.gif?version=b618f6cd0079c6ba752d7f310c8448c8'}, {'Emoticon sad.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b8/Emoticon_sad.gif?version=d8ff4455e84666e5f4b9091c66c78616'}, {'Emoticon sick.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/17/Emoticon_sick.gif?version=01d4ad648492309d2ad71b17f820abca'}, {'Emoticon sleeping.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ed/Emoticon_sleeping.gif?version=30f2f9bab6365f141ea3e646bd087754'}, {'Emoticon smile.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f2/Emoticon_smile.gif?version=925c1ee1d499d07ead0eca6bf263faed'}, {'Emoticon surprise.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d9/Emoticon_surprise.gif?version=4f5331202388497ed3031ee9080b8e49'}, {'Emoticon wink.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/65/Emoticon_wink.gif?version=840a099cc0ca92e7cc937a4d3420ad3f'}, {'TI4 copper.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/86/TI4_copper.gif?version=d39d6cac271e3db3aa7096fce8964616'}, {'TI4 bronze.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a9/TI4_bronze.gif?version=6b696bc15986461dbf1fdf2cfd652dfb'}, {'TI4 silver.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6b/TI4_silver.gif?version=376674b6b931975e59b0f9618d076249'}, {'TI4 gold.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ea/TI4_gold.gif?version=62f089caef0dceb6f3a02dfb5c63bd59'}, {'TI4 platinum.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/04/TI4_platinum.gif?version=95c320f4e19ac1591b95d5c98b1d11ee'}, {'TI4 diamond.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/54/TI4_diamond.gif?version=278c0449afa80264a402b298feb94a86'}, {'Emoticon cocky.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/90/Emoticon_cocky.gif?version=08cb9c79d79f0438a42ce80675e58d9c'}, {'Emoticon devil.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/18/Emoticon_devil.gif?version=6a7c8ea40fdb9d08858075aff4bbbc91'}, {'Emoticon happy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/be/Emoticon_happy.gif?version=e29dafc4dd4ece80c30f8967ddee481b'}, {'Emoticon thinking.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f5/Emoticon_thinking.gif?version=bcaa98da2151bf4f4d9f5e80e4749a38'}, {'Emoticon tp.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/99/Emoticon_tp.gif?version=46e4ae7d8504c530283d14f6812ee41f'}, {'Emoticon salty.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Emoticon_salty.gif?version=4be471268d40a2d81ab56ac156481f80'}, {'Emoticon angel.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f9/Emoticon_angel.gif?version=5e8dcb82630cf5f879195b6b1ae35d2c'}, {'Emoticon blink.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a6/Emoticon_blink.gif?version=1bbf9a5b6c56c58738b5db8d54e1d474'}, {'Emoticon snot.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d6/Emoticon_snot.gif?version=303a36531a63e7cd505ee305d72e1a0b'}, {'Emoticon stunned.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/03/Emoticon_stunned.gif?version=4cab5364656c85ba86525444c2406b41'}, {'Emoticon disappear.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8b/Emoticon_disappear.gif?version=8e5063c53a48f670f14ade06879c1e4f'}, {'Emoticon fire.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/be/Emoticon_fire.gif?version=aa7ec0e785c308da09f86afb350ff674'}, {'Emoticon bountyrune.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/86/Emoticon_bountyrune.gif?version=c49dc5f9e591623f7284269e95a988c9'}, {'Emoticon troll.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8e/Emoticon_troll.gif?version=08a2b26c7932296cab3db16bfabe1e57'}, {'Emoticon gross.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/86/Emoticon_gross.gif?version=002e25cb482ef3391ac0fe9379e2c293'}, {'Emoticon ggdire.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/61/Emoticon_ggdire.gif?version=fd240047f919e1e6ce61fe6c88387143'}, {'Emoticon ggradiant.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4f/Emoticon_ggradiant.gif?version=95d91d565cfd7ebd30baf92603a070be'}, {'Emoticon yolo.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4f/Emoticon_yolo.gif?version=fd21f0d27ee97d098cbcaf6c5b5cfa5e'}, {'Emoticon throwgame.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9c/Emoticon_throwgame.gif?version=f3d8371f0271a81ce9732227a4e47d8e'}, {'Emoticon aegis2015.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ae/Emoticon_aegis2015.gif?version=dbca295ad02e1680e7ef89451c5a0047'}, {'Emoticon eyeroll.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ef/Emoticon_eyeroll.gif?version=4e28e2b0b82f5727934bd4cd41f05c02'}, {'Emoticon pa kiss.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/89/Emoticon_pa_kiss.gif?version=1f996f11eb9832ca13ee1c419212d01a'}, {'Emoticon fuming.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cf/Emoticon_fuming.gif?version=84af69c80857fc9dcf1e15a44b19aba3'}, {'Emoticon dizzy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4a/Emoticon_dizzy.gif?version=0f7837523ec6628bc2a4a0232e87fe98'}, {'Emoticon blush smile.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/15/Emoticon_blush_smile.gif?version=ab92ae2a48eebec9e887a258c628a48a'}, {'Emoticon arcane rune.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/86/Emoticon_arcane_rune.gif?version=09a6b99a00138290d5c98e426f1c2328'}, {'Emoticon axe laugh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0b/Emoticon_axe_laugh.gif?version=fd399d6e68a26971484cec0adf6abcd5'}, {'Emoticon zipper.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7b/Emoticon_zipper.gif?version=7815d14075961ae67f655feabe3d5a70'}, {'Emoticon nervous.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ad/Emoticon_nervous.gif?version=e81b29a06a47a900f62bb75ee0838747'}, {'Emoticon luna love.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b0/Emoticon_luna_love.gif?version=6f469e68b631cd38c319cdb1604c7b99'}, {'Emoticon giff.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2a/Emoticon_giff.gif?version=42af0264a2396830e7ac242464781601'}, {'Emoticon thumbs down.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cc/Emoticon_thumbs_down.gif?version=a7e8e2780359199ac3acf53ed083bcdd'}, {'Emoticon thumbs up.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2d/Emoticon_thumbs_up.gif?version=6c5eadef0441df741b17fc46f3656592'}, {'Emoticon surprise blush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8c/Emoticon_surprise_blush.gif?version=0db80a0acc8106169c0d5995543f1ba5'}, {'Emoticon dead eyes.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2a/Emoticon_dead_eyes.gif?version=9518f61517e3a3ed3c7eb25716655dc1'}, {'Emoticon money.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e3/Emoticon_money.gif?version=e0537e1504d85aa577e9d7315bff3d3c'}, {'Emoticon unicorn.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c5/Emoticon_unicorn.gif?version=403341b791497e5c4842d268b6281431'}, {'Emoticon naga song.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/93/Emoticon_naga_song.gif?version=596a0bb039a61ca9f1263f3bc0eab850'}, {'Emoticon poop.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9f/Emoticon_poop.gif?version=af34a35c9b506077d3d5afe75147414d'}, {'Emoticon aegis 2016.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d5/Emoticon_aegis_2016.gif?version=3baefdfa6894df877220d06b1ff83628'}, {'Emoticon tear.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3b/Emoticon_tear.gif?version=e90f20e5505b63177563edfc05dbb282'}, {'Emoticon grimace.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/50/Emoticon_grimace.gif?version=f4bc48bdb79f4173b596d1f1c5bd0826'}, {'Emoticon aegis 2017.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3d/Emoticon_aegis_2017.gif?version=f2435cfc0fbf56ac3515d7bb2234ded8'}, {'Emoticon gem.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2c/Emoticon_gem.gif?version=a9a27c310aec522a0ac2422a873a29e0'}, {'Emoticon plant.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c9/Emoticon_plant.gif?version=7cf81b24cfbe6384976a8c6429efdb77'}, {'Emoticon relieved.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6e/Emoticon_relieved.gif?version=463b96628a61a80f9e911ea20dffb757'}, {'Emoticon foggy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c7/Emoticon_foggy.gif?version=fe3cd48341143e6ef99e1f0ce9ab98a5'}, {'Emoticon eh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/29/Emoticon_eh.gif?version=cad58f4626317684a3d58270260ba757'}, {'Emoticon flex.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a1/Emoticon_flex.gif?version=e795395a353ebc9c120442a4af5ae41f'}, {'Emoticon gg.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d8/Emoticon_gg.gif?version=643cde2281041df47361546356c96fb6'}, {'Emoticon donkey.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d2/Emoticon_donkey.gif?version=143daaf91694e5643ce7ff5b2f6ed16f'}, {'Emoticon kiss2.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/20/Emoticon_kiss2.gif?version=aff84050585bcf5570911e1675418520'}, {'Emoticon observer ward.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/67/Emoticon_observer_ward.gif?version=5c0e2c1ffb1acc40b06fc87e039475fe'}, {'Emoticon lick.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/dd/Emoticon_lick.gif?version=60a4708914d3fba35fca986f645331a0'}, {'Emoticon laugh2.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/50/Emoticon_laugh2.gif?version=fa7ece6389a02f2548c096e8ebe21532'}, {'Emoticon sentry ward.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9d/Emoticon_sentry_ward.gif?version=476db62d2c0e9112e9604226a7373d68'}, {'Emoticon whew.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/74/Emoticon_whew.gif?version=92f7319392825612a2e7934ed0ec3a28'}, {'Emoticon gyro.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4d/Emoticon_gyro.gif?version=f6e62d8ec078c0a0736b76966a9ff25a'}, {'Emoticon nerd.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/fd/Emoticon_nerd.gif?version=d7f2469e02099cdac492ff6779dc4c03'}, {'Emoticon confounded.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ae/Emoticon_confounded.gif?version=14aca5e90959204fed8d19d5a59cc06c'}, {'Emoticon joke.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ed/Emoticon_joke.gif?version=dd83ce3b6573a0a234e5053fafd885f8'}, {'Emoticon aaaah.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/ce/Emoticon_aaaah.gif?version=5913f30ca79e2f981f109f152bc14514'}, {'Emoticon burn.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/69/Emoticon_burn.gif?version=d66892d36b8ef401dab88b6076bab14b'}, {'Emoticon hide.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/31/Emoticon_hide.gif?version=097bbf6b334cf7280dedfd82f70f2c01'}, {'Emoticon iceburn.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1f/Emoticon_iceburn.gif?version=a084a28a4b56c848b91012909e492167'}, {'Emoticon tears.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5b/Emoticon_tears.gif?version=bc89f5860e0c8b96654469cf6fb76848'}, {'Emoticon fail.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4a/Emoticon_fail.gif?version=c7ace334c1b229a283d3b5d4fac3ff2d'}, {'Emoticon goodjob.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/ce/Emoticon_goodjob.gif?version=5316b1c98e9a6ce58051e3e508396e58'}, {'Emoticon headshot.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e4/Emoticon_headshot.gif?version=567ef8d731c610ef64a28b8b67001926'}, {'Emoticon heart.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/2c/Emoticon_heart.gif?version=00f747c185e2592466db0c0de65c06f7'}, {'Emoticon horse.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f7/Emoticon_horse.gif?version=7e7a0732a22965645bea56023bd199dd'}, {'Emoticon bristle.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4f/Emoticon_bristle.gif?version=42681fd03387249dc043844982545e88'}, {'Emoticon godz.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/ff/Emoticon_godz.gif?version=80395fbec21a3542889909efca6442ff'}, {'Emoticon lina.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/49/Emoticon_lina.gif?version=f30cb4d615b08b838612fd1f500563cd'}, {'Emoticon merlini.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/54/Emoticon_merlini.gif?version=460a25e30da5fc65d9383cb6d4ca2c65'}, {'Emoticon rosh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/70/Emoticon_rosh.gif?version=4602dd073ec4cf4ec7bb882abbba9a86'}, {'Emoticon dac15 nosewipe.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0e/Emoticon_dac15_nosewipe.gif?version=3dcd8af94fdfefd8df83313088f0721e'}, {'Emoticon dac15 blush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b5/Emoticon_dac15_blush.gif?version=680140f46571ccde6025bd877d8bccb4'}, {'Emoticon dac15 face.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/29/Emoticon_dac15_face.gif?version=9a321d307fce2802f2d8d09cbd58efec'}, {'Emoticon dac15 cool.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d2/Emoticon_dac15_cool.gif?version=55cbf725ab03cb27a5cf58c091c02189'}, {'Emoticon dac15 duel.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8e/Emoticon_dac15_duel.gif?version=fef5ab51a7f1b8aebfe380f8fb56275a'}, {'Emoticon dac15 transform.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/fe/Emoticon_dac15_transform.gif?version=a1cbe0fc36a63db927082662efe6ef15'}, {'Emoticon dac15 stab.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/04/Emoticon_dac15_stab.gif?version=9e7623b2ab502cda69e60411b968bb2d'}, {'Emoticon dac15 frog.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a4/Emoticon_dac15_frog.gif?version=affe11b7c4522d92bb9d81122fb88c9f'}, {'Emoticon dac15 surprise.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Emoticon_dac15_surprise.gif?version=babe84accaf86dae2514755ab7010418'}, {'Emoticon charm blush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cf/Emoticon_charm_blush.gif?version=e1a49c95a7860efdeac37b5fb3edaad2'}, {'Emoticon charm cheeky.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/ca/Emoticon_charm_cheeky.gif?version=4c18d46359a8d2ad21504aaedcfae27e'}, {'Emoticon charm cool.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/ba/Emoticon_charm_cool.gif?version=858e6459966acd1d58ebd8a535260b1c'}, {'Emoticon charm crazy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a5/Emoticon_charm_crazy.gif?version=545121ebc2a83c7972686f09117e8380'}, {'Emoticon charm cry.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/c0/Emoticon_charm_cry.gif?version=dc82d6cbea3aad8a9f472944bcc34b8c'}, {'Emoticon charm disapprove.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/14/Emoticon_charm_disapprove.gif?version=29032c8080506222a39da13f4208de50'}, {'Emoticon charm facepalm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5f/Emoticon_charm_facepalm.gif?version=aa6bc17410cd1b1e03db562b9eeb079d'}, {'Emoticon charm happytears.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8a/Emoticon_charm_happytears.gif?version=c4170e6f62a90ff073477b4a4478b741'}, {'Emoticon charm highfive.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8d/Emoticon_charm_highfive.gif?version=84e12c6b548a0a802cafa662dd21a0e7'}, {'Emoticon charm huh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/62/Emoticon_charm_huh.gif?version=55ab17038e8afa1ca7d8177d2cacf176'}, {'Emoticon charm hush.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/36/Emoticon_charm_hush.gif?version=f847b1a99b9e56c9a22ea7ca0417153e'}, {'Emoticon charm laugh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/08/Emoticon_charm_laugh.gif?version=923b9e4bd07a4ec89786f3a0e0de04a8'}, {'Emoticon charm rage.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a4/Emoticon_charm_rage.gif?version=d9b7ea74e27ee813c6a1c7afb27ed3e9'}, {'Emoticon charm sad.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d4/Emoticon_charm_sad.gif?version=cdfde2a3b9fd33909905a61819750f60'}, {'Emoticon charm sick.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/40/Emoticon_charm_sick.gif?version=2ac7380a93f8c6b21784c2c270e0b7c6'}, {'Emoticon charm sleeping.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/69/Emoticon_charm_sleeping.gif?version=c90cbb6956d963e91385bb90203202d3'}, {'Emoticon charm surprise.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/58/Emoticon_charm_surprise.gif?version=02f01706a88356872d6d14f29bb887a4'}, {'Emoticon charm wink.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/79/Emoticon_charm_wink.gif?version=565e1139963abb624da4f0531402015d'}, {'Emoticon charm smile.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/17/Emoticon_charm_smile.gif?version=d0663ecfe40031df2cfe77b39b0de0e7'}, {'Emoticon charm onlooker.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3d/Emoticon_charm_onlooker.gif?version=704fb2d790bf080651257d8bf5c42ed3'}, {'Emoticon cocky ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b1/Emoticon_cocky_ti6_charm.gif?version=a744cfec88a71e9d95cf44a837ff161d'}, {'Emoticon devil ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0c/Emoticon_devil_ti6_charm.gif?version=f400cb0b7480b6e6cb2a0d5f06945bf4'}, {'Emoticon happy ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5f/Emoticon_happy_ti6_charm.gif?version=5be3a99d4669f5d9bfb265a99f94e526'}, {'Emoticon thinking ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e7/Emoticon_thinking_ti6_charm.gif?version=f91f8291d0a5ab73c476e697a639f92d'}, {'Emoticon tp ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cb/Emoticon_tp_ti6_charm.gif?version=ce4f1857231bdf2466d1964dae91e07c'}, {'Emoticon angel ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7a/Emoticon_angel_ti6_charm.gif?version=421fcb11ac1cafb9727035b563c4e9c1'}, {'Emoticon hex ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/32/Emoticon_hex_ti6_charm.gif?version=f45dd79430534fb5cca37b70b314552e'}, {'Emoticon snot ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/80/Emoticon_snot_ti6_charm.gif?version=2c851dad48a16e68172479de0b036c8e'}, {'Emoticon stunned ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/01/Emoticon_stunned_ti6_charm.gif?version=2a11645b611d2d36b729ac2c740f535f'}, {'Emoticon disappear ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/de/Emoticon_disappear_ti6_charm.gif?version=c2da4edee474ea138e844eaca712a5c5'}, {'Emoticon fire ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/ce/Emoticon_fire_ti6_charm.gif?version=f61e37d141de8b41cf88e751feed11dd'}, {'Emoticon gross ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/7f/Emoticon_gross_ti6_charm.gif?version=d91170369eccd0cded8b73e2e4073cb5'}, {'Emoticon yolo ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/31/Emoticon_yolo_ti6_charm.gif?version=9fb41991bc9cdd968b912a394ef1d75e'}, {'Emoticon throwgame ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/80/Emoticon_throwgame_ti6_charm.gif?version=18bbd4b40df2723da49f00b9d10b7903'}, {'Emoticon eyeroll ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/49/Emoticon_eyeroll_ti6_charm.gif?version=395d968f54711e719b4b895c2a5441e6'}, {'Emoticon lifestealer ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bb/Emoticon_lifestealer_ti6_charm.gif?version=faab6cc264ae855624968fb2e5c6658f'}, {'Emoticon heal ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8f/Emoticon_heal_ti6_charm.gif?version=8b368390675fda82b461046907dd5909'}, {'Emoticon drunk ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/66/Emoticon_drunk_ti6_charm.gif?version=0d0c26c6442323c97c053f31eb994374'}, {'Emoticon salty ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/7/71/Emoticon_salty_ti6_charm.gif?version=37cd68f1df62a4893ef7e871b99d78eb'}, {'Emoticon chicken ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/fa/Emoticon_chicken_ti6_charm.gif?version=b8f7ba65e0149724bb93ae8096df32cf'}, {'Emoticon legion commander t16 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f2/Emoticon_legion_commander_t16_charm.gif?version=07ccea682a688d8653b3de6194f10552'}, {'Emoticon snowman.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0b/Emoticon_snowman.gif?version=ab8f070c7d983a57373d74e4963b7be7'}, {'Emoticon healed.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ad/Emoticon_healed.gif?version=de7435447582ce65dd06a835ce14755d'}, {'Emoticon drunk.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6a/Emoticon_drunk.gif?version=cf4928dc7e7dfa1a1edc4f7f5d23b57a'}, {'Emoticon trophy 2016.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/51/Emoticon_trophy_2016.gif?version=f3580d7a3528ab8c5bdfad799f6b4763'}, {'Emoticon fall 2016 trophy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/36/Emoticon_fall_2016_trophy.gif?version=7f309166d4735493c78a87c1f874448f'}, {'Emoticon jugg.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/aa/Emoticon_jugg.gif?version=ac234cc66f48de791f217a9143fe3b11'}, {'Emoticon no.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9f/Emoticon_no.gif?version=78e159612cd0709c16782ed0a2f692d5'}, {'Emoticon recharge.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/92/Emoticon_recharge.gif?version=c3bfb6e248f7d0f0107ff17d2704e644'}, {'Emoticon dunno.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/69/Emoticon_dunno.gif?version=8e42adc1f872670ca015e43aa099f807'}, {'Emoticon exclamation.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bb/Emoticon_exclamation.gif?version=409342c04beb024af4e4a7d294280925'}, {'Emoticon venom.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/17/Emoticon_venom.gif?version=64245a46b6b97fcc0e655a9ca2c605ff'}, {'Emoticon brood love.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/80/Emoticon_brood_love.gif?version=18eb159291745d7c71ed756c16cb97fb'}, {'Dotakin axe heykid.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a0/Dotakin_axe_heykid.gif?version=a9a0da589b9be184c3afee2105efbe4a'}, {'Dotakin cm huff.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/13/Dotakin_cm_huff.gif?version=ae24451569bc64c8385ff90cdb2fef8e'}, {'Dotakin es beg.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/b5/Dotakin_es_beg.gif?version=8a3875997030075316a5cf8df2875193'}, {'Dotakin kunkka kisskiss.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5e/Dotakin_kunkka_kisskiss.gif?version=6a0dee8bfb69175980cf3b980b3effe1'}, {'Dotakin mk snort.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/94/Dotakin_mk_snort.gif?version=33f9f86d546a0365b707858605c70bc6'}, {'Dotakin naga sweat.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0f/Dotakin_naga_sweat.gif?version=95fca59c516d7e6df5af79d1f3aa87ed'}, {'Dotakin pudge chuckle.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/13/Dotakin_pudge_chuckle.gif?version=d69b871eef9b7ead27fe0d65a8893451'}, {'Dotakin roshan stars.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bb/Dotakin_roshan_stars.gif?version=f89626b5a74f598e13b8d70dc8715b14'}, {'Dotakin slark sleep.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/14/Dotakin_slark_sleep.gif?version=266301e5c935026a4b8225da4af52068'}, {'Dotakin tide bawl.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/3b/Dotakin_tide_bawl.gif?version=a3851bdb4ef343dc8af712f3541b4d39'}, {'Emoticon brow.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8c/Emoticon_brow.gif?version=c734e142f5eaa506674bda8ac4128d21'}, {'Emoticon dealwithit.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bd/Emoticon_dealwithit.gif?version=7ba89329d74fdb19bea42cf64411912d'}, {'Emoticon four.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/07/Emoticon_four.gif?version=17417e1e5ec2e01c0a3f7753f00df0b7'}, {'Emoticon ggzeus.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e4/Emoticon_ggzeus.gif?version=cc93040d8d3a60750d688ce1d549c17a'}, {'Emoticon hahano.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/18/Emoticon_hahano.gif?version=3f38933b58112d079f681dc65f379890'}, {'Emoticon nuh uh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/27/Emoticon_nuh_uh.gif?version=f83215a292c23f8e79f266ba46970f8b'}, {'Emoticon snicker.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/c/cd/Emoticon_snicker.gif?version=07ff1ef1b5a34f54e6732d3f3f2f7019'}, {'Emoticon welluhh.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5c/Emoticon_welluhh.gif?version=c7d5bb3692062127f62edd0206b13aa2'}, {'Emoticon wplina.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ea/Emoticon_wplina.gif?version=e6590ba57bf59ab3a3f2eaede3534dfe'}, {'Emoticon eaglesong 2015.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/90/Emoticon_eaglesong_2015.gif?version=5e1cc78ba1700950f44eb3a6ef0e4d37'}, {'Emoticon reaver 2016.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e2/Emoticon_reaver_2016.gif?version=45cacdaa7406975b6e2d02c21b1fc91b'}, {'Emoticon check.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5f/Emoticon_check.gif?version=46943111e78bbb828ab456abd5556929'}, {'Emoticon eyes.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/3/39/Emoticon_eyes.gif?version=bedc7679eda3f72ab87ad766dedd9ca9'}, {'Emoticon fire bc.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/9d/Emoticon_fire_bc.gif?version=e2f629cb6b428b39501523bdb10d3885'}, {'Emoticon bc flex.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/6/6f/Emoticon_bc_flex.gif?version=44630f1b77b9a960f2b87296493bc5ae'}, {'Emoticon frog.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a4/Emoticon_frog.gif?version=db2a778717d53200d2edeef3f0a27298'}, {'Emoticon hundred.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/90/Emoticon_hundred.gif?version=71b5f48e316ffe6a96bf49c8edc6c752'}, {'Emoticon okay.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1a/Emoticon_okay.gif?version=55d09671e3b6cfa5a3523047a57a40ad'}, {'Techies emoticon.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/4/4a/Techies_emoticon.gif?version=27394c52ab6bc9ad6567b76dd9603bbd'}, {'Emoticon grave.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d6/Emoticon_grave.gif?version=68cb2f46160016116c5f6e54528c70c6'}, {'Emoticon pup.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/0/0c/Emoticon_pup.gif?version=a08479d8912df17a577d126387302218'}, {'Emoticon wrath.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/1/1f/Emoticon_wrath.gif?version=407ae29fe9b9db7082871b0be9db8ac7'}, {'Emoticon underlord ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/e5/Emoticon_underlord_ti6_charm.gif?version=1c92ec364bd2abc2fd2e2502622e5c50'}, {'Emoticon monkey king ti6 charm.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/90/Emoticon_monkey_king_ti6_charm.gif?version=620032a4bd206ee4400f6a2fe67db724'}, {'Emoticon mischief.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/25/Emoticon_mischief.gif?version=761abc0413f6710c2873fbce6116a185'}, {'Emoticon pudge arcana 01.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/83/Emoticon_pudge_arcana_01.gif?version=d7cd6c19f9ff7668bd934c9813c56ab9'}, {'Emoticon pudge arcana 02.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/92/Emoticon_pudge_arcana_02.gif?version=6d04d15e6d54c0d75191036d371299e0'}, {'Emoticon magus cypher.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/8/8a/Emoticon_magus_cypher.gif?version=f5ffae526284bb1f89291447ded35084'}, {'Emoticon darkmoon chicken.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/2/23/Emoticon_darkmoon_chicken.gif?version=7361a3adff356943ca69290ae336b00e'}, {'Emoticon siltbreaker trophy.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/ad/Emoticon_siltbreaker_trophy.gif?version=06154db36bd8238ac00d4be1ace495e5'}, {'Emoticon siltbreaker trophy 2.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/b/ba/Emoticon_siltbreaker_trophy_2.gif?version=af4468869ee56964fad0e2348e90520f'}, {'Emoticon aegis 2018.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f3/Emoticon_aegis_2018.gif?version=e6490ac53faf543ae7c51d53a832a1cd'}, {'Emoticon aegis 2019.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/5f/Emoticon_aegis_2019.gif?version=176be13e0e059152ccbadc3f956ae07b'}, {'Emoticon under win.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a8/Emoticon_under_win.gif?version=5854b384a1554ea4e9705356db5be0eb'}, {'Emoticon under champ.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/d/de/Emoticon_under_champ.gif?version=49c1d86283278a92cae00cd570291e09'}, {'Emoticon under king.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/5/55/Emoticon_under_king.gif?version=1258d315f4a2f41ca5dea12af6fece34'}, {'Emoticon frostivus 2018.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/a/a8/Emoticon_frostivus_2018.gif?version=1163fa58efacb8d379008f5cfb8faf57'}, {'Emoticon morokai woof.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/f/f4/Emoticon_morokai_woof.gif?version=9f6b4aa26f5f688159e80195dee7f6e4'}, {'Emoticon cny rat.gif': 'https://gamepedia.cursecdn.com/dota2_gamepedia/9/99/Emoticon_cny_rat.gif?version=f9709647c27e637883ef771fc725348a'}]

OBSCENT_WORDS = ['arse', 'arsehole',
                 'balls', 'bastard', 'beaver', 'beef curtains', 'bellend', 'bint', 'bitch',
                 'bloodclaat','bloody', 'bollocks', 'bonk', 'bugger', 'bukkake', 'bullshit',
                 'clunge', 'cock', 'cocksucker', 'cow', 'crap', 'cunt', 'chingchong',
                 'damn', 'dick', 'dickhead', 'dildo',
                 'fanny', 'feck', 'flaps', 'fuck',
                 'gash', 'ginger', 'git', 'god', 'goddam',
                 'ho', 'jesus christ', 'jizz', 'knob',
                 'minge', 'minger', 'motherfucker', 'munter', 'nonce',
                 'pissed', 'pissed off', 'prick', 'prickteaser', 'punani', 'pussy',
                 'rapey', 'shag', 'shit', 'skank', 'slag', 'slapper', 'slut', 'snatch', 'sod-off', 'son of a bitch',
                 'tart', 'tits ', 'twat ', 'wanker', 'whore ']

OPEN_DOTA_HEROES = [
    {
        "id": 1,
        "name": "npc_dota_hero_antimage",
        "localized_name": "Anti-Mage",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 2,
        "name": "npc_dota_hero_axe",
        "localized_name": "Axe",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Durable",
            "Disabler",
            "Jungler"
        ],
        "legs": 2
    },
    {
        "id": 3,
        "name": "npc_dota_hero_bane",
        "localized_name": "Bane",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker",
            "Durable"
        ],
        "legs": 4
    },
    {
        "id": 4,
        "name": "npc_dota_hero_bloodseeker",
        "localized_name": "Bloodseeker",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Disabler",
            "Jungler",
            "Nuker",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 5,
        "name": "npc_dota_hero_crystal_maiden",
        "localized_name": "Crystal Maiden",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker",
            "Jungler"
        ],
        "legs": 2
    },
    {
        "id": 6,
        "name": "npc_dota_hero_drow_ranger",
        "localized_name": "Drow Ranger",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Disabler",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 7,
        "name": "npc_dota_hero_earthshaker",
        "localized_name": "Earthshaker",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Initiator",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 8,
        "name": "npc_dota_hero_juggernaut",
        "localized_name": "Juggernaut",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Pusher",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 9,
        "name": "npc_dota_hero_mirana",
        "localized_name": "Mirana",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Support",
            "Escape",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 10,
        "name": "npc_dota_hero_morphling",
        "localized_name": "Morphling",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape",
            "Durable",
            "Nuker",
            "Disabler"
        ],
        "legs": 0
    },
    {
        "id": 11,
        "name": "npc_dota_hero_nevermore",
        "localized_name": "Shadow Fiend",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker"
        ],
        "legs": 0
    },
    {
        "id": 12,
        "name": "npc_dota_hero_phantom_lancer",
        "localized_name": "Phantom Lancer",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Pusher",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 13,
        "name": "npc_dota_hero_puck",
        "localized_name": "Puck",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Initiator",
            "Disabler",
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 14,
        "name": "npc_dota_hero_pudge",
        "localized_name": "Pudge",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Disabler",
            "Initiator",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 15,
        "name": "npc_dota_hero_razor",
        "localized_name": "Razor",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Durable",
            "Nuker",
            "Pusher"
        ],
        "legs": 0
    },
    {
        "id": 16,
        "name": "npc_dota_hero_sand_king",
        "localized_name": "Sand King",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Support",
            "Nuker",
            "Escape",
            "Jungler"
        ],
        "legs": 6
    },
    {
        "id": 17,
        "name": "npc_dota_hero_storm_spirit",
        "localized_name": "Storm Spirit",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape",
            "Nuker",
            "Initiator",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 18,
        "name": "npc_dota_hero_sven",
        "localized_name": "Sven",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Disabler",
            "Initiator",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 19,
        "name": "npc_dota_hero_tiny",
        "localized_name": "Tiny",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Nuker",
            "Pusher",
            "Initiator",
            "Durable",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 20,
        "name": "npc_dota_hero_vengefulspirit",
        "localized_name": "Vengeful Spirit",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Initiator",
            "Disabler",
            "Nuker",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 21,
        "name": "npc_dota_hero_windrunner",
        "localized_name": "Windranger",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Support",
            "Disabler",
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 22,
        "name": "npc_dota_hero_zuus",
        "localized_name": "Zeus",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 23,
        "name": "npc_dota_hero_kunkka",
        "localized_name": "Kunkka",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Support",
            "Disabler",
            "Initiator",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 25,
        "name": "npc_dota_hero_lina",
        "localized_name": "Lina",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Carry",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 26,
        "name": "npc_dota_hero_lion",
        "localized_name": "Lion",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 27,
        "name": "npc_dota_hero_shadow_shaman",
        "localized_name": "Shadow Shaman",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Pusher",
            "Disabler",
            "Nuker",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 28,
        "name": "npc_dota_hero_slardar",
        "localized_name": "Slardar",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Durable",
            "Initiator",
            "Disabler",
            "Escape"
        ],
        "legs": 0
    },
    {
        "id": 29,
        "name": "npc_dota_hero_tidehunter",
        "localized_name": "Tidehunter",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Durable",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 30,
        "name": "npc_dota_hero_witch_doctor",
        "localized_name": "Witch Doctor",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 31,
        "name": "npc_dota_hero_lich",
        "localized_name": "Lich",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 32,
        "name": "npc_dota_hero_riki",
        "localized_name": "Riki",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 33,
        "name": "npc_dota_hero_enigma",
        "localized_name": "Enigma",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Disabler",
            "Jungler",
            "Initiator",
            "Pusher"
        ],
        "legs": 0
    },
    {
        "id": 34,
        "name": "npc_dota_hero_tinker",
        "localized_name": "Tinker",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 35,
        "name": "npc_dota_hero_sniper",
        "localized_name": "Sniper",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 36,
        "name": "npc_dota_hero_necrolyte",
        "localized_name": "Necrophos",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Durable",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 37,
        "name": "npc_dota_hero_warlock",
        "localized_name": "Warlock",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Initiator",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 38,
        "name": "npc_dota_hero_beastmaster",
        "localized_name": "Beastmaster",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 39,
        "name": "npc_dota_hero_queenofpain",
        "localized_name": "Queen of Pain",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 40,
        "name": "npc_dota_hero_venomancer",
        "localized_name": "Venomancer",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Initiator",
            "Pusher",
            "Disabler"
        ],
        "legs": 0
    },
    {
        "id": 41,
        "name": "npc_dota_hero_faceless_void",
        "localized_name": "Faceless Void",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Initiator",
            "Disabler",
            "Escape",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 42,
        "name": "npc_dota_hero_skeleton_king",
        "localized_name": "Wraith King",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Support",
            "Durable",
            "Disabler",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 43,
        "name": "npc_dota_hero_death_prophet",
        "localized_name": "Death Prophet",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Pusher",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 44,
        "name": "npc_dota_hero_phantom_assassin",
        "localized_name": "Phantom Assassin",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 45,
        "name": "npc_dota_hero_pugna",
        "localized_name": "Pugna",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Nuker",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 46,
        "name": "npc_dota_hero_templar_assassin",
        "localized_name": "Templar Assassin",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 47,
        "name": "npc_dota_hero_viper",
        "localized_name": "Viper",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Durable",
            "Initiator",
            "Disabler"
        ],
        "legs": 0
    },
    {
        "id": 48,
        "name": "npc_dota_hero_luna",
        "localized_name": "Luna",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 49,
        "name": "npc_dota_hero_dragon_knight",
        "localized_name": "Dragon Knight",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Pusher",
            "Durable",
            "Disabler",
            "Initiator",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 50,
        "name": "npc_dota_hero_dazzle",
        "localized_name": "Dazzle",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 51,
        "name": "npc_dota_hero_rattletrap",
        "localized_name": "Clockwerk",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 52,
        "name": "npc_dota_hero_leshrac",
        "localized_name": "Leshrac",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Support",
            "Nuker",
            "Pusher",
            "Disabler"
        ],
        "legs": 4
    },
    {
        "id": 53,
        "name": "npc_dota_hero_furion",
        "localized_name": "Nature's Prophet",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Jungler",
            "Pusher",
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 54,
        "name": "npc_dota_hero_life_stealer",
        "localized_name": "Lifestealer",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Durable",
            "Jungler",
            "Escape",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 55,
        "name": "npc_dota_hero_dark_seer",
        "localized_name": "Dark Seer",
        "primary_attr": "int",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Jungler",
            "Escape",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 56,
        "name": "npc_dota_hero_clinkz",
        "localized_name": "Clinkz",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 57,
        "name": "npc_dota_hero_omniknight",
        "localized_name": "Omniknight",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 58,
        "name": "npc_dota_hero_enchantress",
        "localized_name": "Enchantress",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Jungler",
            "Pusher",
            "Durable",
            "Disabler"
        ],
        "legs": 4
    },
    {
        "id": 59,
        "name": "npc_dota_hero_huskar",
        "localized_name": "Huskar",
        "primary_attr": "str",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Durable",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 60,
        "name": "npc_dota_hero_night_stalker",
        "localized_name": "Night Stalker",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Initiator",
            "Durable",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 61,
        "name": "npc_dota_hero_broodmother",
        "localized_name": "Broodmother",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Pusher",
            "Escape",
            "Nuker"
        ],
        "legs": 8
    },
    {
        "id": 62,
        "name": "npc_dota_hero_bounty_hunter",
        "localized_name": "Bounty Hunter",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 63,
        "name": "npc_dota_hero_weaver",
        "localized_name": "Weaver",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape"
        ],
        "legs": 4
    },
    {
        "id": 64,
        "name": "npc_dota_hero_jakiro",
        "localized_name": "Jakiro",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Pusher",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 65,
        "name": "npc_dota_hero_batrider",
        "localized_name": "Batrider",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Initiator",
            "Jungler",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 66,
        "name": "npc_dota_hero_chen",
        "localized_name": "Chen",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Jungler",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 67,
        "name": "npc_dota_hero_spectre",
        "localized_name": "Spectre",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Durable",
            "Escape"
        ],
        "legs": 0
    },
    {
        "id": 68,
        "name": "npc_dota_hero_ancient_apparition",
        "localized_name": "Ancient Apparition",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 69,
        "name": "npc_dota_hero_doom_bringer",
        "localized_name": "Doom",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Disabler",
            "Initiator",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 70,
        "name": "npc_dota_hero_ursa",
        "localized_name": "Ursa",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Jungler",
            "Durable",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 71,
        "name": "npc_dota_hero_spirit_breaker",
        "localized_name": "Spirit Breaker",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Initiator",
            "Disabler",
            "Durable",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 72,
        "name": "npc_dota_hero_gyrocopter",
        "localized_name": "Gyrocopter",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 73,
        "name": "npc_dota_hero_alchemist",
        "localized_name": "Alchemist",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Support",
            "Durable",
            "Disabler",
            "Initiator",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 74,
        "name": "npc_dota_hero_invoker",
        "localized_name": "Invoker",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Disabler",
            "Escape",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 75,
        "name": "npc_dota_hero_silencer",
        "localized_name": "Silencer",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Support",
            "Disabler",
            "Initiator",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 76,
        "name": "npc_dota_hero_obsidian_destroyer",
        "localized_name": "Outworld Devourer",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Nuker",
            "Disabler"
        ],
        "legs": 4
    },
    {
        "id": 77,
        "name": "npc_dota_hero_lycan",
        "localized_name": "Lycan",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Pusher",
            "Jungler",
            "Durable",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 78,
        "name": "npc_dota_hero_brewmaster",
        "localized_name": "Brewmaster",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Initiator",
            "Durable",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 79,
        "name": "npc_dota_hero_shadow_demon",
        "localized_name": "Shadow Demon",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Initiator",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 80,
        "name": "npc_dota_hero_lone_druid",
        "localized_name": "Lone Druid",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Pusher",
            "Jungler",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 81,
        "name": "npc_dota_hero_chaos_knight",
        "localized_name": "Chaos Knight",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Disabler",
            "Durable",
            "Pusher",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 82,
        "name": "npc_dota_hero_meepo",
        "localized_name": "Meepo",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Nuker",
            "Disabler",
            "Initiator",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 83,
        "name": "npc_dota_hero_treant",
        "localized_name": "Treant Protector",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Initiator",
            "Durable",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 84,
        "name": "npc_dota_hero_ogre_magi",
        "localized_name": "Ogre Magi",
        "primary_attr": "int",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Durable",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 85,
        "name": "npc_dota_hero_undying",
        "localized_name": "Undying",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Durable",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 86,
        "name": "npc_dota_hero_rubick",
        "localized_name": "Rubick",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 87,
        "name": "npc_dota_hero_disruptor",
        "localized_name": "Disruptor",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 88,
        "name": "npc_dota_hero_nyx_assassin",
        "localized_name": "Nyx Assassin",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Disabler",
            "Nuker",
            "Initiator",
            "Escape"
        ],
        "legs": 6
    },
    {
        "id": 89,
        "name": "npc_dota_hero_naga_siren",
        "localized_name": "Naga Siren",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Support",
            "Pusher",
            "Disabler",
            "Initiator",
            "Escape"
        ],
        "legs": 0
    },
    {
        "id": 90,
        "name": "npc_dota_hero_keeper_of_the_light",
        "localized_name": "Keeper of the Light",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Jungler"
        ],
        "legs": 2
    },
    {
        "id": 91,
        "name": "npc_dota_hero_wisp",
        "localized_name": "Io",
        "primary_attr": "str",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Escape",
            "Nuker"
        ],
        "legs": 0
    },
    {
        "id": 92,
        "name": "npc_dota_hero_visage",
        "localized_name": "Visage",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Durable",
            "Disabler",
            "Pusher"
        ],
        "legs": 2
    },
    {
        "id": 93,
        "name": "npc_dota_hero_slark",
        "localized_name": "Slark",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 94,
        "name": "npc_dota_hero_medusa",
        "localized_name": "Medusa",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Disabler",
            "Durable"
        ],
        "legs": 0
    },
    {
        "id": 95,
        "name": "npc_dota_hero_troll_warlord",
        "localized_name": "Troll Warlord",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Pusher",
            "Disabler",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 96,
        "name": "npc_dota_hero_centaur",
        "localized_name": "Centaur Warrunner",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Durable",
            "Initiator",
            "Disabler",
            "Nuker",
            "Escape"
        ],
        "legs": 4
    },
    {
        "id": 97,
        "name": "npc_dota_hero_magnataur",
        "localized_name": "Magnus",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Nuker",
            "Escape"
        ],
        "legs": 4
    },
    {
        "id": 98,
        "name": "npc_dota_hero_shredder",
        "localized_name": "Timbersaw",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Nuker",
            "Durable",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 99,
        "name": "npc_dota_hero_bristleback",
        "localized_name": "Bristleback",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Durable",
            "Initiator",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 100,
        "name": "npc_dota_hero_tusk",
        "localized_name": "Tusk",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 101,
        "name": "npc_dota_hero_skywrath_mage",
        "localized_name": "Skywrath Mage",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 102,
        "name": "npc_dota_hero_abaddon",
        "localized_name": "Abaddon",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Carry",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 103,
        "name": "npc_dota_hero_elder_titan",
        "localized_name": "Elder Titan",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Initiator",
            "Disabler",
            "Nuker",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 104,
        "name": "npc_dota_hero_legion_commander",
        "localized_name": "Legion Commander",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Disabler",
            "Initiator",
            "Durable",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 105,
        "name": "npc_dota_hero_techies",
        "localized_name": "Techies",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Nuker",
            "Disabler"
        ],
        "legs": 6
    },
    {
        "id": 106,
        "name": "npc_dota_hero_ember_spirit",
        "localized_name": "Ember Spirit",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Nuker",
            "Disabler",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 107,
        "name": "npc_dota_hero_earth_spirit",
        "localized_name": "Earth Spirit",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Nuker",
            "Escape",
            "Disabler",
            "Initiator",
            "Durable"
        ],
        "legs": 2
    },
    {
        "id": 108,
        "name": "npc_dota_hero_abyssal_underlord",
        "localized_name": "Underlord",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Durable",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 109,
        "name": "npc_dota_hero_terrorblade",
        "localized_name": "Terrorblade",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Pusher",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 110,
        "name": "npc_dota_hero_phoenix",
        "localized_name": "Phoenix",
        "primary_attr": "str",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Initiator",
            "Escape",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 111,
        "name": "npc_dota_hero_oracle",
        "localized_name": "Oracle",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 112,
        "name": "npc_dota_hero_winter_wyvern",
        "localized_name": "Winter Wyvern",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Disabler",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 113,
        "name": "npc_dota_hero_arc_warden",
        "localized_name": "Arc Warden",
        "primary_attr": "agi",
        "attack_type": "Ranged",
        "roles": [
            "Carry",
            "Escape",
            "Nuker"
        ],
        "legs": 2
    },
    {
        "id": 114,
        "name": "npc_dota_hero_monkey_king",
        "localized_name": "Monkey King",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Disabler",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 119,
        "name": "npc_dota_hero_dark_willow",
        "localized_name": "Dark Willow",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 120,
        "name": "npc_dota_hero_pangolier",
        "localized_name": "Pangolier",
        "primary_attr": "agi",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Nuker",
            "Disabler",
            "Durable",
            "Escape",
            "Initiator"
        ],
        "legs": 2
    },
    {
        "id": 121,
        "name": "npc_dota_hero_grimstroke",
        "localized_name": "Grimstroke",
        "primary_attr": "int",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 126,
        "name": "npc_dota_hero_void_spirit",
        "localized_name": "Void Spirit",
        "primary_attr": "int",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Escape",
            "Nuker",
            "Disabler"
        ],
        "legs": 2
    },
    {
        "id": 128,
        "name": "npc_dota_hero_snapfire",
        "localized_name": "Snapfire",
        "primary_attr": "str",
        "attack_type": "Ranged",
        "roles": [
            "Support",
            "Nuker",
            "Disabler",
            "Escape"
        ],
        "legs": 2
    },
    {
        "id": 129,
        "name": "npc_dota_hero_mars",
        "localized_name": "Mars",
        "primary_attr": "str",
        "attack_type": "Melee",
        "roles": [
            "Carry",
            "Initiator",
            "Disabler",
            "Durable"
        ],
        "legs": 2
    }
]