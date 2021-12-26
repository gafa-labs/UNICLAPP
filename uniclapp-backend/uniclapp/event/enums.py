from django.db import models


class EventStatus(models.TextChoices):
    pending = "pending",
    past = "past",
    upcoming = "upcoming",
    rejected = "rejected",
