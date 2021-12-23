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
]
