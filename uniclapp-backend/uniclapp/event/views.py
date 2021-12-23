from django.shortcuts import render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from event import serializers
from event.models import Event


class EventAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()
    lookup_field = "pk"


class OnlineEventAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.OnlineEventSerializer
    queryset = Event.objects.filter(is_online=True)

    def list(self, request):
        online_event_queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(online_event_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class F2FEventViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.F2FEventSerializer
    queryset = Event.objects.filter(is_online=False)

    def list(self, request):
        f2f_event_queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(f2f_event_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClubEventsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def list(self, request, pk):
        events = Event.objects.filter(club=pk)
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
