# Generated by Django 2.2 on 2020-05-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0002_message_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='media_app.User'),
        ),
    ]