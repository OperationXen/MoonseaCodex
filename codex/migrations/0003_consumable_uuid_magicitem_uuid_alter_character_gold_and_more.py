# Generated by Django 4.0.4 on 2022-06-30 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0002_game_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumable',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='magicitem',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='gold',
            field=models.FloatField(blank=True, help_text='Gold held by character (silver and copper in decimal)', null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='dm_name',
            field=models.CharField(default='', help_text='Name of DM', max_length=32),
        ),
    ]
