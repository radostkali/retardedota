from celery import Celery
from config import REDIS_URL
from dota_api.modules.open_dota_api import OpenDotaApi
from dota_api.modules.db_data import meta_heroes, check_user, post_user
from dota_api.modules.calculator import AchivesCalculator


BROKER_URL = REDIS_URL
app = Celery('dota_api', broker=BROKER_URL)


@app.task
def task_to_analyze(dota_id):
    check = check_user(dota_id)
    if check:
        return {'status': 'success'}
    data = OpenDotaApi(dota_id).run()
    if data is None:
        return {'status': 'error'}
    data['meta_heroes'] = meta_heroes()
    result = AchivesCalculator(data).run()
    post = post_user(dota_id, result, data['personaname'], data['avatar'], data['friends'])
    if post:
        return {'status': 'success'}
    else:
        return {'status': 'error'}

  # celery -A dota_api.modules.celery_tasks worker --loglevel=info -P solo