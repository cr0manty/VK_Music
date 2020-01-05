# Generated by Django 3.0.1 on 2020-01-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dump_password',
            new_name='vk_password',
        ),
        migrations.AddField(
            model_name='user',
            name='vk_login',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
