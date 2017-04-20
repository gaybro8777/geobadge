from rest_framework import serializers
from geobadge.badges.models import Badge


class BadgeSerializer(serializers.ModelSerializer):

    href = serializers.HyperlinkedIdentityField(
        view_name='api:badge-detail'
    )

    class Meta:
        model = Badge
        fields = (
            'id', 'href', 'created',
        )
