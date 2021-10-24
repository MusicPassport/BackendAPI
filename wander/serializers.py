from rest_framework import serializers
from .models import Event, Review, Venue


class EventSerializer(serializers.ModelSerializer):
    # user_list = UserSerializer(
    #     many=True,
    #     read_only=True
    # )
    user_list = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Event
        fields = ('id', 'name', 'genre', 'city', 'address', 'state','tm_url',
                    'img_url', 'start', 'attendees', 'viewers', 'user_list')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ( 'id','name', 'address', 'city', 'state', 'postalCode',
                    'venueId', 'venue_url', 'img_url')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    # owner = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     many=True,
    #     read_only=True
    # )
    venue= VenueSerializer(
        many=False,
        read_only=True
    )

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Review
        fields = ('id', 'owner', 'title', 'venue', 'body', 'upvotes' )
