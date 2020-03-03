import os

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")

REDIS_URL = os.environ.get("REDIS_URL")
MONGO_URI = os.environ.get("MONGO_URI")
DOTA_API = os.environ.get("DOTA_API")
