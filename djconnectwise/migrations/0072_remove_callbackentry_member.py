# Generated by Django 2.0 on 2018-08-23 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0071_auto_20180822_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callbackentry',
            name='member',
        ),
    ]
