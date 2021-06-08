# Generated by Django 2.0.7 on 2021-06-06 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0013_auto_20210525_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='allteams',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50, verbose_name='ชื่อทีม')),
                ('date_build', models.DateField(default=datetime.date.today, verbose_name='วันที่สร้างทีม')),
            ],
        ),
        migrations.CreateModel(
            name='myteams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('date_join', models.DateField(default=datetime.date.today, verbose_name='วันที่เข้าร่วมทีม')),
                ('permissions', models.CharField(default='', max_length=50, verbose_name='สิทธิ์')),
            ],
        ),
    ]