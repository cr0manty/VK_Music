# Generated by Django 3.0.1 on 2019-12-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20191220_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_id',
            field=models.IntegerField(null=True),
        ),
    ]
