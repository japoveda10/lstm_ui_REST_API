# Generated by Django 3.0.1 on 2020-01-14 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_role_role_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_sequence',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.ActivitySequence'),
        ),
    ]
