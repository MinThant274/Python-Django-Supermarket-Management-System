# Generated by Django 2.2 on 2022-08-18 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_employees', '0017_auto_20220608_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 7, 35, 32, 804028, tzinfo=utc), verbose_name='Birthday'),
        ),
    ]
