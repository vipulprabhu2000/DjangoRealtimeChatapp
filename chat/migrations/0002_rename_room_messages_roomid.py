# Generated by Django 4.1.1 on 2022-09-08 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='room',
            new_name='roomid',
        ),
    ]
