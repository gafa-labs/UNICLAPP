from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from club import serializers
from club.models import Club, ClubFollowing
from club.serializers import ClubSerializer


class ClubViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin, mixins.CreateModelMixin):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):
        user = request.user
        if user:

            event_queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(event_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        club = Club.objects.filter(pk=pk).first()
        serializer = self.get_serializer(club)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        event = Club.objects.filter(pk=pk)

        if not event:
            content = {'error': 'Club does not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        event.delete()

        return Response(status=status.HTTP_200_OK)


class FollowingClubViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.ClubFollowingSerializer
    queryset = Club.objects.all()

    def list(self, request):
        user = request.user
        if user:
            clubs = self.get_queryset()
            serializer = self.get_serializer(clubs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
