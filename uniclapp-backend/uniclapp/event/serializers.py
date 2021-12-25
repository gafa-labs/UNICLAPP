from rest_framework import serializers
from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BasicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "club", "name", "description", "location",
                  "start_datetime", "end_datetime", "ge_status", "is_online", ]
