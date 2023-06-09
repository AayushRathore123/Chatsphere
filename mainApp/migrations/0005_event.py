# Generated by Django 4.0.1 on 2023-04-23 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='EVENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_id', models.IntegerField()),
                ('name', models.CharField(default='None', max_length=64)),
                ('purpose', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('time', models.TimeField(default=datetime.datetime(2023, 4, 23, 21, 30, 55, 790249), verbose_name='time')),
                ('place', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
