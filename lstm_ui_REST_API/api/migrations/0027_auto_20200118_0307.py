# Generated by Django 3.0.1 on 2020-01-18 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_runningcase_event_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningcase',
            name='event_log',
        ),
        migrations.RemoveField(
            model_name='runningcase',
            name='event_log_name',
        ),
    ]
