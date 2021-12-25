from django.urls import path
from event import views

urlpatterns = [
    path(
        'events/', views.EventAPIView.as_view(), name='events'),
    path(
        'events/<int:pk>/', views.EventDetailAPIView.as_view(), name='event'),
    path(
        'events/create/', views.EventCreateAPIView.as_view(), name='event-create'),
    path(
        'events/<int:pk>/delete/', views.EventDestroyAPIView.as_view(), name='event-delete'),
    path(
        'events/past/', views.PastEventAPIView.as_view(), name='past-events'),
    path(
        'events/all-upcoming-events/', views.UpcomingEventAPIView.as_view(), name='all-upcoming-events'),
    path(
        'events/pending/', views.PendingEventAPIView.as_view(), name='pending-events'),
    path(
        'events/club-events/', views.ClubUpcomingEventAPIView.as_view(), name='club-upcoming-events'),
]
