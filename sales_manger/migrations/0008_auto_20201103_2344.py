# Generated by Django 3.1.2 on 2020-11-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manger', '0007_auto_20201103_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesesmanger',
            name='salesCode',
            field=models.IntegerField(unique=True),
        ),
    ]