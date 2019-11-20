# Generated by Django 2.2.7 on 2019-11-20 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='runningcase',
            name='prefixes',
            field=models.CharField(choices=[('task_num', 'Task number'), ('task', 'Task')], default='', max_length=1000),
        ),
    ]
