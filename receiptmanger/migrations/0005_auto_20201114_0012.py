# Generated by Django 3.1.2 on 2020-11-13 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receiptmanger', '0004_auto_20201114_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciptsmanger',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 22, 12, 52, 444623, tzinfo=utc)),
        ),
    ]
