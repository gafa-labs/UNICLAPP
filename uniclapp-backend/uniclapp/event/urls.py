from django.urls import path
from event import views

urlpatterns = [
    path(
        'events/', views.EventAPIView.as_view(), name='events'),
    path(
        'events/<int:pk>/', views.EventDetailAPIView.as_view(), name='event'),
]
