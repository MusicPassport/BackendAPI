from os import readv
from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import EventSerializer, ReviewSerializer, VenueSerializer, IemorymageSerializer
from .models import Event, Venue, Review, Memory

# Create your views here.
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MemoryList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
