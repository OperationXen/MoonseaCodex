# Generated by Django 4.0.4 on 2022-09-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0011_advert_advert_uuid_idx_advert_advert_item_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='dm',
            field=models.ForeignKey(blank=True, help_text='Moonsea Codex DM (optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='codex.dungeonmasterinfo'),
        ),
    ]
