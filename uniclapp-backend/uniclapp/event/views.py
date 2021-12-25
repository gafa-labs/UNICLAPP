from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from event import serializers
from event.models import Event, EventEnrollment
from event import utils


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


class EventDestroyAPIView(generics.DestroyAPIView):
    serializer_class = serializers.ClubEventSerializer
    queryset = Event.objects.all()

    def delete(self, request, pk):
        event = Event.objects.get(pk=pk)
        if event:
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


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


class ClubUpcomingEventAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.ClubEventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                boardmember = student.boardmember
                club = boardmember.club
                queryset = Event.objects.filter(club=club)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class EventEnrollmentAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.EventEnrollmentSerializer
    queryset = EventEnrollment.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                event = Event.objects.get(pk=pk)
                if event:
                    if not EventEnrollment.objects.filter(student=student, event=event).exists():
                        event_enrollment = utils.enroll_in_event(
                            student.id, event.id)
                        serializer = self.get_serializer(event_enrollment)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)


class EventCancelEnrollmentAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.EventEnrollmentSerializer
    queryset = EventEnrollment.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                event = Event.objects.get(pk=pk)
                if event:
                    if EventEnrollment.objects.filter(student=student, event=event).exists():
                        return(utils.cancell_enrollment(student.id, event.id))
                    else:
                        return Response(status=status.HTTP_404_NOT_FOUND)


class EventHistoryAPIView(generics.ListAPIView):
    serializer_class = serializers.EventHistorySerializer
    queryset = Event.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                event_enrollments = student.enrolled_events.all()
                serializer = self.get_serializer(event_enrollments, many=True)
                data = serializer.data
                return Response(serializer.data)


class RateEventAPIView(generics.UpdateAPIView):
    serializer_class = serializers.EventEnrollmentSerializer
    queryset = Event.objects.all()

    def put(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                event = Event.objects.get(pk=pk)
                if not EventEnrollment.objects.filter(event=event, student=student).exists():
                    return Response(status=status.HTTP_404_NOT_FOUND)
                event_enrollment = EventEnrollment.objects.get(
                    event=event, student=student)
                data = request.data
                event_enrollment.rate = data["rate"]
                event_enrollment.save()
                data["student"] = student.id
                data["event"] = event.id
                utils.calculate_average_event_rate(event.id)
                return Response(data, status=status.HTTP_201_CREATED)
