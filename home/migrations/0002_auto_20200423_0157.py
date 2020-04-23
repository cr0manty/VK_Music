# Generated by Django 2.2.10 on 2020-04-22 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myapp',
            name='details',
            field=models.TextField(default='Your version is out of date, please upgrade to a new version.'),
        ),
        migrations.AddField(
            model_name='myapp',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myapp',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myapp',
            name='version',
            field=models.CharField(default=0, help_text='0.0.1', max_length=10),
            preserve_default=False,
        ),
    ]