# Generated by Django 2.1.14 on 2020-02-04 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0112_syncjob_synchronizer_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.OpportunityStage'),
        ),
    ]
