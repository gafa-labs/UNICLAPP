from django.db import models
from place import enums


class Building(models.Model):
    name = models.CharField(max_length=10, choices=enums.BuildingNames.choices)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(
        max_length=3, choices=enums.ClassrooomNames.choices)
    building = models.OneToOneField(
        Building, on_delete=models.CASCADE, related_name="classrooms")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.building.name} - {self.name}'
