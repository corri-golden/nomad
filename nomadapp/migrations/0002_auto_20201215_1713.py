# Generated by Django 3.0.3 on 2020-12-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomadapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
