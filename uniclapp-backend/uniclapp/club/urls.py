from django.urls import path
from club import views

urlpatterns = [
    path('clubs/', views.ClubViewSet.as_view({"get": "list"}), name='clubs'),
    path("clubs/<int:pk>/",
         views.ClubViewSet.as_view({"get": "retrieve"}), name="club"),
    path("clubs/followings/", views.FollowingClubViewSet.as_view({"get": "list"}),
         name="club_following")

]
