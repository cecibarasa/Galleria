# Generated by Django 3.0.7 on 2020-06-26 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20200626_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='photo_image',
        ),
    ]
