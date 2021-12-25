from rest_framework.response import Response
from accounts.models import Student
import event
from event.models import Event, EventEnrollment
from club.utils import get_following_club_list
from club.models import Club
from rest_framework import status


def enroll_in_event(student_id, event_id):
    student = Student.objects.get(id=student_id)
    event = Event.objects.get(id=event_id)
    if student and event:
        enrollment = EventEnrollment.objects.create(
            student=student, event=event)
        return enrollment
    return None


def cancell_enrollment(student_id, event_id):
    student = Student.objects.get(id=student_id)
    event = Event.objects.get(id=event_id)
    enrollment = EventEnrollment.objects.filter(
        student=student, event=event).first()
    if enrollment:
        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def get_student_enrolled_upcoming_events(student_id):
    student = Student.objects.get(id=student_id)
    if student:
        all_enrollments = EventEnrollment.objects.filter(
            student=student).all()
        all_enrollments = list(all_enrollments)
        events = []
        for instance in all_enrollments:
            if instance.event.event_status == "upcoming":
                events.append(instance.event.id)
        return events
    return None


def get_student_clubs_upcoming_events(student_id):
    student = Student.objects.get(id=student_id)
    if student:
        event_list = []
        clubs = get_following_club_list(student.id)
        club_queryset = Club.objects.filter(id__in=clubs)
        for club in club_queryset:
            if club.events:
                event_list.append(club.events.all())
        return event_list
    return None
