# Generated by Django 2.2.10 on 2020-05-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_appversions_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myapp',
            name='android_app',
        ),
        migrations.RemoveField(
            model_name='myapp',
            name='ios_app',
        ),
        migrations.AddField(
            model_name='appversions',
            name='android_app',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appversions',
            name='ios_app',
            field=models.URLField(blank=True, null=True),
        ),
    ]
