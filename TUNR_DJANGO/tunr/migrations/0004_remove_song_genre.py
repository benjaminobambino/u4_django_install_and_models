# Generated by Django 4.0.2 on 2022-02-01 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0003_song_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
    ]
