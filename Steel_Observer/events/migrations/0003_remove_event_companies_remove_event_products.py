# Generated by Django 5.1.3 on 2024-12-07 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='event',
            name='products',
        ),
    ]