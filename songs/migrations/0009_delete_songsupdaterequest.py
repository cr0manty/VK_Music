# Generated by Django 2.2.10 on 2020-07-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_song_ignore_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SongsUpdateRequest',
        ),
    ]
