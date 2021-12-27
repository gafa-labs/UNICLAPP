from django.db import models
from event import enums
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_status = models.TextField(
        choices=enums.EventStatus.choices, default=enums.EventStatus.pending)
    club = models.ForeignKey(
        "club.Club", on_delete=models.CASCADE, related_name="events")
    description = models.TextField()
    ge_status = models.BooleanField(default=False)
    ge_point = models.IntegerField(default="10")
    is_online = models.BooleanField(default=False)
    zoom_link = models.URLField(blank=True)
    location = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    rate = models.FloatField(default=0, validators=[
        MinValueValidator(0), MaxValueValidator(5)])

    @property
    def is_past(self):
        if self.end_datetime < timezone.now():
            if self.event_status == "upcoming":
                self.event_status = "past"
                self.save(update_fields=["event_status"])
            return True
        return False

    @property
    def number_of_participants(self):
        return len(self.enrolled_students.all())

    def __str__(self):
        return f'{self.name} - {self.club.name}'


class EventEnrollment(models.Model):
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="enrolled_events")
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="enrolled_students")
    created = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.student.student_id} - {self.event.name}'
