from os import readv
from django.db.models.query import QuerySet
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, ReviewSerializer, VenueSerializer, MemorySerializer
from .models import Event, Venue, Review, Memory
from wander.permissions import IsOwnerOrReadOnly

# Create your views here.
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): serializer.save(
        owner=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsOwnerOrReadOnly]

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): serializer.save(
        owner=self.request.user)


class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    permission_classes = [IsOwnerOrReadOnly]

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

    permission_classes = [IsOwnerOrReadOnly]
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
