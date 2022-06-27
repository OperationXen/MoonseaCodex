# Generated by Django 4.0.4 on 2022-06-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='characters',
            field=models.ManyToManyField(help_text='Moonseacodex characters played', related_name='games', to='codex.character'),
        ),
    ]
