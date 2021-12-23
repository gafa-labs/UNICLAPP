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


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    lookup_field = 'pk'


class FollowingClubAPIView(generics.ListAPIView):
    serializer_class = serializers.ClubFollowingSerializer
    queryset = Club.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = Student.objects.get(user=user)
            if student:
                clubs = student.followees.all()
                serializer = self.get_serializer(request.data)
                data = serializer.data
                data["clubs"] = clubs
                return Response(data)
            else:
                return ValidationError({"student": "student does not exists!"})
        return ValidationError({"user": "user does not exists!"})
