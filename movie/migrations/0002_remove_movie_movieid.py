# Generated by Django 4.0.1 on 2022-02-03 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movieid',
        ),
    ]
