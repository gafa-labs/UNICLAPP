from django.urls import path
from accounts import views


urlpatterns = [
    path('register/oem/', views.OEMRegisterAPIView.as_view(),
         name='user-register'),
    path('register/student/', views.StudentRegisterAPIView.as_view(),
         name='student-register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(),
         name='change-password'),
    path('accounts/students/<int:pk>/',
         views.StudentProfileAPIView.as_view(), name='student-profile'),
    path('profiles/student/', views.StudentProfileAPIView.as_view(),
         name='student_profile'),
    path('accounts/rank/promote-student/', views.PromoteStudentAPIView.as_view(),
         name='promote-student'),
    path('accounts/rank/demote-boardmember/<int:pk>/', views.DemoteStudentAPIView.as_view(),
         name='demote-boardmember'),
]
