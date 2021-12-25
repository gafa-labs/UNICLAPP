from django.db import models
from django.db.models.deletion import CASCADE
from club import enums


class Club(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    rate = models.FloatField(default=0, validators=[
        MinValueValidator(0), MaxValueValidator(5)])
    category = models.CharField(max_length=20, choices=enums.ClubTypes.choices)

    @property
    def number_of_followers(self):
        return len(self.followers.all())

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def calculate_average_rate(self):
        average = self.rate / len(self.events)
        self.rate = average
        self.save(update_fields=["rate"])


class ClubFollowing(models.Model):
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="followees")
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.student.student_id} follows {self.club.name}"
