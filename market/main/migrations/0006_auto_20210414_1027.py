# Generated by Django 3.1.7 on 2021-04-14 07:27

import datetime
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210413_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 4, 14)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 4, 14), validators=[main.validators.validate_age]),
        ),
    ]