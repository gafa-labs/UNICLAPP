from django.contrib import admin
from event.models import Event, EventEnrollment

admin.site.register(Event)
admin.site.register(EventEnrollment)
