# Generated by Django 3.0.7 on 2020-06-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_remove_photos_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='photo_image',
            field=models.ImageField(default='', upload_to='photos/'),
            preserve_default=False,
        ),
    ]