from rest_framework import serializers
from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class OnlineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ["building"]


class F2FEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ["zoom_link"]
