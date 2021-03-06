# Generated by Django 3.0.1 on 2020-01-18 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200118_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningcase',
            name='activity_sequence_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.ActivitySequence'),
        ),
        migrations.AddField(
            model_name='runningcase',
            name='event_log_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.EventLog'),
        ),
        migrations.AddField(
            model_name='runningcase',
            name='role_sequence_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.RoleSequence'),
        ),
    ]
