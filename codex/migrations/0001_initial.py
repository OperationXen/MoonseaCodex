# Generated by Django 4.0.4 on 2022-06-20 20:09

import codex.models.character
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodexUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('discord_id', models.CharField(blank=True, help_text='Discord ID for bot integration', max_length=32, null=True, unique=True)),
                ('email_verified', models.BooleanField(default=False, help_text='User has verified their email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Codex User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(default='Unnamed character', max_length=64)),
                ('artwork', models.ImageField(blank=True, null=True, upload_to=codex.models.character.get_user_artwork_path)),
                ('token', models.ImageField(blank=True, null=True, upload_to=codex.models.character.get_user_token_path)),
                ('sheet', models.URLField(blank=True, help_text='Link to DND Beyond character sheet', max_length=256, null=True)),
                ('public', models.BooleanField(default=True, help_text='Allow anyone to view this character')),
                ('season', models.CharField(blank=True, default='11', help_text='AL season that this character was created', max_length=32, null=True)),
                ('race', models.CharField(blank=True, max_length=32, null=True)),
                ('level', models.IntegerField(default=1, help_text='Total level')),
                ('classes', models.JSONField(default=dict, help_text='A JSON object detailing current classes')),
                ('gold', models.FloatField(help_text='Gold held by character (silver and copper in decimal)', null=True)),
                ('downtime', models.FloatField(blank=True, help_text='Days of downtime', null=True)),
                ('ac', models.IntegerField(help_text='Base armour class', null=True, verbose_name='AC')),
                ('hp', models.IntegerField(help_text='Max HP', null=True, verbose_name='HP')),
                ('pp', models.IntegerField(help_text='Passive perception', null=True, verbose_name='PP')),
                ('dc', models.IntegerField(help_text='Spell Save DC', null=True, verbose_name='DC')),
                ('vision', models.CharField(blank=True, help_text='Any special vision modes (eg darkvision)', max_length=64, null=True)),
                ('biography', models.TextField(blank=True, help_text='Character biography', null=True)),
                ('dm_text', models.TextField(blank=True, help_text='Any information that may be useful for your DM to know ahead of time', null=True, verbose_name='DM help text')),
                ('player', models.ForeignKey(help_text='The player who owns this character', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DungeonMasterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('hours', models.IntegerField(blank=True, default=0, help_text='Total number of DMing service hours unspent')),
                ('player', models.ForeignKey(help_text='The player this DM log belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='dm_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dungeon Master Info',
                'verbose_name_plural': 'Dungeon Master Records',
            },
        ),
        migrations.CreateModel(
            name='MagicItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Item Name', max_length=32)),
                ('equipped', models.BooleanField(default=False, help_text='Item is currently equipped by its owner')),
                ('rarity', models.CharField(choices=[('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('veryrare', 'Very Rare'), ('legendary', 'Legendary')], default='uncommon', help_text='Item rarity', max_length=16)),
                ('attunement', models.BooleanField(default=False, help_text='Item requires attunement to be used')),
                ('description', models.TextField(blank=True, null=True)),
                ('flavour', models.TextField(blank=True, help_text='Flavour text', null=True)),
                ('object_id', models.PositiveIntegerField(help_text='ID of the specific source event', null=True, verbose_name='Event ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magicitems', to='codex.character')),
                ('content_type', models.ForeignKey(help_text='Type of event that resulted in this object coming to you', null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Origin Type')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(blank=True, help_text='Optional character name', max_length=64, null=True)),
                ('recipient_name', models.CharField(blank=True, help_text='Optional character name', max_length=64, null=True)),
                ('associated', models.ForeignKey(help_text='The other half of the trade', null=True, on_delete=django.db.models.deletion.SET_NULL, to='codex.trade')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codex.magicitem')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traded_in', to='codex.character')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traded_out', to='codex.character')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('name', models.CharField(blank=True, help_text='Module name', max_length=32, null=True)),
                ('dm_name', models.CharField(default='', help_text='Name of DM (optional)', max_length=32)),
                ('notes', models.CharField(blank=True, help_text='Public DM notes for game', max_length=512, null=True)),
                ('module', models.CharField(help_text='Module code', max_length=32)),
                ('hours', models.IntegerField(default=0, help_text='DM Hours claimed')),
                ('hours_notes', models.CharField(blank=True, help_text='Time breakdown for game', max_length=256, null=True)),
                ('location', models.CharField(blank=True, help_text='Where the game was organised or run', max_length=64, null=True)),
                ('gold', models.IntegerField(default=0, help_text='Gold awarded')),
                ('downtime', models.IntegerField(default=0, help_text='Days of downtime')),
                ('levels', models.IntegerField(default=0, help_text='Levels to take')),
                ('dm', models.ForeignKey(help_text='Moonsea Codex DM (optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='codex.dungeonmasterinfo')),
            ],
        ),
        migrations.CreateModel(
            name='DMReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Service reward name', max_length=32, null=True)),
                ('hours', models.IntegerField(default=0, help_text='Number of service hours spent', null=True)),
                ('gold', models.IntegerField(default=0, help_text='Gold awarded')),
                ('downtime', models.IntegerField(default=0, help_text='Days of downtime')),
                ('levels', models.IntegerField(default=0, help_text='Bonus levels to assign')),
                ('character_items_assigned', models.ForeignKey(blank=True, help_text='Character given item / gold / downtime rewards', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dm_items', to='codex.character')),
                ('character_level_assigned', models.ForeignKey(blank=True, help_text='Character given levels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dm_levels', to='codex.character')),
                ('dm', models.ForeignKey(help_text='Moonsea Codex DM', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='codex.dungeonmasterinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Item Name', max_length=32)),
                ('type', models.TextField(choices=[('scroll', 'Spell scroll'), ('potion', 'Potion'), ('ammo', 'Ammunition'), ('gear', 'Adventuring Gear')], default='gear', help_text='Item type')),
                ('count', models.IntegerField(help_text='Number of charges / items remaining', null=True)),
                ('rarity', models.CharField(choices=[('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('veryrare', 'Very Rare'), ('legendary', 'Legendary')], default='uncommon', help_text='Item rarity', max_length=16)),
                ('description', models.TextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(help_text='ID of the specific source event', null=True, verbose_name='Event ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumables', to='codex.character')),
                ('content_type', models.ForeignKey(help_text='Type of event that resulted in this object coming to you', null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Origin Type')),
            ],
        ),
        migrations.AddConstraint(
            model_name='codexuser',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Upper('username'), name='username_unique'),
        ),
        migrations.AddConstraint(
            model_name='codexuser',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Upper('email'), name='email_unique'),
        ),
        migrations.AddConstraint(
            model_name='codexuser',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Upper('discord_id'), name='discord_id_unique'),
        ),
    ]
