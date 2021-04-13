from datetime import timedelta

from django.core.mail import send_mail
from django.utils import timezone

from market.celery import celery_app
from main.models import Product, Subscriber


@celery_app.task
def send_novelty_weekly():
    now = timezone.now().date()
    week_ago = now - timedelta(7)
    novelty_count = len(Product.objects.filter(date_created__range=[week_ago, now]))

    message = f'''
        <h3>We have some novelties.</h3>
        You received this message because you have subscribed for information about new goods.
        <br>
        We got {novelty_count} novelties last week! Take a look!
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
