from django.db import models


class ClubTypes(models.TextChoices):
    business = "business",
    entertainment = "entertainment",
    sport = "sport",
    policy = "policy",
