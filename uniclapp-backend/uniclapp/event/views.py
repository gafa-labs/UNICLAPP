from django.db.models.query import QuerySet
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from event import serializers
from event.models import Event, EventEnrollment
from event import utils
from club.models import ClubFollowing
from accounts.serializers import StudentSerializer


class EventAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()


class EventDetailAPIView(generics.RetrieveAPIView):
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
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            results = {}
            event_information = []
            if student:
                event_enrollments = EventEnrollment.objects.filter(
                    student=student)
                for enrollment in event_enrollments:
                    event = enrollment.event
                    if event.is_past:
                        event.event_status = "past"
                        event.save()
                        rate = enrollment.rate
                        serializer = serializers.EventSerializer(event)
                        event_information.append(
                            {"event": serializer.data, "rate": rate})
                results["events"] = event_information

                return Response(results)


class RateEventAPIView(generics.UpdateAPIView):
    serializer_class = serializers.EventEnrollmentSerializer
    queryset = Event.objects.all()

    def put(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                event = Event.objects.get(pk=pk)
                event_enrollment = EventEnrollment.objects.get(event=event)
                data = request.data
                event_enrollment.rate = data["studentRate"]
                event_enrollment.save()
                data["student"] = student.id
                data["event"] = event_enrollment.event.id
                utils.calculate_average_event_rate(event_enrollment.event.id)
                return Response(data, status=status.HTTP_201_CREATED)


class EventTrackerAPIView(generics.ListAPIView):
    serializer_class = serializers.EventTrackerSerializer
    queryset = Event.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            upcoming_events = utils.get_student_enrolled_all_events(
                student.id)
            queryset = Event.objects.filter(id__in=upcoming_events)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class OEMEventAPIView(generics.ListAPIView):
    serializer_class = serializers.AdvancedEventSerializer
    queryset = Event.objects.exclude(event_status="past")


class OEMConfirmationAPIView(generics.UpdateAPIView):
    serializer_class = serializers.EventConfirmationSerializer
    queryset = Event.objects.all()


class EventResultsAPIView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()

    def get(self, request):

        user = request.user
        if user:
            student = user.student
            if student:
                boardmember = student.boardmember
                if boardmember:
                    club = boardmember.club
                    events = Event.objects.filter(club=club)
                    serializer = self.get_serializer(events, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
