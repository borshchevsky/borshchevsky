from market.celery import celery_app


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3.0, test.s())


@celery_app.task
def test():
    print('test')
