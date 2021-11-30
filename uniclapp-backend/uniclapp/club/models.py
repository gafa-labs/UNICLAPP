from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import TextChoices
from club import enums
from django.core.validators import MinValueValidator, MaxValueValidator


class Club(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.ImageField(upload_to="clubs/logos", null=True, blank=True)
    rate = models.FloatField(default=0)
    category = models.CharField(max_length=20, choices=enums.ClubTypes.choices)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=10, choices=enums.BuildingNames.choices)
    available = models.BooleanField(default=True)


class Classroom(models.Model):
    name = models.CharField(
        max_length=3, choices=enums.ClassrooomNames.choices)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="classrooms")
    available = models.BooleanField(default=True)


class Event(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="events")
    poster = models.ImageField(
        upload_to="clubs/{self.name}/events", null=True, blank=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
    ge_status = models.BooleanField(default=False)
    online = models.BooleanField(default=False),
    zoom_link = models.URLField()
    building = models.ForeignKey(
        Building, on_delete=SET_NULL, blank=True, null=True)


class Evaluation(models.Model):
    owner = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="evaluations")
    content = models.TextField()
    rate = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(10)])
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="evaluations")
    date = models.DateTimeField(auto_now_add=True)
