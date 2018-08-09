# Generated by Django 2.0 on 2018-08-09 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0064_auto_20180808_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('monday_start_time', models.TimeField(blank=True, null=True)),
                ('monday_end_time', models.TimeField(blank=True, null=True)),
                ('tuesday_start_time', models.TimeField(blank=True, null=True)),
                ('tuesday_end_time', models.TimeField(blank=True, null=True)),
                ('wednesday_start_time', models.TimeField(blank=True, null=True)),
                ('wednesday_end_time', models.TimeField(blank=True, null=True)),
                ('thursday_start_time', models.TimeField(blank=True, null=True)),
                ('thursday_end_time', models.TimeField(blank=True, null=True)),
                ('friday_start_time', models.TimeField(blank=True, null=True)),
                ('friday_end_time', models.TimeField(blank=True, null=True)),
                ('saturday_start_time', models.TimeField(blank=True, null=True)),
                ('saturday_end_time', models.TimeField(blank=True, null=True)),
                ('sunday_start_time', models.TimeField(blank=True, null=True)),
                ('sunday_end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sla',
            name='based_on',
            field=models.CharField(choices=[('MyCalendar', 'My Company Calendar'), ('Customer', "Customer's Calendar"), ('AllHours', '24 Hours'), ('Custom', 'Custom Calendar')], db_index=True, default='MyCalendar', max_length=50),
        ),
        migrations.AddField(
            model_name='sla',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.Calendar'),
        ),
    ]
