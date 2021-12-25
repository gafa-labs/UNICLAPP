from rest_framework import serializers
from event.models import Event, EventEnrollment
from club.serializers import ClubSerializer


class AdvancedEventSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ["id", "name", "description", "location", "start_datetime",
                  "end_datetime", "rate", "number_of_participants", "club", "event_status"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "description", "location", "start_datetime",
                  "end_datetime", "rate", "number_of_participants",
                  "club", "event_status", "is_online", "ge_status", "ge_point", "zoom_link"]


class BasicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "club", "name", "description", "location",
                  "start_datetime", "end_datetime", "ge_status", "is_online", ]


class ClubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "name", "description", "location", "ge_status",
                  "is_online", "start_datetime", "end_datetime", "ge_point", "event_status"]


class EventEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventEnrollment
        fields = "__all__"


class EventHistorySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventEnrollment
        fields = "__all__"


class RateEventSerializer(serializers.ModelSerializer):
    model = EventEnrollment
    fields = "rate"


class EventTrackerSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"


class EventConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_status",)
