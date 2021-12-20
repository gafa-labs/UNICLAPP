from django.db import models


class ClubTypes(models.TextChoices):
    business = "business",
    entertainment = "entertainment",
    sport = "sport",
    policy = "policy",


class BuildingNames(models.TextChoices):
    B = "B",
    MA = "MA",
    SA = "SA",
    SB = "SB",
    EE = "EE",
    FF = "FF",
    FC = "FC",
    MSSF = "MSSF",


class ClassrooomNames(models.TextChoices):
    pass


class DepartmentNames(models.TextChoices):
    CS = "Computer Science",
    EE = "Electric and Electonical",
    IE = "Industrial Engineering",
