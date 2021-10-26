from django.contrib import admin
from .models import Event, Venue, Review, Memory

# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Review)
admin.site.register(Memory)
