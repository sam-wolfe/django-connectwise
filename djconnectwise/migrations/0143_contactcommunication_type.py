# Generated by Django 3.1.5 on 2021-01-11 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0142_communicationtype_communicationtypetracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactcommunication',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.communicationtype'),
        ),
    ]
