# Generated by Django 2.1.1 on 2018-10-29 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotkiller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotkiller',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='robotkiller',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 12, 23, 30, 319607)),
        ),
    ]