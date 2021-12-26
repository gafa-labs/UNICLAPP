from django.db import models
from club import enums


class Club(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    category = models.CharField(max_length=20, choices=enums.ClubTypes.choices)

    @property
    def number_of_followers(self):
        return len(self.followers.all())

    @property
    def number_of_events(self):
        return len(self.events.all())

    @property
    def number_of_total_participants(self):
        all_events = self.events.all()
        number_of_participants = 0
        for event in all_events:
            event_participants = len(event.enrolled_students.all())
            number_of_participants += event_participants
        return number_of_participants

    @property
    def rate(self):
        all_events = self.events.all()
        total_event_rate = 0
        for event in all_events:
            total_event_rate += event.rate
        if self.number_of_total_participants != 0:
            return total_event_rate / self.number_of_total_participants
        else:
            return 0.0

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
