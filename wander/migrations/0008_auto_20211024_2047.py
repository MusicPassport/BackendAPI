# Generated by Django 3.2.8 on 2021-10-24 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0007_auto_20211024_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='venue_reviewed', to='wander.review'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='postalCode',
            field=models.IntegerField(),
        ),
    ]