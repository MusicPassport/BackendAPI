from rest_framework import serializers
from .models import Event, Memory, Review, Venue
# from users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    # attending = UserSerializer(
    #     data={'id', 'username'},
    #     many=True,
    #     read_only=True
    # )
    # viewing = UserSerializer(
    #     data = {'id','username'},
    #     many=True,
    #     read_only=True
    # )

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Event
        fields = ('id', 'name', 'owner', 'genre', 'city', 'address', 'state','tm_url','venue',
                    'img_url', 'start', 'attendees', 'viewers','owner')




class ReviewSerializer(serializers.ModelSerializer):

    # venue= VenueSerializer(
    #     many=False,
    #     read_only=True
    # )

    # venue_id = serializers.PrimaryKeyRelatedField(
    #     queryset = Venue.objects.all(),
    #     source='venue'
    # )

    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Review
        fields = ('id','owner', 'title', 'venue', 'body')


class VenueSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Venue
        fields = ('id', 'name', 'owner', 'address', 'city', 'state', 'postalCode',
                  'venueId', 'venue_url', 'img_url', 'reviews')

class MemorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # event = EventSerializer( many=False, read_only=True)
    class Meta:
        model = Memory
        fields = ('id', 'title', 'body', 'photo', 'owner', 'event')
