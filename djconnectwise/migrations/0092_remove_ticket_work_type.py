# Generated by Django 2.1 on 2019-07-15 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0091_workrole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='work_type',
        ),
    ]
