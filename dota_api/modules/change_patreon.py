import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGODB_URI")


def mongo_auth():
    splited = MONGO_URI.split('//')[-1]
    host = splited.split('@')[-1].split(':')[0]
    if host == 'localhost':
        db = MongoClient(MONGO_URI)
        return db.db
    port = int(splited.split('@')[-1].split(':')[-1].split('/')[0])
    base = splited.split('@')[-1].split('/')[-1]
    user = splited.split('@')[0].split(':')[0]
    passw = splited.split('@')[0].split(':')[1]
    connection = MongoClient(host, port, retryWrites=False)
    db = connection[base]
    db.authenticate(user, passw)
    return db


def change(dota_id, patreon):
    db = mongo_auth()
    collection = db.achievements
    if collection.find_one({'dota_id': dota_id}):
        collection.update_one({'dota_id': dota_id}, {
            '$set': {
                'patreon': patreon
            }
        })
        print('Success')
    else:
        print('No user')


if __name__ == '__main__':
    dota_id = int(input('Dota ID: '))
    print('Choose patreon status:')
    print('0. No status')
    print('1. Support')
    print('2. Premium')
    patreon = int(input())
    gg = False
    if patreon == 0:
        patreon = None
    elif patreon == 1:
        patreon = 'supporter'
    elif patreon == 2:
        patreon = 'premium'
    else:
        gg = True
    if not gg:
        change(dota_id, patreon)
