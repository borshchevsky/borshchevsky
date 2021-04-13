# Generated by Django 3.1.7 on 2021-04-13 07:26

import datetime
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 4, 13)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 4, 13), validators=[main.validators.validate_age]),
        ),
    ]