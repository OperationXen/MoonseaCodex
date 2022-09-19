from rest_framework import serializers

from codex.models.events_downtime import CatchingUp


class CatchingUpSerialiser(serializers.ModelSerializer):
    """Serialiser for a catching up event"""
    event_type = serializers.ReadOnlyField(default="dt_catchingup")

    class Meta:
        model = CatchingUp
        fields = ["uuid", "datetime", "character", "levels", "details", "event_type"]
        read_only_fields = ['character']
