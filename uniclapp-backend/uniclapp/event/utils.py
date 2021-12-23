from accounts.models import Student
import event
from event.models import Event, EventEnrollment


def enroll_in_event(student_id, event_id):

    student = Student.objects.get(id=student_id)
    event = Event.objects.get(id=event_id)
    if student and event:
        enrollment = EventEnrollment.objects.crete(
            student=student, event=event)

    return enrollment


def cancell_enrollment(student_id, event_id):
    student = Student.objects.get(id=student_id)
    event = Event.objects.get(id=event_id)
    enrollment = EventEnrollment.objects.filter(
        student=student, event=event).first()
    if enrollment:
        enrollment.delete()
