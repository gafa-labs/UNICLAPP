from rest_framework import serializers
from event.models import Event, EventEnrollment


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BasicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "club", "name", "description", "location",
                  "start_datetime", "end_datetime", "ge_status", "is_online", ]


class ClubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "description", "location", "ge_status",
                  "is_online", "start_datetime", "end_datetime", "ge_point"]


class EventEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventEnrollment
        fields = "__all__"
