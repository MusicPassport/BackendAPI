# Generated by Django 3.2.8 on 2021-10-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0002_auto_20211021_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(related_name='_wander_event_users_+', to='wander.Event'),
        ),
    ]