# Generated by Django 2.0 on 2022-06-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='expected_employees',
            field=models.IntegerField(default=0, verbose_name='Expected Employees'),
        ),
    ]
