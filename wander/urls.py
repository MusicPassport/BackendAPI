from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<pk>', views.EventDetail.as_view(), name='event_detail'),

    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<pk>', views.VenueDetail.as_view(), name='venue_detail'),

    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<pk>', views.ReviewDetail.as_view(), name='review_detail'),

    path('memories/', views.MemoryList.as_view(), name='memory_list'),
    path('memories/<pk>', views.MemoryDetail.as_view(), name='memory_detail'),
    # path('user/<int:pk>/event/<int:pk>')
]
