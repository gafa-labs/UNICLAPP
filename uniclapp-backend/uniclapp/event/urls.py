from django.urls import path
from event import views

urlpatterns = [
    path(
        'events/', views.EventAPIView.as_view(), name='events'),
    path(
        'events/<int:pk>/', views.EventDetailAPIView.as_view(), name='event'),
    path(
        'events/past/', views.PastEventAPIView.as_view(), name='past-events'),
    path(
        'events/upcoming/', views.UpcomingEventAPIView.as_view(), name='upcoming-events'),
    path(
        'events/pending/', views.PendingEventAPIView.as_view(), name='pending-events'),
]
