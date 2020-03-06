from pymongo import MongoClient, DESCENDING
from config import MONGO_URI
from datetime import datetime, timedelta


def mongo_auth():
    # 'mongodb://dotaapp:dotaapp1dotaapp@ds125525.mlab.com:25525/heroku_xjf41300'
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


def meta_heroes():
    mongo_inst = mongo_auth()
    collection = mongo_inst.meta_heroes
    heroes = [i['hero_name'] for i in collection.find({})]
    return heroes


def check_user(dota_id):
    mongo_inst = mongo_auth()
    collection = mongo_inst.achievements
    try:
        user = collection.find_one({'dota_id': dota_id})
    except OverflowError:
        return True
    if not user:
        collection.insert({'dota_id': dota_id, 'status': 'pending'})
        return False
    else:
        if user['status'] == 'pending':
            return True
        last_check = datetime.utcnow() - user['timestamp']
        if last_check > timedelta(days=1) or \
                (user['status'] == 'no_games' and last_check > timedelta(minutes=1)):
            collection.update_one({'dota_id': dota_id}, {'$set': {'status': 'pending'}})
            return False
        else:
            return True


def post_user(dota_id, achievements, personaname, avatar, friends):
    mongo_inst = mongo_auth()
    collection = mongo_inst.achievements
    user = collection.find_one({'dota_id': dota_id})
    status = 'complete' if achievements else 'no_games'
    achieves = {i: achievements[i] for i in achievements if achievements[i]['status'] != 0} if achievements else None
    if not user:
        collection.insert({
            'dota_id': dota_id,
            'personaname': personaname,
            'avatar': avatar,
            'friends': friends,
            'timestamp': datetime.utcnow(),
            'status': status,
            'achievements': achieves
        })
    else:
        collection.update_one(
            {'dota_id': dota_id},
            {
                '$set': {
                    'timestamp': datetime.utcnow(),
                    'personaname': personaname,
                    'avatar': avatar,
                    'friends': friends,
                    'status': status,
                    'achievements': achieves
                }
            }
        )
    return True


def open_dota_limit():
    request_number = 8
    mongo_inst = mongo_auth()
    collection = mongo_inst.open_dota_limit
    reqs = collection.find().sort('timestamp', DESCENDING)
    count = 0
    now = datetime.utcnow()
    time = None
    for req in reqs:
        time = req['timestamp']
        if now - time <= timedelta(minutes=1):
            count += req['count']
        else:
            break
    if 60 - count < request_number:
        return False
    else:
        collection.insert({
            'timestamp': now,
            'count': request_number
        })
        if time:
            collection.remove({
                'timestamp': {'$lt': time}
            })
        return True


if __name__ == '__main__':
    r = mongo_auth()
