from celery.schedules import crontab
from django.core.mail import send_mail

from main.models import Subscriber, Product
from main.utils import send_novelty_weekly
from market.celery import celery_app


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=1, day_of_week='sat'), send_novelty_weekly.s())


@celery_app.task
def send_novelty_task(product_id):
    product = Product.objects.get(id=product_id)

    message = f'''
        <h3>A new good arrived.</h3>
        You received this message because you have subscribed for information about new goods.
        <br>
        We just got a new {product.title} supply! You can see the detail information about this one here:
        <br>
        <a href="http://127.0.0.1:8000/goods/{product.id}>{product.title}</a>
        '''

    mail_list = {sub.user.email for sub in Subscriber.objects.all() if sub.user.email}
    send_mail(
        subject='A new good has just arrived.',
        message='Hello.',
        from_email='admin@example.com',
        recipient_list=mail_list,
        fail_silently=False,
        html_message=message
    )
