# Generated by Django 3.0.7 on 2022-06-14 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0003_user_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated',
        ),
    ]
