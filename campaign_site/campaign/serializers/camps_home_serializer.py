from rest_framework import serializers
from campaign.models import campaign_entity


class CampsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaign_entity
        fields = [
            'id',
            'name',
        ]
