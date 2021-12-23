from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import TextChoices
from club import enums


class Club(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    rate = models.FloatField(default=0)
    category = models.CharField(max_length=20, choices=enums.ClubTypes.choices)

    @property
    def number_of_followers(self):
        return len(self.followers.all())

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ClubFollowing(models.Model):
    student = models.OneToOneField(
        "accounts.Student", on_delete=models.CASCADE, related_name="followees")
    club = models.OneToOneField(
        Club, on_delete=models.CASCADE, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        f"{self.studen.full_name} follows {self.club.name}"
