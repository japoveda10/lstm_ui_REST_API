# Generated by Django 3.0.1 on 2020-01-17 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200116_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningcase',
            name='event_log',
        ),
    ]
