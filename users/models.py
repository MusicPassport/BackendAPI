from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(verbose_name='email', unique=True,max_length=100)
    # events = models.ForeignKey(
    #     Event, on_delete=models.SET_NULL, related_name='users')
    # attending = models.ManyToManyField('wander.Event', related_name="attendees")
    # watching = models.ManyToManyField('wander.Event', related_name="viewers")
    dark_mode = models.BooleanField(default=False)
    zipcode = models.IntegerField(default=11111)
    # latitude=models.FloatField()
    # longitude= models.FloatField()

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
