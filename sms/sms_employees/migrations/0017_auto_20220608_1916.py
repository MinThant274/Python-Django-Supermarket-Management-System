# Generated by Django 2.0 on 2022-06-08 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms_employees', '0016_auto_20220608_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 6, 8, 12, 46, 52, 44518, tzinfo=utc), verbose_name='Birthday'),
        ),
    ]
