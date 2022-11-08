# Generated by Django 4.1.2 on 2022-11-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_community_app', '0006_dogs_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='dog_image',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='team',
            name='member_image',
            field=models.CharField(default='', max_length=1024),
        ),
    ]