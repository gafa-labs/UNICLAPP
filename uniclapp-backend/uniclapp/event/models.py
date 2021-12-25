from django.db import models
from event import enums
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField(choices=enums.EventTypes.choices)
    event_status = models.TextField(choices=enums.EventStatus.choices)
    club = models.ForeignKey(
        "club.Club", on_delete=models.CASCADE, related_name="%(class)s_events")
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
        if self.datetime < timezone.now():
            return True
        return False

    def calculate_average_rate(self):
        average = self.rate / len(self.evaluations)
        self.rate = average
        self.save(update_fields=["rate"])

    def __str__(self):
        return f'{self.name} - {self.club.name}'


class EventEnrollment(models.Model):
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="enrolled_students")
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="enrolled_events")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.student.student_id} - {self.event.name}'
