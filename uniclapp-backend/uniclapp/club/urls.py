from django.urls import path
from club import views

urlpatterns = [
    path(
        'clubs/', views.ClubListAPIView.as_view(), name='clubs'),
    path("clubs/<int:pk>/",
         views.ClubDetailAPIView.as_view(), name="club"),
    path("clubs/explore/", views.ClubExploreAPIView.as_view(),
         name="club_explore"),
    path("clubs/followings/", views.ClubFollowingsAPIView.as_view(),
         name="club_following"),
    path("clubs/followings/follow/<int:pk>/", views.ClubFollowingsFollowAPIView.as_view(),
         name="club_following-follow"),
    path("clubs/followings/unfollow/<int:pk>/", views.ClubFollowingsUnfollowAPIView.as_view(),
         name="club_following-unfollow"),
    path("clubs/leaderboard/", views.LeaderBoardAPIView.as_view(),
         name="club_leader_board"),
    path("club/boardmembers/", views.ClubBoardMemberListAPIView.as_view(),
         name="club-boardmembers"),



]
