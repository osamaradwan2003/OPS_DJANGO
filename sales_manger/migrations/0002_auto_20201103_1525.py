# Generated by Django 3.1.2 on 2020-11-03 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesesmanger',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 15, 25, 52, 438330)),
        ),
        migrations.AlterField(
            model_name='salesesmanger',
            name='salesCode',
            field=models.SmallIntegerField(unique=True),
        ),
    ]