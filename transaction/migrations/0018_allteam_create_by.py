# Generated by Django 2.0.7 on 2021-06-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0017_auto_20210607_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='allteam',
            name='create_by',
            field=models.CharField(default='', max_length=50, verbose_name='ชื่อทีม'),
        ),
    ]
