from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    summary = models.TextField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    eventbrite_url = models.TextField()
    img_url = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    seen = models.BooleanField(default=False)
    # users = models.CharField()
        # User, on_delete=models.SET_NULL, null=True, related_name='events')

    REQUIRED_FIELDS = ['name', 'city', 'start', 'end']
    # USERNAME_FIELD = 'email'

    def get_event(self):
        return f"{self.event_name}:{self.summary}"


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # events = models.ForeignKey(
    #     Event, on_delete=models.SET_NULL, related_name='users')
    events = models.ManyToManyField(Event, related_name="user_list")

    def __str__(self):
        return self.name

    
    
    
# class Review(models.Model):
#     user=models.ForeignKey(User, related_name='reviews', on_delete='CASCADE')
#     body=models.TextField()
#     upvotes=models.IntegerField()
