# Generated by Django 2.2.10 on 2020-06-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_user_last_songs_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='vk_password',
        ),
        migrations.AddField(
            model_name='user',
            name='vk_auth_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
