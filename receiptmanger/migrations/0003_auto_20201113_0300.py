# Generated by Django 3.1.2 on 2020-11-13 01:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receiptmanger', '0002_auto_20201113_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciptsmanger',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 11, 13, 1, 0, 30, 737089, tzinfo=utc)),
        ),
    ]
