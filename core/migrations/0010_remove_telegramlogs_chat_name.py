# Generated by Django 2.2.10 on 2020-06-17 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_telegramlogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramlogs',
            name='chat_name',
        ),
    ]