# Generated by Django 4.0.1 on 2022-02-21 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('wiki', 'Wiki'), ('youtube', 'Youtube'), ('twitter', 'Twitter'), ('article', 'Article'), ('cooperation', 'Cooperation')], default='article', max_length=50),
        ),
    ]
