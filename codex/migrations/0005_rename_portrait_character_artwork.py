# Generated by Django 4.0.4 on 2022-06-18 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0004_character_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='portrait',
            new_name='artwork',
        ),
    ]
