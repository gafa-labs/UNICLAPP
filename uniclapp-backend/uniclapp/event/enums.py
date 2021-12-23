from django.db import models


class EventStatus(models.TextChoices):
    draft = "draft",
    active = "active",
    past = "past",
    upcoming = "upcoming",
    rejected = "rejected",


class EventTypes(models.TextChoices):
    business = "business",
    entertainment = "entertainment",
    sport = "sport",
    policy = "policy",
