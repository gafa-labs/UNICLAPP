from django.urls import path
from club import views

urlpatterns = [
    path(
        'clubs/', views.ClubListAPIView.as_view(), name='clubs'),
    path("clubs/<int:pk>/",
         views.ClubDetailAPIView.as_view(), name="club"),
    path("clubs/explore/", views.FollowingClubAPIView.as_view(),
         name="club_explore")
]
