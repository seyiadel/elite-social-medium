# Generated by Django 4.0.5 on 2022-06-30 12:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eliteapp', '0006_alter_feedpost_feed_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedpost',
            name='feed_id',
        ),
        migrations.AddField(
            model_name='feedpost',
            name='id',
            field=models.UUIDField(default=uuid.UUID('72969203-f8c2-4397-aeb2-8e16e52e4425'), primary_key=True, serialize=False),
        ),
    ]
