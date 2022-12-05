# Generated by Django 4.1.2 on 2022-12-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog_community_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dog_community_app.user')),
            ],
        ),
        migrations.DeleteModel(
            name='EventSubscriptions',
        ),
    ]