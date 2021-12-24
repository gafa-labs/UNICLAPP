from django.urls import path
from accounts import views


urlpatterns = [
    path('register/', views.StudentRegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('accounts/students/<int:pk>/',
         views.StudentProfileAPIView.as_view(), name='student-profile'),
    path('profiles/student/', views.StudentProfileAPIView.as_view(),
         name='student_profile'),
    # path('profiles/board-member/', views.StudentProfileAPIView.as_view(),
    # name='board_member_profile'),
    # path('profiles/board-chairman/', views.StudentProfileAPIView.as_view(),
    # name='board_chairman_profile'),
    # path('profiles/club-advisor/', views.StudentProfileAPIView.as_view(),
    # name='club_advisor_profile'),
    # path('profiles/oem/', views.StudentProfileAPIView.as_view(),
    # name='oem_proile'),
]
