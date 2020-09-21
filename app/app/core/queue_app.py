from redis import Redis
from rq import Queue
from app.core.config import settings

redis_conn = Redis.from_url(settings.REDIS_URI)

queue = Queue(connection=redis_conn)
