# Generated by Django 3.2.8 on 2021-10-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(to='wander.Event'),
        ),
    ]