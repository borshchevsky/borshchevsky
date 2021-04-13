from celery.schedules import crontab

from main.utils import send_novelty_weekly
from market.celery import celery_app


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=1, day_of_week='sat'), send_novelty_weekly.s())
