# Generated by Django 4.1.3 on 2023-09-08 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinylvaultapi', '0004_alter_record_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='record',
            name='track_list',
        ),
    ]
