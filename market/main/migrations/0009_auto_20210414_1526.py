# Generated by Django 3.1.7 on 2021-04-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_smslog_server_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslog',
            name='code',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
