# Generated by Django 4.0.4 on 2022-05-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0003_magicitem_attunement_magicitem_equipped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='portrait',
        ),
        migrations.AddField(
            model_name='character',
            name='artwork',
            field=models.ImageField(blank=True, null=True, upload_to='character/artwork'),
        ),
        migrations.AlterField(
            model_name='character',
            name='token',
            field=models.ImageField(blank=True, null=True, upload_to='character/tokens'),
        ),
    ]