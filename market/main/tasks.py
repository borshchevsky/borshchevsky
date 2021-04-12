from market.celery import app


@app.task(bind=True)
def test():
    print('test')
