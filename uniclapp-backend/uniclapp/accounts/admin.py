from django.contrib import admin
from accounts import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.ClubSupervisor)
admin.site.register(models.ClubCoordinator)
