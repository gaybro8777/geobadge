from rest_framework import serializers
from geobadge.accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:user-detail'
    )

    first_name = serializers.CharField(
        allow_blank=False
    )

    last_name = serializers.CharField(
        allow_blank=False
    )

    class Meta:
        model = User
        fields = (
            'id', 'url',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
        )
