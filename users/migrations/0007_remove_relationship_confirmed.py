# Generated by Django 3.0.1 on 2020-01-07 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200107_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='confirmed',
        ),
    ]