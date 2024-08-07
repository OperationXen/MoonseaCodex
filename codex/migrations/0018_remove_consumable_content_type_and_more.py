# Generated by Django 4.0.4 on 2024-07-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0017_spellbookupdate_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumable',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='consumable',
            name='count',
        ),
        migrations.RemoveField(
            model_name='consumable',
            name='object_id',
        ),
        migrations.AddField(
            model_name='consumable',
            name='charges',
            field=models.IntegerField(blank=True, help_text='Number of charges', null=True),
        ),
        migrations.AddField(
            model_name='consumable',
            name='equipped',
            field=models.BooleanField(default=False, help_text='Item is currently equipped by its owner'),
        ),
        migrations.AlterField(
            model_name='consumable',
            name='type',
            field=models.TextField(choices=[('scroll', 'Spell scroll'), ('potion', 'Potion'), ('ammo', 'Ammunition'), ('gear', 'Adventuring Gear'), ('other', 'Other item')], default='scroll', help_text='Item type'),
        ),
    ]
