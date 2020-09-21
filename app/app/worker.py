from raven import Client
from rq import Worker

from app.core.celery_app import queue, redis_conn
from rq.decorators import job
from app.core.config import settings

client_sentry = Client(settings.SENTRY_DSN)


@job(queue)
def test_rq(word: str) -> str:
    return f"test task return {word}"


worker = Worker([queue], connection=redis_conn)
