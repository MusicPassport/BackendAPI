from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('user/', views.UserList.as_view(), name='user_list'),
    # path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]
