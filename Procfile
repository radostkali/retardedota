web: gunicorn run:app
worker: celery worker -A dota_api.modules.celery_tasks worker -P solo --loglevel=INFO