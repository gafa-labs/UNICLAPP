from django.db import models
from django.db.models.deletion import SET_NULL
from event import enums
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField(choices=enums.EventTypes.choices)
    status = models.TextField(choices=enums.EventStatus.choices)
    club = models.OneToOneField(
        "club.Club", on_delete=models.CASCADE, related_name="%(class)s_events")
    about = models.TextField()
    ge_status = models.BooleanField(default=False)
    ge_point = models.IntegerField(default="10")
    duration = models.FloatField(default=0)
    capacity = models.IntegerField(default=0)
    is_online = models.BooleanField(default=False)
    zoom_link = models.URLField(blank=True)
    building = models.ForeignKey(
        "place.Building", on_delete=SET_NULL, blank=True, null=True)
    datetime = models.DateTimeField()

    @property
    def is_past(self):
        if self.date < timezone.now():
            return True
        return False


class EventEnrollment(models.Model):
    student = models.OneToOneField(
        "accounts.Student", on_delete=models.CASCADE, related_name="enrolled_students")
    event = models.OneToOneField(
        Event, on_delete=models.CASCADE, related_name="enrolled_events")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
