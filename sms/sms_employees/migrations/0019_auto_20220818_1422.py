# Generated by Django 2.2 on 2022-08-18 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_employees', '0018_auto_20220818_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 7, 52, 58, 399193, tzinfo=utc), verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name='Zip Code'),
        ),
    ]
