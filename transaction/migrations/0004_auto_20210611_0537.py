# Generated by Django 2.0.7 on 2021-06-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_allteam_create_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allteam',
            name='create_by',
            field=models.IntegerField(),
        ),
    ]
