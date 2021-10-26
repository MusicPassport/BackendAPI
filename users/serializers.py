from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(UserCreateSerializer):
    # events = serializers.HyperlinkedRelatedField(
    #     view_name='event_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id','username', 'password', 'email')
