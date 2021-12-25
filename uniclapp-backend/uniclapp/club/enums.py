from django.db import models


class ClubTypes(models.TextChoices):
    business = "business",
    software = "software",
    science = "science",
    hobbies = "hobbies",
    entertainment = "entertainment",
