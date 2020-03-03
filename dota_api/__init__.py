from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_redis import FlaskRedis

from werkzeug.serving import is_running_from_reloader
from apscheduler.schedulers.background import BackgroundScheduler
from bson.objectid import ObjectId
import atexit
import datetime
import json

from dota_api.modules.general_info_parsing import get_info


TIMEOUT = 86400  # One in a day


cors = CORS(resources={r'/*': {'origins': '*'}})
mongo = PyMongo()
redis = FlaskRedis()


class JSONEncoder(json.JSONEncoder):
    #  Extend json-encoder class

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        return json.JSONEncoder.default(self, o)


def create_app():
    #  Create an application.
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="../dist",
        static_folder="../dist/static"
    )
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)

    from .api import api
    app.register_blueprint(api)

    app.json_encoder = JSONEncoder

    cors.init_app(app)
    mongo.init_app(app)
    redis.init_app(app)

    #  Background parsing
    if not is_running_from_reloader():
        get_info()
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=get_info, trigger="interval", seconds=TIMEOUT)
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown())

    return app
