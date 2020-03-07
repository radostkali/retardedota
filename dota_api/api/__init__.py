from flask import Blueprint, jsonify, render_template, request, current_app, send_from_directory
from dota_api.modules.celery_tasks import task_to_analyze
from dota_api.modules.steam_id_getter import GetSteamId
from dota_api.modules.achieve_serializer import serialize
from dota_api import mongo
from datetime import datetime, timedelta
import os


api = Blueprint('main', __name__)

API_ROOT = 'https://api.opendota.com/api'
MY_DOTA_ID = '120150156'

pending_user = {
    'status': 'pending',
    'personaname': None,
    'avatar': None,
}


def user_info(mongo_user, status):
    user = {
        'status': status,
        'personaname': mongo_user['personaname'],
        'avatar': mongo_user['avatar'],
        'friends': mongo_user['friends'] if len(mongo_user['friends']) else None,
    }
    last_check = datetime.utcnow() - mongo_user['timestamp']
    user['update'] = True if last_check > timedelta(days=1) and status == 'complete' else False
    if mongo_user['achievements']:
        user['data'] = serialize(mongo_user['achievements'])
        user['rate'] = max([mongo_user['achievements'][i]['priority'] for i in mongo_user['achievements']])
    if 'patreon' in mongo_user:
        user['patreon'] = mongo_user['patreon']
    return user


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@api.route('/service-worker.js', methods=['GET'])
def service_worker():
    dist = os.path.join(os.path.dirname(current_app.root_path), 'dist')
    return send_from_directory(dist, 'service-worker.js')


@api.route('/manifest.json', methods=['GET'])
def manifest():
    dist = os.path.join(os.path.dirname(current_app.root_path), 'dist')
    return send_from_directory(dist, 'manifest.json')


@api.route('/img/<path:filename>', methods=['GET'])
def img(filename):
    dist = os.path.join(os.path.dirname(current_app.root_path), 'dist', 'img')
    return send_from_directory(dist, filename)


@api.route('/api/check_user', methods=['POST'])
def check_user():
    input_str = request.json['input']
    dota_id = GetSteamId().define_id(input_str)
    if not dota_id:
        return jsonify({'status': 'error', 'message': 'Wrong ID or URL.'})
    task_to_analyze.apply_async(args=[dota_id])
    return jsonify({'status': 'success', 'dota_id': dota_id})


@api.route('/api/check_status/<dota_id>', methods=['GET'])
def check_status(dota_id):
    collection = mongo.db.achievements
    try:
        dota_id = int(dota_id)
    except ValueError:
        return jsonify({'status': 'not_found'})
    user = collection.find_one({'dota_id': dota_id})
    if not user:
        dota_id = GetSteamId().define_id(dota_id)
        if not dota_id:
            return jsonify({'status': 'not_found'})
        else:
            task_to_analyze.apply_async(args=[dota_id])
            return jsonify(pending_user)
    if user['status'] == 'pending':
        if 'achievements' in user:
            task_to_analyze.apply_async(args=[dota_id])
            return jsonify(user_info(user, 'pending'))
        else:
            return jsonify(pending_user)
    elif user['status'] == 'complete':
        return jsonify(user_info(user, 'complete'))
    elif user['status'] == 'no_games':
        return jsonify(user_info(user, 'no_games'))


@api.route('/api/update', methods=['POST'])
def update():
    input_str = request.json['dota_id']
    dota_id = GetSteamId().define_id(input_str)
    if not dota_id:
        return jsonify({'status': 'error', 'message': 'Wrong ID.'})
    collection = mongo.db.achievements
    user = collection.find_one({'dota_id': dota_id})
    last_check = datetime.utcnow() - user['timestamp']
    if last_check > timedelta(days=1):
        task_to_analyze.apply_async(args=[dota_id])
        return jsonify({'status': 'success', 'dota_id': dota_id})
    else:
        return jsonify({'status': 'error', 'message': 'Can\'t update now.'})
