from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from event import serializers
from event.models import Event

"""
class EventRetrieveAPI(generics.RetrieveAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

"""


class EventViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):
        event_queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(event_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        event = Event.objects.filter(pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        event = Event.objects.filter(pk=pk)

        if not event:
            content = {'error': 'Event does not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        event.delete()

        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class OnlineEventViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
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
