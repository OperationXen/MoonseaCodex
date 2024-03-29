# Generated by Django 4.0.4 on 2022-09-13 07:54

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0012_alter_game_dm'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='codexuser',
            index=models.Index(fields=['email'], name='user_email_idx'),
        ),
        migrations.AddIndex(
            model_name='codexuser',
            index=models.Index(fields=['discord_id'], name='user_discord_id_idx'),
        ),
        migrations.AddIndex(
            model_name='codexuser',
            index=models.Index(django.db.models.functions.text.Upper('discord_id'), name='user_discord_id_upper_idx'),
        ),
        migrations.AddIndex(
            model_name='codexuser',
            index=models.Index(fields=['username'], name='user_username_idx'),
        ),
        migrations.AddIndex(
            model_name='codexuser',
            index=models.Index(django.db.models.functions.text.Upper('username'), name='user_username_upper_idx'),
        ),
    ]
