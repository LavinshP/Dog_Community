# Generated by Django 4.1.2 on 2022-12-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_community_app', '0012_dogs_dog_image_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogs',
            name='dog_image_upload',
        ),
        migrations.AlterField(
            model_name='dogs',
            name='dog_image',
            field=models.ImageField(blank=True, upload_to='assets/img/'),
        ),
    ]