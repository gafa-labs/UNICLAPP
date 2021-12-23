from django.urls import path
from event import views

urlpatterns = [
    path(
        'events/', views.EventViewset.as_view({"get": "list", "post": "create", "put": "update"}), name='events'),
    path('events/online/',
         views.OnlineEventViewSet.as_view({"get": "list"}), name='online-events'),
    path('events/f2f/',
         views.F2FEventViewSet.as_view({"get": "list"}), name='facetoface-events'),
    path('events/past/',
         views.EventViewset.as_view({"get": "list"}), name='facetoface-events'),
    path("clubs/<int:pk>/events/",
         views.ClubEventsViewSet.as_view({"get": "list"}), name="club-events"),
]
