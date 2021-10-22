from rest_framework import serializers
from .models import Event, User




class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ('id','name','events')


class EventSerializer(serializers.ModelSerializer):
    user_list = UserSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Event
        fields = ('id', 'event_name', 'summary', 'city', 'address', 'eventbrite_url',
                    'img_url', 'start', 'end', 'status', 'currency', 'seen', 'user_list')

# class ReviewSerializer(serializers.HyperlinkedModelSerializer):

#     users = serializers.HyperlinkedRelatedField(
#         name='user_detail',
#         many=True,
#         read_only=True
#     )


#     class Meta:
#         model = Review
#         fields = ('id', )
