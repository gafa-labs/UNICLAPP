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
        'events/<int:pk>/enroll/', views.EventEnrollmentAPIView.as_view(), name='enroll-event'),
    path(
        'events/<int:pk>/cancel-enrollment/', views.EventCancelEnrollmentAPIView.as_view(), name='cancel-enrollment'),
    path(
        'events/past/', views.PastEventAPIView.as_view(), name='past-events'),
    path(
        'events/all-upcoming-events/', views.UpcomingEventAPIView.as_view(), name='all-upcoming-events'),
    path(
        'events/pending/', views.PendingEventAPIView.as_view(), name='pending-events'),
    path(
        'events/club-events/', views.ClubUpcomingEventAPIView.as_view(), name='club-upcoming-events'),
    path(
        'events/event-history/', views.EventHistoryAPIView.as_view(), name='club-upcoming-events'),
    path(
        'events/<int:pk>/rate-event/', views.RateEventAPIView.as_view(), name='rate-event'),
    path(
        'events/event-tracker/', views.EventTrackerAPIView.as_view(), name='event-tracker'),
    path(
        'events/oem/', views.OEMEventAPIView.as_view(), name='oem-events'),
    path(
        'events/oem/<int:pk>/', views.OEMConfirmationAPIView.as_view(), name='event-confirmation'),
    path(
        'events/results/', views.EventResultsAPIView.as_view(), name='event-results'),
]
