from raven import Client

from app.core.queue_app import queue
from rq.decorators import job
from app.core.config import settings

client_sentry = Client(settings.SENTRY_DSN)


@job(queue)
def test_rq(word: str) -> str:
    return f"test task return {word}"
