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
