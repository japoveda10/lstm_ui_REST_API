# Generated by Django 3.0.1 on 2020-01-17 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20200117_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningcase',
            name='activity_sequence_id',
        ),
        migrations.RemoveField(
            model_name='runningcase',
            name='role_sequence_id',
        ),
    ]
