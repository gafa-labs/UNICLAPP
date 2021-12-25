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
from club.serializers import BasicClubSerializer


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    lookup_field = 'pk'


class ClubExploreAPIView(generics.RetrieveAPIView):
    serializer_class = BasicClubSerializer
    queryset = Club.objects.all()

    def get(self, request):
        response_data = {}
        user = request.user
        if user:
            student = user.student
            if student:
                clubs = self.get_queryset()
                serializer = self.get_serializer(clubs, many=True)
                data = serializer.data
                following_clubs = utils.get_following_club_list(student.id)
                response_data["following_clubs"] = following_clubs
                response_data["all_clubs"] = data
                return Response(response_data)
            else:
                return ValidationError({"student": "student does not exists!"})
        return ValidationError({"user": "user does not exists!"})


class ClubFollowingsAPIView(generics.RetrieveAPIView):
    serializer_class = BasicClubSerializer
    queryset = Club.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                following_clubs = utils.get_following_club_list(student.id)
                queryset = Club.objects.filter(id__in=following_clubs)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
