# Generated by Django 3.0.1 on 2020-01-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exception', models.TextField(blank=True, null=True)),
                ('additional_text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
