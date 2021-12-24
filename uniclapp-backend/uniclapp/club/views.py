from django.db.models.query import QuerySet
from django.http.request import validate_host
from django.shortcuts import render
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from club import serializers
from club.models import Club, ClubFollowing
from club.serializers import ClubSerializer
from accounts.models import Student
from accounts.serializers import StudentSerializer
from club import utils


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    lookup_field = 'pk'


class FollowingClubAPIView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request):
        response_data = {}
        user = request.user
        if user:
            student = self.get_queryset(user=user)
            if student:
                data = self.get_serializer(student)
                clubs = utils.get_following_club_list(student.first().id)
                print(clubs)
                response_data["following_clubs"] = clubs
                response_data["student"] = data
                return Response(response_data)
            else:
                return ValidationError({"student": "student does not exists!"})
        return ValidationError({"user": "user does not exists!"})
