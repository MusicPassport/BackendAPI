from django.db import models

# Create your models here.
 
class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postalCode = models.IntegerField()
    venueId = models.CharField(max_length=100)
    venue_url = models.TextField()
    img_url = models.TextField()

    REQUIRED_FIELDS = ['name', 'city']

    def __str__(self):
        return self.name


class Review(models.Model):
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=100)
    venue = models.ForeignKey(
        Venue, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField()
    upvotes = models.IntegerField()
    # downvotes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tm_url = models.TextField()
    img_url = models.TextField()
    eventId = models.CharField(max_length=100)
    start = models.DateTimeField()
    # end = models.DateTimeField()
    # currency = models.CharField(max_length=100)
    venue = models.ForeignKey(
        Venue, related_name='venue_location', on_delete=models.CASCADE, default='')
    attendees = models.ManyToManyField('users.User', related_name='attending')
    viewers = models.ManyToManyField('users.User', related_name='viewing')
    # users = models.CharField()
    # User, on_delete=models.SET_NULL, null=True, related_name='events')

    REQUIRED_FIELDS = ['name', 'city', 'start']
    # USERNAME_FIELD = 'email'

    def get_event(self):
        return self.name

    def __str__(self):
        return self.name
