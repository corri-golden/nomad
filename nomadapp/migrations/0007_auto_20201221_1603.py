# Generated by Django 3.1.4 on 2020-12-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomadapp', '0006_auto_20201217_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
