# Generated by Django 3.1.5 on 2021-03-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0147_auto_20210223_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcommunication',
            name='value',
            field=models.CharField(default='', max_length=250),
        ),
    ]
