from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models
# from '../wander/serializers.py' import EventSerializer
from wander.serializers import EventSerializer


class UserCreateSerializer(UserCreateSerializer, serializers.ModelSerializer):
    attending = EventSerializer(
        many=True,
        read_only=True
    )

    viewing = EventSerializer(
        many=True,
        read_only=True
    )

    events = EventSerializer(
        many=True,
        read_only=True
    )
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id','username', 'password', 'email','attending','viewing','events')
