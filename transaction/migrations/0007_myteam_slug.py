# Generated by Django 2.0.7 on 2021-06-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_auto_20210611_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='myteam',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
