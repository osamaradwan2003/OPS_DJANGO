# Generated by Django 3.1.2 on 2020-11-15 22:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payedProducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payedproducts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 22, 6, 25, 502615, tzinfo=utc)),
        ),
    ]
