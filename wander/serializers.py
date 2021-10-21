from rest_framework import serializers
from .models import Event, User


class EventSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Event
        fields = ('id', 'event_name' ,'summary','city','address','eventbrite_url','img_url','start','end','status','currency','seen','users')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ('id','name','events')

# class ReviewSerializer(serializers.HyperlinkedModelSerializer):

#     users = serializers.HyperlinkedRelatedField(
#         name='user_detail',
#         many=True,
#         read_only=True
#     )


#     class Meta:
#         model = Review
#         fields = ('id', )
