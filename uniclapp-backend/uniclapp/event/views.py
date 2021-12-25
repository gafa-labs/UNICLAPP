from django.shortcuts import render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from event import serializers
from event.models import Event
from event import utils
from itertools import chain


class EventAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()
    lookup_field = "pk"


class EventCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def post(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                boardmember = student.boardmember
                club_id = boardmember.club.id
                data = request.data
                data["club"] = club_id
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)


class PastEventAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        past_events = [x for x in Event.objects.all() if x.is_past]
        serializer = self.get_serializer(past_events, many=True)
        return Response(serializer.data)


class UpcomingEventAPIView(generics.ListAPIView):
    serializer_class = serializers.BasicEventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                response_data = {}
                all_upcoming_events = [
                    x for x in Event.objects.all() if x.event_status == "upcoming"]
                serializer = self.get_serializer(
                    all_upcoming_events, many=True)
                data = serializer.data

                enrolled_events = utils.get_student_enrolled_upcoming_events(
                    student.id)
                queryset = Event.objects.filter(id__in=enrolled_events)
                serializer = self.get_serializer(queryset)
                response_data["all_upcoming_events"] = data
                response_data["enrolled_events"] = enrolled_events
                """
                upcoming_events = [
                    x for x in Event.objects.all() if not x.is_past]
                serializer = self.get_serializer(upcoming_events, many=True)
                """
                return Response(response_data)


class AUpcomingEventAPIView(generics.ListAPIView):
    serializer_class = serializers.BasicEventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                response_data = {}
                clubs_upcoming_events = utils.get_student_clubs_upcoming_events(
                    student.id)
                print(clubs_upcoming_events)

                enrolled_events = utils.get_student_enrolled_upcoming_events(
                    student.id)
                queryset = Event.objects.filter(id__in=enrolled_events)
                serializer = self.get_serializer(queryset)
                response_data["all_upcoming_events"] = data
                response_data["enrolled_events"] = enrolled_events
                """
                upcoming_events = [
                    x for x in Event.objects.all() if not x.is_past]
                serializer = self.get_serializer(upcoming_events, many=True)
                """
                return Response(response_data)


class PendingEventAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.filter(event_status="pending")


class ClubEventsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def list(self, request, pk):
        events = Event.objects.filter(club=pk)
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
