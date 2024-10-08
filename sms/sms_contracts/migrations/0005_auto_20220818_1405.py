# Generated by Django 2.2 on 2022-08-18 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_contracts', '0004_auto_20220609_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 7, 35, 32, 804028, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contractmodel',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 7, 35, 32, 804028, tzinfo=utc), verbose_name='Start Date'),
        ),
    ]
