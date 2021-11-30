from django.shortcuts import render
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from uniclapp.club import models, serializers


class ClubViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = serializers.ClubSerializer
    queryset = models.Club.objects.all()
