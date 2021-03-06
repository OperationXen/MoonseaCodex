from rest_framework import serializers

from codex.models.dungeonmaster import DungeonMasterInfo
from codex.models.events import DMReward, Game


class DMLogSerialiser(serializers.ModelSerializer):
    """ Serialise a dungeon master log record """
    dm_name = serializers.ReadOnlyField(source='player.username', read_only=True)

    class Meta:
        model = DungeonMasterInfo
        fields = ['dm_name', 'hours', 'uuid']
        read_only_fields = ['uuid']


class DMRewardSerialiser(serializers.ModelSerializer):
    """ serialiser for creating and viewing DMRewards records """

    class Meta:
        model = DMReward
        fields = ['uuid', 'datetime', 'dm', 'name', 'gold', 'downtime', 'hours', 'character_level_assigned', 'character_items_assigned']
        read_only_fields = ['uuid']


class DMRewardUpdateSerialiser(serializers.ModelSerializer):
    """ serialiser for allowing updates to DMRewards records """

    class Meta:
        model = DMReward
        fields = ['uuid', 'datetime', 'dm', 'name', 'gold', 'downtime', 'hours', 'character_level_assigned', 'character_items_assigned']
        read_only_fields =['uuid', 'dm']


class DMRewardDisplaySerialiser(serializers.ModelSerializer):
    """ Converts DMRewards for display """
    dm_uuid = serializers.ReadOnlyField(source="dm.uuid")
    character_level_assigned = serializers.ReadOnlyField(source='character_level_assigned.uuid')
    character_items_assigned = serializers.ReadOnlyField(source='character_items_assigned.uuid')

    class Meta:
        model = DMReward
        fields = ['uuid', 'datetime', 'dm_uuid', 'name', 'gold', 'downtime', 'hours', 'character_level_assigned', 'character_items_assigned']
