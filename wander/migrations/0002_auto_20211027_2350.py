# Generated by Django 3.2.8 on 2021-10-27 23:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wander', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attending', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='viewing', to=settings.AUTH_USER_MODEL),
        ),
    ]
