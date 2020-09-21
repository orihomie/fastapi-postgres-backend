# from celery import Celery
# celery_app = Celery("worker", broker="amqp://guest@0.0.0.0:4369//")
# celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}

from redis import Redis
from rq import Queue
from app.core.config import settings

print('REDIS URI:' + settings.REDIS_URI)

redis_conn = Redis.from_url(settings.REDIS_URI)
queue = Queue(connection=redis_conn)
